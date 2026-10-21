---
name: dictate
description: Voice mode. Record the team through the mic for as long as they want, transcribe when they say stop, reply, record again. Use when the user runs /dictate, says "voice mode", "listen", or wants to talk instead of type.
---

`dictate-listen` is a toggle. First call starts recording and prints `(recording)`. Second call stops it and prints the transcript.

Loop:

1. Run `dictate-listen` with Bash. It returns at once with `(recording)`. End your turn with one short line: recording, type anything when done.
2. The user's next message (any text, or /dictate again) means they are done talking. Run `dictate-listen` again (timeout 600000) to get the transcript. If the message has text of its own, read that too.
3. Treat the transcript as the team's message. Several people share the mic; a turn may start with a name ("Anna: ..."). Track who said what. Transcripts can misspell names and Norwegian words; infer from context and ask only if it matters.
4. Reply as usual, then go to 1.

Stop looping when someone says "stop listening" or similar, or the user asks to stop. Say in one line that voice mode is off and `/dictate` starts it again.
