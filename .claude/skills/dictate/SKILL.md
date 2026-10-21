---
name: dictate
description: Voice mode. Listen to the team through the mic, transcribe, reply, listen again. Use when the user runs /dictate, says "voice mode", "listen", or wants to talk instead of type.
---

Run `dictate-listen` with Bash (timeout 120000). It records until 2 s of silence, max 90 s, and prints the transcript.

Treat the transcript as the team's message. Several people share the mic; a turn may start with a name ("Anna: ..."). Track who said what. Transcripts can misspell names and Norwegian words; infer from context and ask only if it matters.

Reply as usual, then run `dictate-listen` again. Keep looping.

Stop looping when the output is `(silence)` twice in a row, when someone says "stop listening" or similar, or when the user types. Say in one line that voice mode is off and `/dictate` starts it again.
