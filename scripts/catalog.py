"""Read every skill's SKILL.md and SOURCES.md into one structure. Used by gen_docs.py."""
import os, re
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "skills")
def load():
    out = {}
    for name in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, name, "SKILL.md")
        if not os.path.exists(p): continue
        t = open(p).read()
        m = re.search(r"^description:\s*(.*)$", t, re.M)
        desc = m.group(1).strip().strip('"') if m else ""
        groups, cur = [], None
        sec = t.split("\n## Modules\n", 1)[1] if "\n## Modules\n" in t else ""
        for line in sec.splitlines():
            if line.startswith("### "): cur = {"g": line[4:].strip(), "items": []}; groups.append(cur)
            mm = re.match(r"\| `([^`]+)` \| (.*) \|$", line)
            if mm and cur is not None: cur["items"].append({"n": mm.group(1), "d": mm.group(2)})
        src = {}
        sp = os.path.join(ROOT, name, "SOURCES.md")
        if os.path.exists(sp):
            for line in open(sp):
                mm = re.match(r"\| ([^|]+) \| ([^|]+) \|$", line.strip())
                if mm and mm.group(1).strip() != "Module" and not mm.group(1).startswith("---"):
                    src[mm.group(1).strip()] = mm.group(2).strip()
        out[name] = {"desc": desc, "groups": groups, "sources": src}
    return out
