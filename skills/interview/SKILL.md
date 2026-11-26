---
name: interview
description: Interview the user in depth about a feature, project or idea, then write a detailed spec. Asks probing, non-obvious questions about behavior, UX, technical approach, edge cases, risks and tradeoffs until nothing important is open, then saves the spec in the project's .plans folder. Use for "interview me", "help me spec this", "turn this idea into a spec", or before building something large.
---

# Interview

Turn what's in the person's head into a spec someone could build from.

## Asking

- Ask with your question tool when you have one (in Claude Code, AskUserQuestion), a few related questions at a time; otherwise ask in chat.
- Skip anything the codebase or the conversation already answers. Read the relevant code first.
- Prefer questions they haven't thought about: what happens at the edges, what they would cut first, who else is affected, what failure looks like, how they'll know it worked.
- Offer concrete options when a choice has a few sensible answers, and say which you'd pick and why.
- Cover the ground that matters for this topic: goals and non-goals, users and flows, UI and states, data and APIs, technical approach, edge cases and errors, performance, security and privacy, rollout, and open risks.
- Keep going round by round until the remaining unknowns are small enough to decide during building. Then ask whether anything is missing.

## Writing the spec

Save it as `.plans/<topic>-spec.md` in the current project (create `.plans/` if needed), using a short kebab-case topic. Never save it under `~/.claude/`. Write the absolute path in your reply.

Structure:
1. Summary: what and why, in a few sentences
2. Goals and non-goals
3. Users and key flows
4. Requirements, grouped by area
5. UI and states, including empty, loading and error states
6. Technical approach and data
7. Edge cases and how each is handled
8. Risks, open questions and decisions made, with the reason for each
9. How to verify it works

Use the person's own words for decisions they made. Mark anything you inferred rather than asked.

## Their instructions

Focus on whatever the person asked about when they ran this skill.
