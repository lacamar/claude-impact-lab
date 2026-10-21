---
title: 'Social Initiation Agent (Nabo) — Prototype & Interaction Flow'
type: 'feature'
created: '2026-10-21'
status: 'done'
baseline_commit: '063b997c66bdec9a20797c11274ae4c9316fd02b'
route: 'dispatch'
review_loop_iteration: 0
context: ['claude-impact-lab/initial_intent.md', 'claude-impact-lab/BRIEF.md']
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** In cities like Oslo, meeting people and sustaining friendships is exhausting because initiation carries a heavy burden of social risk (fear of rejection, ghosting) and coordination fatigue. People frequently say "let's grab coffee sometime," but neither side follows through, and social ties dissolve before they begin.

**Approach:** Build "Nabo" — an autonomous middleman agent that absorbs initiation and coordination costs. Nabo proactively proposes concrete hangouts with a transparent "Why you" explanation, coordinates timing across participants in the background, guarantees private non-embarrassing rejections (the other person never knows you declined), supports "Go as two" pairing for anxiety reduction, and closes the loop with post-event anonymous feedback to nurture recurring friendships.

## Boundaries & Constraints

**Always:**
- Keep all data strictly local and demo-ready with realistic mock profiles and scenarios (no external API keys or auth required for the hackathon demo).
- Prioritize zero social embarrassment: any "No" response must be completely private.
- The UI must clearly articulate "Why You": the explicit reason and shared context behind every agent proposal.
- Self-contained and runnable directly in the browser (vanilla HTML/CSS/JS) with responsive modern styling and smooth micro-interactions.

**Never:**
- Never build a swipe/dating-style app ("Tinder for activities" is an explicit anti-pattern noted by the team; this is a trusted personal coordinator).
- Never require complex calendar integration or auth sign-ins that fail during a live demo.
- Never expose who declined or why an event didn't happen.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Proposal Accept | User taps "Yes" on proposed activity (e.g., Coffee with Mia) | Activity added to "Your Week" schedule; agent confirms in background; feedback prompt scheduled post-event | Display celebratory confirmation toast |
| Proposal Decline | User taps "No" on proposed activity | Card dismissed silently; marked as privately declined; other party is never notified | Feedback toast: "Declined privately. Mia will never know." |
| "Go as Two" Pairing | User accepts a larger event or community task (e.g. Move piano, Dog walk) | Prompt to pair with another accepted attendee or newcomer buddy to reduce anxiety | If user opts out of pairing, proceed as solo attendee |
| Post-Event Recurrence Loop | User views "Past Hangouts" | Shows who attended; allows private 1-click "I'd like to see again"; agent feeds this into future pair suggestions | Anonymous; no notification sent unless mutual |

## Decisions
- **Demo Hero Persona:** Dual perspective toggle enabled — users can switch between Jonas (newcomer with "sometime" list) and Kari (organizer coordinating community activities) to showcase both Person-to-Person and Org-to-People demand.
- **Recurrence Loop:** Include a dedicated "Past & Feedback" view where users can privately indicate who they'd like to see again, reinforcing the repeat low-pressure interaction flywheel.
- **Layout & Presentation:** Split screen layout featuring a sleek central mobile device preview accompanied by a live "Agent Behind-the-Scenes Reasoning & Messaging" stream (visualizing Nabo autonomously coordinating in the background).
- **Pitch Package:** Provide a dedicated 5-minute hackathon pitch script and live demonstration checklist in `claude-impact-lab/PITCH.md`.

</frozen-after-approval>

## Code Map

- `claude-impact-lab/index.html` -- Main interactive prototype: split desktop/mobile layout with phone card deck, agent reasoning sidebar, dual persona switcher, "Go as two" pairing dialogs, and post-event feedback view.
- `claude-impact-lab/PITCH.md` -- 5-minute pitch deck narrative and demo walkthrough script for 13:15.
- `claude-impact-lab/initial_intent.md` -- Core problem definition and background context.
- `claude-impact-lab/transcripts/*.md` -- Original voice transcripts from Claude Impact Lab.

## Tasks & Acceptance

**Execution:**
- [x] `claude-impact-lab/index.html` -- Build the complete Nabo Agent prototype:
  - Responsive split layout: Sleek phone frame + Live Agent Operations console (real-time logs of agent outreach, negotiations, and confirmations).
  - Persona Switcher: Toggle between Jonas (newcomer) and Kari (community organizer) with custom proposal feeds.
  - Interactive Proposal Cards: "Why You" attribution, timing slots, private decline ("Mia will never know"), accept, and "Go as two" buddy pairing.
  - "Your Week" Confirmed Calendar: Displays scheduled hangouts and location details.
  - "Post-Event Recurrence" Feedback Loop: Anonymous 1-click rating to feed repeat hangout recommendations.
  - Audio/Visual cues: Micro-animations, celebratory toasts, and Nordic warm aesthetic.
- [x] `claude-impact-lab/PITCH.md` -- 5-minute pitch script (The Problem, The Persona, The Live Demo, Why AI / Middleman, Next Steps).
- [x] `claude-impact-lab/README.md` -- Update README with overview and quickstart instructions.

**Acceptance Criteria:**
- Given a user viewing a proposal, when they decline, then the system confirms the decline was 100% private and other attendees are not notified.
- Given a proposal with multiple attendees, when accepted, then the system provides an option to "Go as two" with another newcomer.
- Given a completed event, when the user marks "Liked hanging out", then future proposals highlight this affinity.
- The interface feels responsive, modern, visually compelling, and runs out of the box in any browser.

## Implementation Notes

- Upgraded `claude-impact-lab/index.html` from a basic draft into a responsive dual-view demo cockpit.
- Added live agent telemetry console on the right side of the desktop view to showcase autonomous coordination, calendar checks, and privacy enforcement in real time.
- Implemented "Go as two" buddy pairing to directly solve newcomer arrival anxiety highlighted in team audio transcripts.
- Implemented the post-hangout mutual affinity check ("See again") to demonstrate the recurring friendship flywheel.
- Created `claude-impact-lab/PITCH.md` featuring a 5-minute presentation script broken into timing segments (Problem, Solution, Live Demo, Why AI, Next Steps) ready for 13:15.

## Spec Change Log

## Review Triage Log

## Design Notes

The design aesthetic should reflect Nordic warmth and trustworthiness: clean typography, calm organic palette (warm sand/cream background `#f7f5f0`, deep forest slate `#1e293b`, warm amber accents `#d97706`, and reassuring sage green `#059669`), crisp card hierarchy, and glassmorphic micro-toasts that emphasize safety and ease.
