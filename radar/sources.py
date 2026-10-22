import html
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

OSLO = ZoneInfo("Europe/Oslo")
UA = "Mozilla/5.0 (X11; Linux aarch64; rv:140.0) Gecko/20100101 Firefox/140.0 nabo-radar/0.1"
DEICHMAN_ADULT = {"Voksne", "For alle", "Senior", "Du som lærer norsk"}


def get(url, params=None):
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "nb,en"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def get_json(url, params=None):
    return json.loads(get(url, params))


def when(s):
    if not s:
        return None
    s = s.strip().replace(" ", "T", 1)
    if len(s) == 10:
        s += "T00:00:00"
    dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    return (dt.replace(tzinfo=OSLO) if dt.tzinfo is None else dt.astimezone(OSLO)).isoformat(timespec="minutes")


def text(s):
    return html.unescape(re.sub(r"<[^>]+>", " ", s or "")).strip() or None


def ev(**kw):
    return {"end": None, "address": None, "lat": None, "lon": None, "price": None, "image": None,
            "description": None, "category": None, "audience": None, "source_tags": [], **kw}


def edge(base):
    for e in get_json(f"{base}/api/eventsEdge"):
        cf, place = e.get("custom_fields") or {}, e.get("place") or {}
        if not cf.get("published", True) or place.get("city") not in (None, "Oslo"):
            continue
        yield ev(title=e["name"], start=when(e["start_time"]), end=when(cf.get("end_time")),
                 venue=place.get("name"), address=place.get("address"),
                 lat=place.get("latitude"), lon=place.get("longitude"),
                 price="Gratis" if cf.get("freeEntry") else cf.get("cover"),
                 url=cf.get("ticketUrl") or base, description=(e.get("details") or "")[:2000] or None,
                 category=cf.get("type"), audience=cf.get("age"), source_tags=e.get("tags") or [])


def deichman(start, end):
    data = get_json("https://deichman.no/api/library-events", {"page": 1})
    pages = -(-data["total"] // max(1, len(data["searchResults"])))
    # The API returns pages 1..N cumulatively, so one request for the last page gets everything.
    for e in get_json("https://deichman.no/api/library-events", {"page": pages})["searchResults"]:
        if e.get("cancelled") or e.get("privateEvent") or e.get("targetAudience") not in DEICHMAN_ADULT:
            continue
        img = (e.get("image") or {}).get("url")
        yield ev(title=e["title"], start=when(e["startTime"]), end=when(e.get("endTime")),
                 venue=f"Deichman {e['library']}", url=f"https://deichman.no/hva-skjer/{e['id']}",
                 image=img and urllib.parse.urljoin("https://deichman.no", img),
                 description=e.get("ingress"), category=e.get("type"), audience=e.get("targetAudience"),
                 source_tags=e.get("tags") or [])


def litteraturhuset(start, end):
    q = """*[_type=="event" && !fromArchive && count(dates[eventStart >= $from && eventStart < $to]) > 0]{
      "slug": slug.current, "title": coalesce(title.nb, title.en), "desc": coalesce(description.nb, description.en),
      dates, english, childFriendly, "status": admission.status, "rooms": venues[].room->title}"""
    res = get_json("https://4bjarlop.apicdn.sanity.io/v2023-01-01/data/query/production",
                   {"query": q, "$from": json.dumps(utc(start)), "$to": json.dumps(utc(end))})["result"]
    for e in res:
        for d in e["dates"]:
            s = datetime.fromisoformat(d["eventStart"].replace("Z", "+00:00"))
            yield ev(title=e["title"], start=when(d["eventStart"]),
                     end=when((s + timedelta(minutes=d.get("eventDuration") or 0)).isoformat()) if d.get("eventDuration") else None,
                     venue="Litteraturhuset", address="Wergelandsveien 29",
                     url=f"https://www.litteraturhuset.no/nb/arrangement/{e['slug']}",
                     description=e.get("desc"), price="Gratis" if e.get("status") == "free" else None,
                     audience="Barn" if e.get("childFriendly") else None,
                     source_tags=[r for r in e.get("rooms") or [] if r] + (["english"] if e.get("english") else []))


def wp_pages(url, params):
    page = 1
    while True:
        try:
            batch = get_json(url, {**params, "per_page": 100, "page": page})
        except urllib.error.HTTPError as e:
            if e.code == 400:
                return
            raise
        if not batch:
            return
        yield from batch
        page += 1


def subjekt(start, end):
    for e in wp_pages("https://subjekt.no/wp-json/wp/v2/event", {}):
        a = e.get("acf") or {}
        m = a.get("event_map") or {}
        if (a.get("event_city") or m.get("city")) != "Oslo" or a.get("event_schedule_type") == "period":
            continue
        occ = a.get("event_custom_occurrences") or [{"start": a.get("event_start_datetime"), "end": a.get("event_end_datetime")}]
        for o in occ:
            if not o.get("start"):
                continue
            yield ev(title=text(e["title"]["rendered"]), start=when(o["start"]), end=when(o.get("end")),
                     venue=a.get("event_venue_name") or m.get("name"), address=m.get("address"),
                     lat=m.get("lat"), lon=m.get("lng"),
                     url=a.get("event_external_url") or e["link"], description=text(e.get("excerpt", {}).get("rendered")))


def nb(start, end):
    # ponytail: only events published in the last year; widen `after` if long-announced events go missing
    after = (start - timedelta(days=365)).replace(tzinfo=None).isoformat(timespec="seconds")
    for e in wp_pages("https://www.nb.no/wp-json/wp/v2/event", {"after": after}):
        m = e.get("meta") or {}
        if m.get("event_attendance_mode") == "online":
            continue
        yield ev(title=text(e["title"]["rendered"]), start=when(m.get("event_start_datetime")),
                 end=when(m.get("event_end_datetime")), venue="Nasjonalbiblioteket",
                 address="Henrik Ibsens gate 110", url=e["link"], price=text(m.get("event_ticket_price_text")),
                 description=text(m.get("event_short_description")) or text(e.get("excerpt", {}).get("rendered")),
                 source_tags=[t for t in [m.get("event_infoscreen_place_name")] if t])


def afm(start, end):
    for e in wp_pages("https://www.afmuseet.no/wp-json/wp/v2/event", {}):
        m = e.get("meta") or {}
        yield ev(title=text(e["title"]["rendered"]), start=when(m.get("afm_event_from")), end=when(m.get("afm_event_to")),
                 venue="Astrup Fearnley Museet", address="Strandpromenaden 2", url=e["link"],
                 description=text(e.get("excerpt", {}).get("rendered")))


def find_events(node):
    if isinstance(node, list):
        for n in node:
            yield from find_events(n)
    elif isinstance(node, dict):
        t = node.get("@type")
        if t == "Event" or (isinstance(t, str) and t.endswith("Event")) or (isinstance(t, list) and "Event" in t):
            yield node
        else:
            for v in node.values():
                yield from find_events(v)


def jsonld(urls):
    def run(start, end):
        for url in urls:
            for block in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', get(url), re.S):
                try:
                    data = json.loads(block)
                except json.JSONDecodeError:
                    continue
                for e in find_events(data):
                    loc = e.get("location") or {}
                    loc = loc[0] if isinstance(loc, list) and loc else loc
                    addr = loc.get("address") if isinstance(loc, dict) else None
                    addr_s = ", ".join(str(addr.get(k)) for k in ("streetAddress", "addressLocality") if addr.get(k)) if isinstance(addr, dict) else addr
                    where = json.dumps(loc, ensure_ascii=False).lower()
                    if loc and "oslo" not in where:
                        continue
                    offers = e.get("offers") or {}
                    offers = offers[0] if isinstance(offers, list) and offers else offers
                    img = e.get("image")
                    yield ev(title=text(e.get("name")), start=when(e.get("startDate")), end=when(e.get("endDate")),
                             venue=loc.get("name") if isinstance(loc, dict) else None, address=addr_s or None,
                             url=e.get("url") or url, image=img[0] if isinstance(img, list) and img else img if isinstance(img, str) else None,
                             price=f"{offers['price']} {offers.get('priceCurrency', '')}".strip() if isinstance(offers, dict) and offers.get("price") not in (None, "") else None,
                             description=text(e.get("description")))
    return run


def utc(dt):
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


SOURCES = {
    "rockefeller": lambda s, e: edge("https://www.rockefeller.no"),
    "blaa": lambda s, e: edge("https://www.blaaoslo.no"),
    "vulkan": lambda s, e: edge("https://vulkanarena.no"),
    "deichman": deichman,
    "litteraturhuset": litteraturhuset,
    "subjekt": subjekt,
    "nb": nb,
    "afm": afm,
    "meetup": jsonld(["https://www.meetup.com/find/?location=no--Oslo&source=EVENTS"]),
    "eventbrite": jsonld([f"https://www.eventbrite.com/d/norway--oslo/all-events/?page={p}" for p in (1, 2, 3)]),
    "ticketmaster": jsonld(["https://www.ticketmaster.no/discover/oslo"]),
}
