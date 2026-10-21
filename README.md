# Claude Impact Lab

One-day build event. Pick a person and their problem, prototype a solution with Claude as a single HTML file, demo it in five minutes.

- **When:** Wednesday 21 October 2026, 09:30–14:00
- **Where:** Mesh Youngstorget, Møllergata 6–8, 0179 Oslo ([map](https://www.google.com/maps/search/?api=1&query=59.9140854%2C10.7465087))
- **Hosts:** Claude Community Oslo, [GritAI](https://www.gritai.studio/) (Aleksander Stensby), Mesh Oslo
- **Part of:** Day of AI, [Oslo Innovation Week](https://lu.ma/oslo-innovation-week)
- **Follows:** Claude Conversation, 30 September 2026 at Mesh (~50 people, small groups, no talks)
- **Guide:** <https://www.gritai.studio/meetups/claude-impact-lab> ([norsk](https://www.gritai.studio/no/meetups/claude-impact-lab))
- **Brief for Claude:** <https://www.gritai.studio/meetups/claude-impact-lab/brief> — copy in [BRIEF.md](BRIEF.md)
- **Luma:** <https://luma.com/claude-qv5r> (full, waitlist open)

## Schedule

| Time | What |
|---|---|
| 09:30–10:00 | Welcome and teams |
| 10:00–10:20 | Pick a problem |
| 10:20–11:45 | Build round one |
| 11:45–12:15 | Lunch |
| 12:15–13:00 | Build round two |
| 13:00–13:15 | Get ready to show it |
| 13:15–14:00 | Demos, five minutes per team |
| Evening | Optional: show it on the big stage |

## Six steps, one problem

Start with a person and their problem, not with the tool.

1. **Pick an area** — one of the three, as a team.
2. **Let Claude interview you** — one question at a time, to find the problem.
3. **Define the problem** — one person, what they might struggle with, and why. Before any solution.
4. **Build the smallest version** — one screen that works. Test it.
5. **Improve and expand** — make it better, bigger or more ambitious.
6. **Show it** — five minutes at the demos, mostly clicking through it.

Three steps from problem to prototype: define the problem (who, what changes, why it matters) → explore solutions (ask for many ways, include a bold one) → prototype and imagine (a first clickable version, plus a sketch of the finished thing).

## Problem areas

From the two questions at Claude Conversation.

**My job** — What does AI mean for my job (also the one you train for or left)?
- Which task eats the most of your week?
- What do you wish you had time for?
- Who in your field is falling behind, and why?

**My kids** — What is AI doing to my kids? Seen from home and school.
- Where do children meet AI today, at home or at school?
- What do parents or teachers worry about?
- What would help a family talk about it?

**My community** — What is AI doing to my community? Neighbourhood, clubs, teams, groups, online forums. How people meet, belong and help each other, not public services.
- Who in your neighbourhood is left out?
- Where do you meet people today, in clubs, groups or online?
- What could help people help each other?

The five steps from the Claude Conversation table sheets, one question each: What does this mean for us, here? What are we hoping for, and what are we worried about? What can we do about it? What stands in our way? Where do we start?

Problem statement form: `[Person] struggles with [what], because [why]` or `[Person] could [what], if [what changes]`.

## Quick start

Paste into Claude. It reads the brief, then interviews the team.

```
Help us get started. https://www.gritai.studio/meetups/claude-impact-lab/brief
```

In this repo with Claude Code, `claude` picks up [CLAUDE.md](CLAUDE.md) and [BRIEF.md](BRIEF.md) on its own.

## Prompts to copy

Paste one, fill in the brackets, read what comes back, then change it.

**01 Find the problem** (plan)
```
We are a team at a one-day build event. Our area is [area]. Interview us with five questions, one at a time, to find a real problem worth working on today. Then write it in the form who struggles with what, because why.
```

**02 Plan the smallest version** (plan)
```
Write a short plan for the smallest version we can build in two hours. What it does, what it leaves out, and the one screen that matters most. Do not build anything yet.
```

**03 Build it as one page** (build)
```
Build the plan as a single HTML file we can open in a browser. Keep it to one screen. Use made-up example data, never real names or personal details.
```

**04 Check it works** (build)
```
Open the page in the browser and try it the way a first-time user would. Fix anything broken before you tell us it is done.
```

**05 Test it as the person** (test)
```
Act as [the person from our problem statement]. Use the page to [the task]. Tell us where you got stuck, then make the three changes that matter most.
```

**06 Tell the story** (show)
```
Make our idea into one HTML page that tells the story of [who] before and after, as a page we scroll through. Then help us plan a five-minute demo.
```

## When you get stuck

Short starters to type into Claude:

- Ask me questions first
- How could we …?
- Which step should we cut?
- Show me three different ways
- Make it work for a nurse on a night shift
- Who struggles most with this?
- What are we missing?
- Explain it to a 12-year-old
- What is the smallest version we could build today?
- What if we …?
- What could go wrong?
- What would make this a pleasure to use?
- Give me a bolder idea
- Turn this into a clickable prototype
- What smaller problem hides inside this one?
- How can I be more ambitious?
- Make it simpler
- What would this look like for the whole city?
- Play the person who uses it
- Make it work on a phone
- What would a far better version look like?
- Who else has solved something like this?
- What should the first screen say?
- Write the demo in three sentences

## Three more words at the end (creative HTML)

Claude builds sliders, steps and stories only when asked. Add a few plain words to the end of a prompt.

| Want | Say | Example |
|---|---|---|
| Let me move it | "Add sliders" | How many hours would a nurse save a week? |
| Take me through it | "Make it a wizard, one step at a time" | A parent answers five questions and gets a family plan |
| Walk me through the point | "Make it a scrolling story" | Before and after, one scene at a time |
| Show me less | "Not so overwhelming" | Main point on one screen, detail behind a click |
| Show me more than one | "Give me three directions, side by side" | Hopeful, worried, and a middle way |
| Make me want to look at it | "Make it feel alive" | Motion and timing |
| Think bigger | — | A whole school, profession or neighbourhood; what goes wrong at scale, who must be involved |

Then give feedback in rounds: look at the page, say what is off, add a few words each round. One good ending, from Thariq Shihipar's ELI5 skill at Anthropic:

```
explain like I'm someone who knows nothing about this topic, using a HTML artifact with big pictures and few words
```

## Demos, 13:15–14:00

Five minutes per team, four parts:

| Part | Time | |
|---|---|---|
| The problem | 45 s | Read the statement |
| Who it is for | 45 s | The person it helps |
| Show it | 150 s | Click through it live |
| What next | 60 s | The first step |

Big stage in the evening is optional. Before you leave: share the HTML file with everyone on the team, agree on one step to take this week, swap contact details.

## $100 Claude API credits

Only for Claude Code and the API — not claude.ai or the Claude app. Once per person. Offer expiry is on the claim page.

1. Open <https://platform.claude.com/offers/c4d0026b-5c56-44dc-b91e-64e298ced09e> (sign in if asked).
2. Sign in at <https://console.anthropic.com>, Settings → Organization, copy the Organization ID.
3. Paste the organisation ID in the form. The claude.ai ID is rejected.
4. Wait a couple of minutes, then sign in to Claude Code with the Console account, or use an API key from the console.

Nothing after a few minutes? Ask a host.

## What a good result looks like

- One HTML file that opens in any browser, nothing to install
- Made-up example data only, never real names or personal details
- Makes one challenge or opportunity concrete for one person, hints at what it could mean for many
- Shareable after the day

## FAQ

- **Do I need to know how to code?** No. Claude builds; what you know about the problem matters more.
- **Can we change our problem?** Yes, until about lunch. After lunch, improve what you have.
- **How do we share what we built?** One HTML file. Download it from Claude or find it in your Claude Code folder, send it to the team before you leave.
- **Claude or Claude Code?** Either. claude.ai suits everyone; Claude Code suits people who already build software.
- **Real data?** No. Claude can make realistic test data.
- **Team can't agree?** Quick start, let Claude interview with multiple choice, ask for three directions including a bold one, pick what you can get somewhere with before lunch.
- **Stuck?** Say what you see and what you want instead, one change at a time. Hosts are in the room.

## Links

- GritAI: [site](https://www.gritai.studio/) · [events](https://www.gritai.studio/events) · [community](https://www.gritai.studio/build-with-ai-community) · [YouTube](https://www.youtube.com/@gritaistudio) · [Instagram](https://www.instagram.com/gritaistudio/) · [LinkedIn](https://www.linkedin.com/company/gritai/)
- Claude Community: [claude.com/community](https://claude.com/community) · [events calendar](https://lu.ma/claudecommunity)
- Hosts on Luma: [GritAI](https://lu.ma/user/gritai) · [Mesh Oslo](https://lu.ma/user/MeshOslo)
