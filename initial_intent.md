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

## Decisions, 11:30 interview with Claude

Answers from the team to five clarifying questions. Open decisions 1 to 4 above are now resolved as follows.

### Problem statement (to confirm)

**Someone who knows a few people in Oslo struggles to actually meet them, because every hangout depends on one person asking and coordinating, and after a few "can't that day" replies they stop asking and assume nobody wants to.**

### The person

A mix of the newcomer and the local who stopped asking: knows a few people here, has said "sometime" to them, and has given up initiating. Not the organiser, not strangers one-on-one.

### What the agent does

- Initiates instead of you. Proposals come from the agent, so declining is private and nobody is exposed.
- Asks everyone as itself, collects yes or no from each side, and only surfaces a plan when all sides said yes.
- Starts with small groups around an interest, where nobody is the initiator. One-to-one comes later, from who you clicked with.
- After an event you say, anonymously, who you would like to see again. The agent uses that for the next proposal, as a pair or a group.

### What the agent knows

A short onboarding conversation: interests, age, gender, location, optional calendar access. After that it learns from what you accept and decline.

### The demo, in order of build

1. Onboarding, moved through fast.
2. A group proposal with time and place, and the scheduling around it.
3. The mechanism visible: both sides of the screen, each person answering privately, the plan appearing only when everyone said yes.
4. The after-event step, "who would you like to see again", feeding the next proposal.

Steps 2 and 3 are the core and come first. Step 4 can be a single static screen if time runs out.

## Decisions, 11:45 after "play the person"

Claude walked through the four steps as Jonas, someone who stopped asking. The team's answers:

### What makes it not "Meetup with extra steps"

- **Curation, not known faces.** A group proposal does not need one person you already know. The card says "this event is happening, and three people who match your interests are going." The agent's job is to make sure the people in a group fit each other, so the vibe is good and people come back. Meetup selects for people who create events; this selects for fit.
- **Pitch it as a personalised matchmaker**, agent-initiated. "Agent" is the mechanism, not the sales line.
- **First time with support, then alone.** A first experience can be with a close match or someone you know. Later events can be solo or all weak ties, which is how Creator Brunch Club events work.

### The proposal is a decision, not a conversation

- An event card: what, where, when, who is coming, roughly how many. **Yes or no only, no maybe.** Maybe means no.
- No chatbot in the loop once onboarding is done.

### Once the group is set

- Everyone sees a **who's going** section: a profile card per person with picture, name and a few interest bullets. Takes away the "thrown in a pit with strangers" feeling.
- A **profile picture is required** before attending. Part of the curation.

### The plan survives declines

- If one person says no, the plan goes ahead for the rest, with a lower threshold. An event with only one person is off. Rescheduling is a possible fallback.

### Privacy of a no, confirmed

- Each person is asked the same neutral way. Nobody is told "Jonas already said yes."
- After the event, "who would you like to see again" is a silent mutual match. The screen says, in Hinge's style, that the other person will not see your answer unless they picked you too.

### Onboarding effort is a feature

- A somewhat taxing onboarding filters out low-effort people and flakers, who ruin the experience for the ones who try. Hinge over Tinder.

### Parked for later, not today

- Hinge-style nudges: decline too many proposals and you are paused; accept but never show up and you are asked to attend before getting more.
- A "sometime" list of people you already know. Not needed for the group-first demo.

## Decisions, 12:30 after the closed loop

- **The loop is right.** After a group event you pick who you'd like to see again. Only a mutual pick leads to anything, and then Nabo proposes an actual plan with a time, which both answer yes or no. Interest first, plan second, so a no on the plan can be about timing rather than the person.
- **The soft spot is accepted.** If a mutual pair's plan doesn't happen, the one who said yes can infer the other passed. Same leak Hinge accepts. Nabo only proposes when it's mutual, so a yes is a safe bet most of the time.
- **Antisocial score.** People who keep saying no to people they themselves picked, or who say yes and don't show up, get quietly de-ranked. The agent learns it over time. Nobody is told their score.
- **Flake phone.** A fifth phone, someone who said yes last week and didn't go, now paused. Worth showing.
- **Demo script.** Wanted, one page, which button when.
- **Be more ambitious.** The hosts keep asking for it. The team likes what it has and wants a bolder frame on top, not a different product.
