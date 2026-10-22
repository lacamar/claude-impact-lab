#!/usr/bin/python3
import argparse
import json
import os
import re
import sqlite3
import sys
import time
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path

from sources import OSLO, SOURCES

WINDOW_DAYS = 30
LLM_URL = os.environ.get("NABO_RADAR_LLM_URL", "http://localhost:9080/v1/chat/completions")
LLM_WAIT = int(os.environ.get("NABO_RADAR_LLM_WAIT", "0"))
INTERESTS = ["music", "jazz", "rock", "electronic", "classical", "nightlife", "art", "film", "theatre", "dance",
             "literature", "talks", "politics", "science", "tech", "startup", "design", "food", "drinks", "sport",
             "outdoors", "crafts", "comedy", "language", "volunteering", "community", "family", "wellbeing"]
VIBES = ["social", "quiet", "lively", "party", "learning", "hands-on"]
PRICES = ["free", "low", "mid", "high", "unknown"]

SCHEMA = """
CREATE TABLE IF NOT EXISTS events (
  key TEXT PRIMARY KEY, title TEXT NOT NULL, start TEXT NOT NULL, end TEXT, venue TEXT, address TEXT,
  lat REAL, lon REAL, price TEXT, url TEXT, image TEXT, description TEXT, category TEXT, audience TEXT,
  source_tags TEXT, tags TEXT, first_seen TEXT NOT NULL, last_seen TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS event_sources (
  key TEXT NOT NULL REFERENCES events(key), source TEXT NOT NULL, url TEXT NOT NULL,
  PRIMARY KEY (key, source, url));
CREATE INDEX IF NOT EXISTS events_start ON events(start);
"""
FIELDS = ["title", "start", "end", "venue", "address", "lat", "lon", "price", "url", "image",
          "description", "category", "audience", "source_tags"]


def db_path():
    if p := os.environ.get("NABO_RADAR_DB"):
        return Path(p)
    return Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local/share") / "nabo-radar/radar.db"


def connect(path=None):
    path = path or db_path()
    if str(path) != ":memory:":
        Path(path).parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con


def norm(s):
    return re.sub(r"\W+", "", (s or "").casefold())


def key(e):
    return f"{norm(e['title'])}|{norm(e['venue'])}|{e['start'][:10]}"


def upsert(con, source, e, now):
    e = {**e, "source_tags": json.dumps(e["source_tags"], ensure_ascii=False)}
    k = key(e)
    cols = ", ".join(FIELDS)
    keep = ", ".join(f"{f} = coalesce({f}, excluded.{f})" for f in FIELDS if f not in ("title", "start"))
    con.execute(f"INSERT INTO events (key, {cols}, first_seen, last_seen) VALUES (?, {', '.join('?' * len(FIELDS))}, ?, ?) "
                f"ON CONFLICT(key) DO UPDATE SET {keep}, last_seen = excluded.last_seen",
                [k, *(e[f] for f in FIELDS), now, now])
    con.execute("INSERT OR IGNORE INTO event_sources VALUES (?, ?, ?)", (k, source, e["url"] or ""))


def collect(con, only=None):
    start = datetime.now(OSLO).replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + timedelta(days=WINDOW_DAYS)
    now = datetime.now(OSLO).isoformat(timespec="seconds")
    failed = []
    for name, fn in SOURCES.items():
        if only and name not in only:
            continue
        n = 0
        try:
            for e in fn(start, end):
                if not e["title"] or not e["start"] or not (start.isoformat() <= e["start"] < end.isoformat()):
                    continue
                if e["end"] and datetime.fromisoformat(e["end"]) - datetime.fromisoformat(e["start"]) > timedelta(days=2):
                    continue
                upsert(con, name, e, now)
                n += 1
            con.commit()
        except Exception as ex:
            con.rollback()
            failed.append(name)
            print(f"{name}: FAILED {ex!r}", file=sys.stderr)
            continue
        print(f"{name}: {n}")
    total = con.execute("SELECT count(*) FROM events WHERE start >= ?", (start.isoformat(),)).fetchone()[0]
    print(f"upcoming events in database: {total}")
    return failed


def llm(messages):
    body = {"messages": messages, "temperature": 0, "response_format": {"type": "json_object"},
            "chat_template_kwargs": {"enable_thinking": False}}
    req = urllib.request.Request(LLM_URL, json.dumps(body).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.loads(json.loads(r.read())["choices"][0]["message"]["content"])


def clean_tags(t):
    t = t if isinstance(t, dict) else {}
    return {"interests": [i for i in t.get("interests") or [] if i in INTERESTS][:4],
            "vibe": t.get("vibe") if t.get("vibe") in VIBES else None,
            "group_friendly": bool(t.get("group_friendly")),
            "price": t.get("price") if t.get("price") in PRICES else "unknown",
            "language": t.get("language") if t.get("language") in ("no", "en", "mixed", "none") else None}


PROMPT = f"""You tag Oslo events for Nabo, an app that sends small groups of people to events together.
For each event return an object with:
- interests: 1-4 of {INTERESTS}
- vibe: one of {VIBES}
- group_friendly: true if 3-6 people could go together and talk or do it together
- price: one of {PRICES} (low < 200 NOK, mid < 500 NOK, high otherwise)
- language: "no", "en", "mixed" or "none" (for music without talk)
Answer with one JSON object mapping each event id to its tags. No other text."""


def tag(con, batch=10, limit=None):
    deadline = time.monotonic() + LLM_WAIT
    while True:
        try:
            urllib.request.urlopen(LLM_URL.rsplit("/chat/", 1)[0] + "/models", timeout=5)
            break
        except Exception as ex:
            if time.monotonic() > deadline:
                print(f"local model not reachable at {LLM_URL} ({ex}); skipping tagging", file=sys.stderr)
                return 0
            time.sleep(10)
    today = datetime.now(OSLO).date().isoformat()
    rows = con.execute("SELECT key, title, start, venue, price, category, audience, source_tags, description "
                       "FROM events WHERE tags IS NULL AND start >= ? ORDER BY start" + (f" LIMIT {int(limit)}" if limit else ""),
                       (today,)).fetchall()
    done = 0
    for i in range(0, len(rows), batch):
        chunk = rows[i:i + batch]
        items = [{"id": str(n), **{k: r[k] for k in ("title", "start", "venue", "price", "category", "audience")},
                  "tags": r["source_tags"], "description": (r["description"] or "")[:300]} for n, r in enumerate(chunk)]
        try:
            out = llm([{"role": "system", "content": PROMPT},
                       {"role": "user", "content": json.dumps(items, ensure_ascii=False)}])
        except Exception as ex:
            print(f"tagging batch failed: {ex!r}", file=sys.stderr)
            continue
        for n, r in enumerate(chunk):
            if str(n) in out:
                con.execute("UPDATE events SET tags = ? WHERE key = ?", (json.dumps(clean_tags(out[str(n)])), r["key"]))
                done += 1
        con.commit()
        print(f"tagged {done}/{len(rows)}", file=sys.stderr)
    return done


def upcoming(con, days):
    start = datetime.now(OSLO).replace(hour=0, minute=0, second=0, microsecond=0)
    seen = (start - timedelta(days=2)).isoformat()
    rows = con.execute("SELECT e.*, group_concat(DISTINCT s.source) AS sources FROM events e "
                       "JOIN event_sources s USING (key) WHERE start >= ? AND start < ? AND last_seen >= ? "
                       "GROUP BY e.key ORDER BY start",
                       (start.isoformat(), (start + timedelta(days=days)).isoformat(), seen)).fetchall()
    out = []
    for r in rows:
        d = dict(r)
        d["source_tags"] = json.loads(d["source_tags"] or "[]")
        d["tags"] = json.loads(d["tags"]) if d["tags"] else None
        d["sources"] = d["sources"].split(",")
        out.append(d)
    return out


def main():
    ap = argparse.ArgumentParser(prog="nabo-radar", description="Collect Oslo events for Nabo.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("collect", help="fetch events from all sources")
    c.add_argument("sources", nargs="*", help=f"only these sources: {', '.join(SOURCES)}")
    t = sub.add_parser("tag", help="tag untagged events with the local model")
    t.add_argument("--limit", type=int)
    sub.add_parser("run", help="collect, then tag")
    ls = sub.add_parser("list", help="show upcoming events")
    ls.add_argument("--days", type=int, default=7)
    ls.add_argument("--json", action="store_true")
    a = ap.parse_args()

    con = connect()
    if a.cmd == "collect":
        if bad := set(a.sources) - set(SOURCES):
            ap.error(f"unknown sources: {', '.join(bad)}")
        sys.exit(1 if collect(con, a.sources) else 0)
    if a.cmd == "tag":
        tag(con, limit=a.limit)
    if a.cmd == "run":
        failed = collect(con)
        tag(con)
        sys.exit(1 if len(failed) == len(SOURCES) else 0)
    if a.cmd == "list":
        evs = upcoming(con, a.days)
        if a.json:
            json.dump(evs, sys.stdout, ensure_ascii=False, indent=1)
            return
        for e in evs:
            tags = ",".join(e["tags"]["interests"]) if e["tags"] else ""
            print(f"{e['start'][5:16].replace('T', ' ')}  {e['title'][:60]:<60}  {(e['venue'] or '')[:28]:<28}  {tags}")
        print(f"{len(evs)} events", file=sys.stderr)


if __name__ == "__main__":
    main()
