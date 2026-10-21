---
title: 'Social Initiation Agent (Nabo) — Prototype & Interaction Flow'
type: 'feature'
created: '2026-10-21'
status: 'draft'
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

</frozen-after-approval>

## Code Map

- `claude-impact-lab/index.html` -- Existing static draft with card stack, basic yes/no buttons, and week list. Needs architectural upgrade to support rich proposal inspection, "Why you" transparency, organizer demands, "Go as two" pairing, and post-event recurrence feedback.
- `claude-impact-lab/initial_intent.md` -- Team consensus and core problem statement.
- `claude-impact-lab/transcripts/*.md` -- Voice transcripts documenting the lived experience in Oslo, the psychological barriers, and key product pillars.

## Tasks & Acceptance

**Execution:**
- [ ] `claude-impact-lab/index.html` -- Redesign and implement the complete Nabo Agent experience:
  - Header with persona context and agent status indicator ("Nabo active: 4 proposals coordinated").
  - Rich proposal cards with transparent "Why you" context, timing options, and participant avatars.
  - Interactive Actions: Private Decline (with safety guarantee), Accept, and "Go with a buddy" option.
  - "Your Week" calendar summary with confirmed events and details.
  - "Post-Event Recurrence" view demonstrating the private feedback loop ("meet again" flywheel).
  - Perspective toggle (Newcomer Jonas vs Organizer Kari) or simulated incoming agent message notifications.
- [ ] `claude-impact-lab/README.md` -- Update documentation with project pitch, the problem statement, demo instructions, and team hackathon presentation script for 13:15.

**Acceptance Criteria:**
- Given a user viewing a proposal, when they decline, then the system confirms the decline was 100% private and other attendees are not notified.
- Given a proposal with multiple attendees, when accepted, then the system provides an option to "Go as two" with another newcomer.
- Given a completed event, when the user marks "Liked hanging out", then future proposals highlight this affinity.
- The interface feels responsive, modern, visually compelling, and runs out of the box in any browser.

## Implementation Notes

## Spec Change Log

## Review Triage Log

## Design Notes

The design aesthetic should reflect Nordic warmth and trustworthiness: clean typography, calm organic palette (warm sand/cream background `#f7f5f0`, deep forest slate `#1e293b`, warm amber accents `#d97706`, and reassuring sage green `#059669`), crisp card hierarchy, and glassmorphic micro-toasts that emphasize safety and ease.
