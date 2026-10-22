import radar
from sources import ev, when


def test_merge_and_times():
    assert when("2026-10-22T17:00:00.000Z") == "2026-10-22T19:00+02:00"
    assert when("2026-11-10 18:00:00") == "2026-11-10T18:00+01:00"
    con = radar.connect(":memory:")
    a = ev(title="Hundzig", start="2026-10-24T20:00+02:00", venue="BLÅ", url="https://a")
    b = ev(title="HUNDZIG!", start="2026-10-24T21:00+02:00", venue="Blå", url="https://b", price="250 NOK")
    radar.upsert(con, "blaa", a, "now")
    radar.upsert(con, "ticketmaster", b, "now")
    rows = con.execute("SELECT * FROM events").fetchall()
    assert len(rows) == 1 and rows[0]["price"] == "250 NOK" and rows[0]["url"] == "https://a"
    assert con.execute("SELECT count(*) FROM event_sources").fetchone()[0] == 2
    t = radar.clean_tags({"interests": ["jazz", "bogus"], "vibe": "x", "price": "free", "group_friendly": 1})
    assert t == {"interests": ["jazz"], "vibe": None, "group_friendly": True, "price": "free", "language": None}


if __name__ == "__main__":
    test_merge_and_times()
    print("ok")
