"""Build site/index.html from site/template.html and the skill folders. Run: python3 scripts/build_site.py"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import catalog, gen_docs

CARD = {
 "design": "Builds or redesigns any screen, then a judge AI scores it until it reaches 8/10.",
 "landing-page": "Pages that convert: strategy, copy and a strict visual system.",
 "prototype": "Your site in six themes on one gallery, each one full screen.",
 "scroll-site": "Cinematic sites where scrolling drives the story.",
 "animate": "Micro-interactions, cursor effects, particles and shaders that run smoothly.",
 "image": "Generated hero art, or real photos and logos.",
 "brand": "Brand kits, logos and design systems.",
 "review": "A graded design report, plus accessibility and performance audits.",
 "demo": "Fake product UI, walkthrough videos and progress screenshots.",
 "marketing": "Campaign plans, posts, emails, SEO and reports.",
 "interview": "Asks the questions you missed, then writes the spec.",
 "agentation": "Click-to-comment feedback from your Next.js app to your agent.",
}

HOW = {
 "design": ["Read the page and its job", "Set one art direction", "Build or redesign", "Judge scores from screenshots", "Fix worst first, repeat to 8/10"],
 "landing-page": ["Offer, audience, one action", "Structure and layout", "Copy and SEO", "Strict visual system", "Judge loop to 8/10"],
 "prototype": ["Pull your real content", "Pick six theme families", "Build each version in parallel", "Gallery with full-screen viewer"],
 "scroll-site": ["Write the story as chapters", "Pick one scroll engine", "Build and lock each chapter", "Check phone, motion, speed"],
 "animate": ["Should it move at all?", "Purpose, tool, properties", "Easing and duration", "Interruption and exit", "Reduced motion and 60fps"],
 "image": ["Generate or source?", "Make or fetch the image", "Right format and size", "Alt text and license"],
 "brand": ["Identity or system?", "Run the matching module", "Name tokens by purpose", "Check on real screens"],
 "review": ["Shoot desktop and phone", "Independent judge scores", "Slop, a11y, speed audits", "Graded report, worst first"],
 "demo": ["Pick the output", "Build or record it", "One feature per clip", "Share it"],
 "marketing": ["Plan the campaign", "Write the pieces", "Check the brand voice", "Measure and report"],
 "interview": ["Read what's already known", "Ask the non-obvious questions", "Keep going until nothing's open", "Write the spec to .plans/"],
 "agentation": ["Inspect the Next.js app", "Mount the toolbar in dev only", "Connect it to your agent", "Prove one note arrives"],
}

def module_desc(skill, mod):
    """One complete sentence from the module's own description, never cut mid-thought."""
    p = os.path.join(HERE, "..", "skills", skill, "modules", mod, "MODULE.md")
    t = open(p).read() if os.path.exists(p) else ""
    m = re.search(r"^description:\s*(.*?)(?=^\w[\w-]*:|^---)", t, re.S | re.M)
    d = re.sub(r"\s+", " ", m.group(1)).strip().strip('"').strip("'") if m else ""
    d = re.sub(r"^[>|][-+]?\s*", "", d)
    first = re.match(r"(.{30,170}?[.!?])(\s|$)", d)
    s = first.group(1) if first else d
    if len(s) > 170:
        s = s[:170]
        s = s[:max(s.rfind(", "), s.rfind("; "), s.rfind(" "))].rstrip(",;: ")
        s += "."
    if s.count("(") > s.count(")"): s = s[:s.rfind("(")].rstrip(" ,;:") + "."
    s = re.sub(r"^(Use (this skill |this )?when you need to |Use (this skill |this )?when )", "For when ", s)
    return s[0].upper() + s[1:] if s else s

REPO = "https://github.com/Jack-Attackz101/super-design-skills"
SITE = os.path.join(HERE, "..", "site")
AGENTS = [("claudecode-color", "Claude Code"), ("claude-color", "Claude"), ("grokbot", "Grok"),
          ("cursor", "Cursor"), ("codex-color", "Codex"), ("openai", "ChatGPT")]

def svg(name):
    s = open(os.path.join(SITE, "logos", name + ".svg")).read()
    s = re.sub(r'\s(height|width|style)="[^"]*"', "", s)
    s = re.sub(r"<title>.*?</title>", "", s)
    return s.replace("<svg", '<svg class="logo" aria-hidden="true" focusable="false"', 1)

def main():
    c = catalog.load()
    skills = []
    for i, k in enumerate(gen_docs.ORDER):
        t, about, uses, tries = gen_docs.ABOUT[k]
        groups = [{"g": g["g"], "items": [{"n": m["n"], "d": module_desc(k, m["n"]) or m["d"], "src": c[k]["sources"].get(m["n"], "")} for m in g["items"]]} for g in c[k]["groups"]]
        skills.append({"slug": k, "title": t, "about": about, "uses": uses, "tries": tries,
                       "lede": CARD[k], "how": HOW[k], "groups": groups,
                       "count": sum(len(g["items"]) for g in groups)})
    skills.append({"slug": "rea", "title": "REA", "external": "https://github.com/morluto/rea",
                   "lede": "Reverse engineer apps and pages, with evidence. Installed separately.",
                   "about": "", "uses": [], "tries": [], "groups": [], "count": 0})
    data = {"repo": REPO, "skills": skills,
            "agents": [{"name": n, "svg": svg(f)} for f, n in AGENTS],
            "urls": gen_docs.URLS}
    tpl = open(os.path.join(SITE, "template.html")).read()
    html = tpl.replace("/*DATA*/", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    html = html.replace("{{REPO}}", REPO)
    html = html.replace("{{LOGOS}}", "".join(f'<li title="{n}">{svg(f)}<span>{n}</span></li>' for f, n in AGENTS))
    open(os.path.join(SITE, "index.html"), "w").write(html)
    print("built site/index.html:", len(html) // 1024, "KB,", len(skills), "skills")

if __name__ == "__main__":
    main()
