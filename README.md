# Super Design Skills

Twelve skills that make coding agents good at design: building and judging screens until they score 8/10, landing pages, theme prototypes, scroll sites, motion, images, brand, review, demos and marketing. Each big skill carries the expert playbooks it needs and loads them only when they're useful, so your agent stays fast.

Works with Claude Code, Codex, Cursor, Gemini CLI, OpenCode and other agents that support skills, plus Claude.ai.

## Install: give this repo to your agent

Paste this into your coding agent:

> Install the skills from https://github.com/Jack-Attackz101/super-design-skills and tell me what I can do with them.

Your agent follows `AGENTS.md`: it installs the skills for itself, checks them, and walks you through what each one does.

### Or install it yourself

```bash
git clone https://github.com/Jack-Attackz101/super-design-skills.git ~/super-design-skills
~/super-design-skills/install.sh
```

That links the skills into `~/.claude/skills` (Claude Code) and `~/.agents/skills` (Codex, Cursor and others). Start a new session afterwards. `./install.sh --help` lists the options.

- **Any skills-compatible agent:** `npx skills add Jack-Attackz101/super-design-skills -g`
- **Claude Code plugin:** `/plugin marketplace add Jack-Attackz101/super-design-skills`, then `/plugin install super-design@super-design-skills`. Plugin skills are prefixed, for example `/super-design:design`.
- **Claude.ai, Claude desktop chat and Cowork:** run `python3 scripts/make_claude_ai_zips.py`, then upload the zips from `dist/` in Customize → Skills. Skills there also load in Claude Code on the web and in Claude Code sessions signed in to the same account.

## The skills

| Command | What it does |
|---|---|
| `/design` | **Super Design.** Sets an art direction, builds or redesigns any screen, then an independent judge AI scores and critiques it from screenshots while the builder fixes issues, until it reaches 8/10 |
| `/landing-page` | Landing pages and marketing sites: intake, structure, conversion copy, SEO and a strict visual system, finished with the judge loop |
| `/prototype` | One gallery page with many full versions of your site in different themes (36 styles in 8 families), each openable full screen |
| `/scroll-site` | Cinematic scroll-driven sites: Lenis and GSAP, pinned scenes, scrubbed sequences, word reveals |
| `/animate` | All other motion: micro-interactions, cursor effects, particles, shaders, globes, React Native, and fixing janky motion |
| `/image` | Generate hero art, comps and transparent assets, or source real photos and logos |
| `/brand` | Brand kits, logo systems and design systems (tokens, components, docs, migrations) |
| `/review` | A graded report with no changes: the same rubric and judge as `/design`, plus slop, accessibility, performance and originality audits |
| `/demo` | Faux product UI, walkthrough videos, page-to-video, voiceover, progress screenshots, publishing to GitHub |
| `/marketing` | Campaign plans, competitor briefs, posts, emails, SEO audits, brand-voice checks, reports |
| `/interview` | Interviews you in depth about a feature, then writes a spec |
| `/agentation` | Adds the Agentation feedback toolbar to a Next.js app and connects it to your agent |

**[SKILLS.md](SKILLS.md)** has every skill's full description, when to use it, prompts to try, and the mini skills inside it.

### How the judge loop works

`/design`, `/landing-page` and `/review` share one rubric (`skills/review/references/rubric.md`): ten weighted dimensions with anchored scores and hard caps. A broken phone layout, for example, caps a page at 5/10. Each round, a fresh judge agent sees only screenshots, the rubric and a short brief, never the builder's reasoning, so it can't be talked into a good score. The loop stops at 8.0 with no dimension below 7, or after 5 rounds, or when the score stalls; then it offers two new directions.

## Also worth getting: REA

[REA (Reverse Engineer Anything)](https://github.com/morluto/rea) isn't included, because it ships with its own MCP server and setup. Get it with `npx rea-agents setup`.

## Requirements

- Screenshot, video and gallery features use Node.js 18+ and Playwright; video needs ffmpeg.
- Optional: the awwwards MCP server for design references (`install.sh --awwwards` for Claude Code).

## Credits and license

This pack builds on skills by Meng To, Emil Kowalski, Leon Lin (taste-skill), INSANE0777 (Awwwards MCP), arla6ka, Lucas Markes (Hairline), Damir Sokolovsky (unslop), codeswithroh (Tastemaker), Benji Taylor (Stageshow), ConardLi and Anthropic. Every module keeps its original license and credits; see [CREDITS.md](CREDITS.md). The pack's own files are under the MIT license in [LICENSE](LICENSE).
