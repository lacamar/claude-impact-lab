# Architecture & Technical Design: Nabo Working MVP

## Overview
Nabo is architected as an autonomous client-side agent application engineered for maximum reliability, speed, and demonstrable utility at hackathon evaluation.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          NABO AGENT APPLICATION                         │
├───────────────────────────────────┬─────────────────────────────────────┤
│        USER EXPERIENCE COCKPIT    │     AUTONOMOUS AGENT ENGINE         │
│  - Dual-View Layout (Phone/Console│  - Intent Parser                    │
│  - Proposal Card Deck (Touch/Keys)│  - Matchmaking & Availability Logic │
│  - Intake Modal (Contacts/Intents)│  - Privacy / Social Shield Filter   │
│  - Weekly Calendar Schedule       │  - Recurrence Flywheel Evaluator    │
│  - Calendar Export (.ics & GCal)  │  - Live Telemetry Stream Broadcaster│
└───────────────────────────────────┴─────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     LOCAL PERSISTENCE LAYER (localStorage)              │
│  - profiles: { jonas, kari, custom }                                    │
│  - contacts: [ { id, name, context, interests, availability, affinity } ]│
│  - intents: [ { id, type, title, location, when, tags, host, slots } ]  │
│  - proposals: [ active queue derived from matching ]                    │
│  - confirmed_events: [ accepted hangouts with buddy assignments ]       │
│  - past_events: [ completed hangouts with mutual affinity flags ]       │
│  - telemetry_log: [ append-only audit trail ]                           │
└─────────────────────────────────────────────────────────────────────────┘
```

## Key Technical Components

### 1. Dynamic Matchmaking Engine
```javascript
function matchIntentsToContacts(profile, contacts, intents) {
  // 1. Matches user availability and interests against active intents
  // 2. Evaluates contacts in the 'sometime' list who share matching tags
  // 3. Ranks proposals by mutual affinity score (from past feedback loop)
  // 4. Formulates dynamic "Why You" attribution text explaining the match
}
```

### 2. Social Shield (Private Decline)
Every decline triggers:
- Card dismissal animation (`out-left` / `-150% translateX`).
- `private_declines` counter increment.
- Telemetry log entry: `[SHIELDED DECLINE] Proposal archived. Zero notification emitted.`
- Absolute suppression of notifications to the other party.

### 3. Calendar Export (.ics & Google Calendar)
- Generates RFC 5545 compliant `.ics` data URI with event title, location, description, and timestamps.
- Formats `https://calendar.google.com/calendar/render?action=TEMPLATE&text=...` deep-link URL.

### 4. Recurrence Flywheel
- Rating an attendee as "👍 See again" updates that contact's `affinityScore += 1`.
- Contacts with `affinityScore > 0` are given 3x weighting for follow-up proposal generation.
