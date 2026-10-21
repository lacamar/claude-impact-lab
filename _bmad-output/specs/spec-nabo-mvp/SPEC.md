---
id: SPEC-nabo-mvp
companions: ['architecture.md']
sources: ['claude-impact-lab/initial_intent.md', 'claude-impact-lab/BRIEF.md']
---

> **Canonical contract.** This SPEC and the files in `companions:` are the complete, preservation-validated contract for what to build, test, and validate.

# Nabo — Autonomous Social Initiation Agent Full Working MVP

## Why

In cities like Oslo, loneliness thrives not from a lack of goodwill, but from the brutal emotional and logistical cost of initiating hangouts ("let's grab coffee sometime"). Initiation requires someone to be the vulnerable party, risk rejection or lukewarm ghosting, and coordinate back-and-forth dates. People give up on coordination long before they give up on each other. Nabo transforms initiation from an anxious human burden into an autonomous background agent service: absorbing the social risk through private non-embarrassing rejections, negotiating timing automatically, offering newcomer pairing ("Go as two"), and nurturing repeat connections through an anonymous recurrence loop.

## Capabilities

- **CAP-1: User Profile & Availability Engine**
  - **intent:** User can configure and edit their personal profile (name, neighborhood, hobbies/interests, weekly free slots, and buddy preference).
  - **success:** Updating preferences immediately alters the active matchmaking criteria and recalculates matching compatibility across all contacts and community requests.

- **CAP-2: "Sometime List" Contact Intake**
  - **intent:** User can add and manage real or informal contacts (name, where met, context notes, tags like "coffee", "padel", "running").
  - **success:** Newly added contacts are persisted and immediately factored into the autonomous proposal generation pipeline.

- **CAP-3: Intent & Demand Dispatch (P2P and Community/Org)**
  - **intent:** User or organizer can post a new raw hangout intent or volunteer demand (e.g. "Coffee near Torggata", "Looking for 3 people to play board games Saturday", "Help move furniture at youth club").
  - **success:** The agent parses the intent, matches it with available contacts whose interests and time align, and generates actionable proposal cards.

- **CAP-4: Autonomous Matching & "Why You" Rationale Engine**
  - **intent:** System evaluates mutual availability, shared tags, and past affinity to generate proposal cards containing explicit "Why You" transparency.
  - **success:** Each proposal card displays a verifiable reason (e.g. shared music tag, mutual promise at recent meetup, dry weather window for cycling).

- **CAP-5: Social Shield (Zero-Risk Private Decline)**
  - **intent:** User can decline any proposal with complete privacy, guaranteeing the other party is never informed that an offer was extended.
  - **success:** Dismissed cards trigger an immediate safe confirmation ("Declined privately. Mia will never know."), record a suppression event in the agent audit log, and produce zero notifications for the counterparty.

- **CAP-6: "Go as Two" Anxiety Shield**
  - **intent:** For group or volunteer events, user can select "Go as two" to be paired with another newcomer arrival buddy.
  - **success:** User is paired with a designated attendee, reducing arrival intimidation and noting the buddy on the schedule.

- **CAP-7: Real Calendar Integration & .ics Export**
  - **intent:** User can export confirmed hangouts directly to their real calendar via downloadable `.ics` files and 1-click Google Calendar links.
  - **success:** Clicking "Export to Calendar" downloads a valid iCalendar `.ics` file containing exact start/end times, venue, and attendee summary, and provides a functioning Google Calendar deep link.

- **CAP-8: Anonymous Recurrence Flywheel**
  - **intent:** User can review past events and submit anonymous thumbs-up ("See again") ratings for attendees they clicked with.
  - **success:** When mutual affinity is registered, the system records it in the local graph and automatically schedules a low-pressure follow-up suggestion within 7 days.

- **CAP-9: Local Persistent Storage & Demo Reset**
  - **intent:** Entire state (profiles, contacts, custom intents, scheduled hangouts, ratings, and telemetry logs) persists in browser `localStorage`.
  - **success:** Reloading the browser preserves all changes; clicking "Reset Demo Scenario" cleanly re-seeds default hackathon demo personas (Jonas and Kari).

## Constraints

- Client-side browser execution with zero external server dependencies: ensures 100% demo uptime and resilience during hackathon judging and offline presentations.
- 100% privacy guarantee on negative decisions: no data or webhook may ever transmit a "declined" state to another user.
- Responsive split layout: on desktop/projector screens, display mobile app alongside live agent reasoning console; on small screens, provide an intuitive view toggle.

## Non-goals

- Real multi-device cloud authentication or live SMS/WhatsApp gateway in MVP (simulated telemetry logs demonstrate this flow).
- Payment or commercial monetization features.

## Success signal

A user can enter a real friend or intent, run Nabo's autonomous matchmaking, privately accept or decline with zero social exposure, download a working `.ics` calendar invite to their real phone/laptop, and rate a past hangout to trigger repeat event suggestions.
