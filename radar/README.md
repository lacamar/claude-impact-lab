# nabo-radar

Collects upcoming Oslo events (next 30 days) from structured feeds into SQLite, then tags them with a local model for Nabo matching.

```
nabo-radar collect [source ...]   # fetch; sources: rockefeller blaa vulkan deichman litteraturhuset subjekt nb afm meetup eventbrite ticketmaster
nabo-radar tag [--limit N]        # tag untagged events via llama-server
nabo-radar run                    # collect, then tag (what the timer runs)
nabo-radar list [--days 7] [--json]
```

Enable the daily run: `systemctl --user enable --now nabo-radar.timer`

| Variable | Default |
|---|---|
| `NABO_RADAR_DB` | `$XDG_DATA_HOME/nabo-radar/radar.db` |
| `NABO_RADAR_LLM_URL` | `http://localhost:9080/v1/chat/completions` |
| `NABO_RADAR_LLM_WAIT` | `0` seconds to wait for the model to load (timer: 600) |

Same title, venue and day from several sources is stored once; `event_sources` keeps every link. Deichman is limited to adult audiences.
