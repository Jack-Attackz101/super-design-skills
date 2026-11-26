"""Build one upload-ready zip per skill in dist/, for claude.ai and the Claude desktop app
(Customize > Skills). Skills you add there also load in Claude Code sessions signed in to
that account, and in Claude Code on the web.

claude.ai rejects a skill with more than 200 files, so this script:
  1. drops videos, 3D models and images over 150 KB (demo assets; instructions and scripts stay), and
  2. if a skill is still over the limit, packs each module's files into modules/<name>/bundle.tar.gz,
     keeping its MODULE.md loose, and tells the agent in SKILL.md how to unpack a bundle when needed.

Run: python3 scripts/make_claude_ai_zips.py
"""
import os, shutil, tarfile, zipfile, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.join(HERE, "..", "skills")
DIST = os.path.join(HERE, "..", "dist")
LIMIT = 200
MEDIA = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif")
DROP = (".mp4", ".webm", ".mov", ".glb", ".gltf")
NOTE = ("\n**Packed module files.** To fit the claude.ai skill limit, each module keeps only its `MODULE.md` loose. "
        "Its other files (scripts, references, examples, assets) are in `bundle.tar.gz` in the same folder. "
        "When a module mentions a file you don't see, unpack that module's bundle into a temporary folder "
        "(`mkdir -p /tmp/skill-modules/<module> && tar -xzf <module folder>/bundle.tar.gz -C /tmp/skill-modules/<module>`) "
        "and read or run the files from there; paths in `MODULE.md` are relative to that folder.\n")
MARKER = "Paths inside a module are relative to that module's folder."

def count(d): return sum(len(f) for _, _, f in os.walk(d))

def slim(d):
    for dp, dn, fs in os.walk(d):
        dn[:] = [x for x in dn if x != "node_modules"]
        for f in fs:
            p = os.path.join(dp, f); low = f.lower()
            if low.endswith(DROP) or (low.endswith(MEDIA) and os.path.getsize(p) > 150_000) or f == ".super-design-skill":
                os.remove(p)
    for dp, dn, fs in os.walk(d, topdown=False):
        if not os.listdir(dp): os.rmdir(dp)

def pack(d):
    mods = os.path.join(d, "modules")
    for m in sorted(os.listdir(mods)):
        md = os.path.join(mods, m)
        rest = [os.path.relpath(os.path.join(dp, f), md) for dp, _, fs in os.walk(md) for f in fs
                if not (dp == md and f == "MODULE.md")]
        if not rest: continue
        with tarfile.open(os.path.join(md, "bundle.tar.gz"), "w:gz") as t:
            for r in sorted(rest): t.add(os.path.join(md, r), arcname=r)
        for e in os.listdir(md):
            if e not in ("MODULE.md", "bundle.tar.gz"):
                p = os.path.join(md, e); shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    sk = os.path.join(d, "SKILL.md"); s = open(sk).read()
    if MARKER in s: open(sk, "w").write(s.replace(MARKER, MARKER + "\n" + NOTE, 1))

def main():
    shutil.rmtree(DIST, ignore_errors=True); os.makedirs(DIST)
    with tempfile.TemporaryDirectory() as tmp:
        for name in sorted(os.listdir(SKILLS)):
            src = os.path.join(SKILLS, name)
            if not os.path.exists(os.path.join(src, "SKILL.md")): continue
            d = os.path.join(tmp, name); shutil.copytree(src, d, symlinks=False)
            slim(d)
            packed = count(d) > LIMIT and os.path.isdir(os.path.join(d, "modules"))
            if packed: pack(d)
            n = count(d)
            z = os.path.join(DIST, name + ".zip")
            with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
                for dp, _, fs in os.walk(d):
                    for f in fs:
                        p = os.path.join(dp, f); zf.write(p, os.path.relpath(p, tmp))
            flag = "  OVER LIMIT" if n > LIMIT else ""
            print(f"dist/{name}.zip  {os.path.getsize(z)/1e6:5.1f} MB  {n:3d} files{'  (modules packed)' if packed else ''}{flag}")

main()
