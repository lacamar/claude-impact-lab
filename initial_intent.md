# Initial intent

Claude Impact Lab, Mesh Oslo, 21 October 2026. Distilled from the team's conversation 10:25–11:06 (three OBS recordings and the live `/dictate` captures). Raw transcripts are in [`transcripts/`](transcripts/).

## Area

**My community.** Loneliness, and how hard it is to meet people and keep meeting them, especially when you are new to a city.

## What the team said about the problem

- You get tired of initiating. You ask a few times, people "can't that day", and you stop asking. Then you stop hanging out because you assume nobody wants to.
- "Yeah, yeah, let's get a coffee" and it never happens. If you push, you get ghosted or a lukewarm reply. The mental attrition of that is bad.
- Coordination is draining. Doodles, calendars, "I'm sick", "I'm travelling". People give up on coordination before they give up on each other.
- New in Oslo: all the effort is one-sided, which is tiresome and demoralising. People who already knew a couple of people here had a kickstart; those who didn't, didn't.
- Shift work and demanding jobs leave no energy. There has to be something worth going to, and it has to be easy.
- Meeting people through a cause (EA, safer AI, a professional network) leaves it unclear whether you are friends or colleagues. Networking and transactional atmospheres don't help.
- In Norway the way to make friends is to do something together: sport, skiing, kids, work, volunteering. Doing something meaningful is a multiplier.
- What works: curated, low-pressure, non-transactional events where nothing is expected of you (Creator Brunch Club). Robust friendships come from repeated low-pressure interactions in the same place.

## Problem, one line

Top-level, in the team's words: **lower the cost of initiation.** Or positively framed: simplify connection.

Candidate problem statements, not yet confirmed:

- *[Someone new in Oslo] struggles to meet people and keep meeting them, because every hangout needs someone to initiate and coordinate, and after a few failed tries they stop.*
- *[A person who says "coffee sometime"] could actually meet, if nobody had to carry the asking, the chasing and the risk of being turned down.*

## The idea: an agent that initiates for you

Move initiation away from the person and onto an agent.

- The agent proposes; you confirm or decline. "You guys are having coffee Thursday" flips the default: the emphasis moves from building up the courage to ask to saying "no thanks". A no is private; the other side never knows they were asked.
- Rejection by an agent carries no social cost. Nobody is embarrassed, nobody is exposed.
- It absorbs the coordination: finds the time, asks everyone, confirms. The thing that makes people give up is handled in the background.
- Not necessarily a chat. It can run in the background and surface only a proposal with a reason: "coffee with John because he likes the same music", "walk a shelter dog Saturday, you said you like dogs".
- Two kinds of demand:
  - **Org → people.** A shelter needs four volunteers Thursday. "I need four strong people tomorrow at 10 to move a piano." Push it to people who fit and are free; they confirm.
  - **People → people.** "I'm into music, there's a jazz concert." "Coffee sometime." Personal intent that needs a match.
- Inputs: what you are interested in, and that you are open to suggestions. Offer three time slots to verify rather than relying on a calendar (people don't look at their calendars). Learn from what gets declined.
- **Go as two.** Reluctant people bring a plus-one to take the anxiety away. If two newcomers get sent to the same event and click, send them to the next one together. Lowers the barrier, builds bonds.
- **After the event:** "these two I'd like to see again", anonymously. Match those people up again, and match the group to the events that fit all of them. AI is good at pulling signals from disparate sources and matching.
- Tinder for activities was the first framing; the team later cooled on it (see below). "Middleman agent" is the framing that stuck.

## Objections and constraints the team raised

- **Swipe fatigue.** Bumble has had friend-matching for years; nobody uses it. Don't build another Tinder.
- **Trust.** "I wouldn't trust these things." Trust and the value proposition need to be obvious.
- **Cold start / network effect.** A platform with nobody on it matches nobody. Which side comes first is the biggest platform decision (Airbnb and Craigslist). Leverage existing networks and recent contacts instead of building a new social network.
- **GDPR.** Classic ML matching on age, interests, life stage works, but data access in Europe is the hard part.
- **No commercial thinking today.**
- Keep it to what can be built in a few hours.

## Success measures

- Events a person actually attends.
- People see each other again (recurrence).

## Open decisions

1. Who is the one person for the demo: the newcomer, the organiser who needs four volunteers, or the person with a "sometime" list.
2. Org → people or people → people first.
3. How the agent contacts the other side: drafts for you to send, messages as itself on your behalf, or agent-to-agent.
4. What the smallest clickable version is.

## State at 11:06

- 11:03, about three hours left; demos 13:15–14:00.
- Repo set up (this one). A draft single-page prototype exists in [`index.html`](index.html) ("Nabo": proposal cards with a why-you line and yes/no), built before the team asked to finish planning first. Treat it as a sketch, not a decision.
- One team member is switching from Claude Code to Antigravity and wants to use the BMAD method to structure the work.
- Next step the team named: formalise the problem, then narrow.
