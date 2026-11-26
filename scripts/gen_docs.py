"""Regenerate SKILLS.md and CREDITS.md from the skill folders. Run: python3 scripts/gen_docs.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import catalog

ORDER = ["design", "landing-page", "prototype", "scroll-site", "animate", "image", "brand", "review", "demo", "marketing", "interview", "agentation"]
ABOUT = {
"design": ("Super Design", "The main design skill. It works out what a page or screen is for, sets one clear art direction, builds or redesigns it, then hands it to a judge AI. The judge never sees the builder's reasoning: it scores the page from screenshots against a 10-point rubric and writes a full critique. The builder fixes the worst issues and the loop repeats until the page scores 8/10 with no dimension below 7.",
 ["An app screen, dashboard or component looks generic or unfinished", "A page \"looks AI-generated\" and you want it fixed, not just flagged", "An honest critique of a design before you show it to anyone", "UX copy, a developer handoff spec, or a user research plan", "Award-winning references before you choose a direction"],
 ["Redesign the settings page so it stops looking AI-generated", "Critique this dashboard and fix it until it scores 8/10", "Write the empty states and error messages for the signup flow"]),
"landing-page": ("Landing Page", "Web design for pages that sell: one offer, one audience, one primary action. It runs intake questions, picks the structure and layout, writes the conversion copy and SEO, applies a strict visual system, then finishes with the Super Design judge loop.",
 ["A new landing page for a product, client or launch", "Rewriting a homepage that tries to do too much", "A pricing page", "A premium, award-style marketing site", "Rebuilding a page inspired by a reference site without copying it"],
 ["Build a landing page for my app that gets people to join the waitlist", "Rewrite this homepage hero so the offer is obvious", "Make a pricing page with three plans"]),
"prototype": ("Prototype", "Turns one site into many. It pulls your real content, builds several complete versions in different themes, and puts them on one gallery page. Open any version full size or full screen, flip through with the arrow keys, then take the winner into Super Design. Themes come from 36 visual styles in 8 families, plus brand-inspired style recipes.",
 ["Showing a client several directions before committing", "Choosing between dark, light, editorial or brutalist looks", "Turning a day's inspiration references into five original builds", "Seeing how the same copy feels in different styles"],
 ["Prototype my site in six different themes", "Show me an editorial, a brutalist and a dark glass version of this page"]),
"scroll-site": ("Scroll Site", "Cinematic, scroll-driven websites where scrolling moves the story: smooth scroll, pinned scenes, scrubbed image sequences and word-by-word reveals. It plans the story in chapters, then builds one chapter at a time with one scroll engine.",
 ["An Awwwards-style launch or portfolio site", "Scrubbing a video or image sequence as you scroll", "Pinned sections, horizontal chapters, progress timelines", "Copying how a reference site's scroll motion works", "Debugging GSAP or ScrollTrigger"],
 ["Turn this product story into a cinematic scroll site", "Pin the features section and scrub the phone mockup on scroll"]),
"animate": ("Animate", "All motion that isn't scroll storytelling. It decides whether something should move at all, then picks the purpose, tool, properties, easing and duration, and makes sure it's interruptible and smooth. Covers micro-interactions, cursor effects, particles, shaders, globes and React Native motion, and audits motion that already exists.",
 ["Button, hover and page-transition polish", "A cursor trail, particles or a shader background", "A globe or 3D accent on a landing page", "Motion that feels janky or drops frames", "Recreating an interaction you saw in a video", "Naming an effect you can only describe"],
 ["Make these buttons and cards feel alive", "Add a subtle particle background to the hero", "Why does this animation stutter on my phone?"]),
"image": ("Image", "Gets the images a page needs. It generates art-directed hero images, section comps, app screen concepts and transparent assets when an image tool is available, and sources real photos and real company logos when that's the honest choice.",
 ["A hero or section visual that matches the art direction", "Real stock photos for people and places", "Company or tool logos for a \"used by\" row", "Transparent PNG ornaments, icons or sprites"],
 ["Generate a hero image for this page", "Find real photos for the team section and add proper alt text"]),
"brand": ("Brand", "Brand identity and the system under every page. It makes brand kits and logo systems, and builds, audits, documents or migrates a design system: tokens, components, states and docs.",
 ["A new brand or a refresh", "Logo concepts and guideline boards", "Hardcoded colors everywhere and inconsistent UI", "Extracting tokens from an existing app", "Documenting a component, or picking a component library"],
 ["Make a brand kit for my coffee shop", "Our UI is a mess: build us a design system from what's there"]),
"review": ("Review", "A graded report on any page or site, with no changes made. It uses the same rubric and independent judge as Super Design, so a review score and a design score mean the same thing. Full mode adds audits for AI-design slop, accessibility, performance, motion, originality and worst-case data.",
 ["\"Is this ready to ship?\"", "Grading a site before a pitch", "Finding out why something looks AI-generated", "Accessibility evidence (WCAG 2.1 AA)", "Stress-testing a screen with long names and empty states"],
 ["Review my site and grade it", "Do a full audit of this page before launch"]),
"demo": ("Demo", "Shows the product, and shows the work. It builds realistic fake product UI for hero shots and feature cards, records polished browser walkthroughs, turns pages into short videos with voiceover, sends progress screenshots as you build, and publishes finished projects to GitHub with a proper README and preview.",
 ["A product shot for a hero or feature card", "A short walkthrough video of a feature", "Before-and-after pictures for an update", "Publishing a finished project with a GitHub Pages link"],
 ["Make an animated product shot of our dashboard for the hero", "Record a 20-second walkthrough of the checkout flow"]),
"marketing": ("Marketing", "Plans, writes and measures marketing for your business or your clients: campaign briefs, competitor positioning, blog, social, email and launch copy, SEO audits, brand-voice checks and performance reports. Pulls live numbers from tools like HubSpot or Ahrefs when those are connected.",
 ["A launch or campaign plan", "A week of social posts or a newsletter", "An onboarding or win-back email sequence", "An SEO audit with an action plan", "Checking copy against a brand voice", "A monthly marketing report"],
 ["Plan the launch campaign for our new feature", "Write a five-email onboarding sequence"]),
"interview": ("Interview", "Interviews you in depth about a feature or project, asking questions that aren't obvious, until the picture is complete. Then it writes a detailed spec into the project's .plans folder.",
 ["Before building something big", "Turning a vague idea into a buildable spec", "Surfacing tradeoffs and edge cases early"],
 ["Interview me about the new onboarding flow"]),
"agentation": ("Agentation", "Adds the Agentation visual feedback toolbar to a Next.js app, so you can click on the page and leave notes your coding agent can read. It verifies the whole loop, not just that the toolbar appears.",
 ["Giving visual feedback on a running app straight to your agent", "Setting up a review loop for a client build"],
 ["Set up Agentation in this Next.js app and connect it to you"]),
}
LICENSES = {"MengTo/Skills": "MIT", "emilkowalski/skills": "MIT", "Leonxlnx/taste-skill": "MIT", "INSANE0777/Awwwards-mcp": "MIT",
            "arla6ka/skills": "MIT", "lucasmarkes/hairline": "MIT", "codeswithroh/tastemaker": "MIT", "benjitaylor/skills": "MIT (stageshow/LICENSE)",
            "ConardLi/garden-skills": "MIT", "heydamir/unslop (CC BY 4.0)": "CC BY 4.0", "Anthropic marketing plugin (Apache 2.0)": "Apache 2.0",
            "Anthropic design plugin 1.2.0": "Apache 2.0"}
URLS = {"MengTo/Skills": "https://github.com/MengTo/Skills", "emilkowalski/skills": "https://github.com/emilkowalski/skills",
        "Leonxlnx/taste-skill": "https://github.com/Leonxlnx/taste-skill", "INSANE0777/Awwwards-mcp": "https://github.com/INSANE0777/Awwwards-mcp",
        "arla6ka/skills": "https://github.com/arla6ka/skills", "lucasmarkes/hairline": "https://github.com/lucasmarkes/hairline",
        "codeswithroh/tastemaker": "https://github.com/codeswithroh/tastemaker", "benjitaylor/skills": "https://github.com/benjitaylor/skills",
        "ConardLi/garden-skills": "https://github.com/ConardLi/garden-skills", "heydamir/unslop (CC BY 4.0)": "https://github.com/heydamir/unslop",
        "Anthropic marketing plugin (Apache 2.0)": "https://github.com/anthropics/knowledge-work-plugins", "Anthropic design plugin 1.2.0": "https://github.com/anthropics/knowledge-work-plugins"}

def main():
    c = catalog.load()
    here = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
    L = ["# Skills\n\nTwelve skills. Each big skill runs a full workflow and loads its mini skills (modules) only when it needs them.\n",
         "\n| Command | Skill | What it does |\n|---|---|---|\n"]
    for k in ORDER:
        t, about, _, _ = ABOUT[k]
        L.append(f"| `/{k}` | {t} | {about.split('. ')[0].rstrip('.')}. |\n")
    for k in ORDER:
        t, about, uses, ex = ABOUT[k]; info = c[k]
        n = sum(len(g["items"]) for g in info["groups"])
        L.append(f"\n## /{k}: {t}\n\n{about}\n\n**Use it when**\n\n" + "".join(f"- {u}\n" for u in uses))
        L.append("\n**Try**\n\n" + "".join(f"- `/{k} {e}`\n" for e in ex))
        if n:
            L.append(f"\n<details><summary>{n} mini skills inside</summary>\n\n")
            for g in info["groups"]:
                L.append(f"**{g['g']}**\n\n" + "".join(f"- `{m['n']}`: {m['d']}\n" for m in g["items"]) + "\n")
            L.append("</details>\n")
    L.append("\n## Not included: REA\n\nREA (Reverse Engineer Anything) pairs well with these skills but ships separately with its own MCP server. Get it from https://github.com/morluto/rea, or run `npx rea-agents setup`.\n")
    open(os.path.join(here, "SKILLS.md"), "w").write("".join(L))

    C = ["# Credits\n\nThis pack merges skills by many authors. Each module keeps its original files, credit lines and license files. ",
         "Third-party modules stay under their own licenses below; the MIT license in `LICENSE` covers only this pack's own files ",
         "(each skill's top-level `SKILL.md`, `SOURCES.md`, the review rubric, judge protocol and scripts, the prototype gallery, and the repo scripts and docs).\n\n",
         "| Source | License | Modules |\n|---|---|---|\n"]
    by = {}
    for k in ORDER:
        for mod, s in c[k]["sources"].items(): by.setdefault(s, []).append(f"{k}/{mod}")
    for s, mods in sorted(by.items(), key=lambda x: -len(x[1])):
        name = f"[{s}]({URLS[s]})" if s in URLS else s
        lic = LICENSES.get(s, "Not stated; check with the repo owner before sharing publicly")
        C.append(f"| {name} | {lic} | {len(mods)}: " + ", ".join(f"`{m}`" for m in sorted(mods)) + " |\n")
    C.append("| Repo owner (uploaded) | Not stated; check before sharing publicly | `interview`, `agentation` |\n")
    open(os.path.join(here, "CREDITS.md"), "w").write("".join(C))
    print("wrote SKILLS.md and CREDITS.md")
main()
