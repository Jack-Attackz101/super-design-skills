#!/usr/bin/env bash
# Install the Super Design skills for your coding agents.
#
#   ./install.sh                  Claude Code (~/.claude/skills) plus agents that read ~/.agents/skills
#   ./install.sh --claude         Claude Code only
#   ./install.sh --universal      only ~/.agents/skills (Codex, Cursor, Gemini CLI, OpenCode and others)
#   ./install.sh --copy           copy instead of symlink (use when this folder won't stay put)
#   ./install.sh --awwwards       also register the optional awwwards MCP server for Claude Code
#   ./install.sh --uninstall      remove the skills this script installed
#
# Safe to run again. A same-named skill that isn't ours is moved to
# <skills dir>/.super-design-backup-<timestamp>/ instead of being overwritten.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGETS=(); MODE=link; AWW=0; UNINSTALL=0
for a in "$@"; do
  case "$a" in
    --claude) TARGETS+=("$HOME/.claude/skills") ;;
    --universal) TARGETS+=("$HOME/.agents/skills") ;;
    --copy) MODE=copy ;;
    --awwwards) AWW=1 ;;
    --uninstall) UNINSTALL=1 ;;
    -h|--help) sed -n '2,13p' "$0"; exit 0 ;;
    *) echo "Unknown option: $a (try --help)" >&2; exit 2 ;;
  esac
done
[ ${#TARGETS[@]} -eq 0 ] && TARGETS=("$HOME/.claude/skills" "$HOME/.agents/skills")

STAMP="$(date +%Y%m%d-%H%M%S)"
names=()
for src in "$REPO"/skills/*/; do [ -f "$src/SKILL.md" ] && names+=("$(basename "$src")"); done

for DEST in "${TARGETS[@]}"; do
  mkdir -p "$DEST"
  for name in "${names[@]}"; do
    src="$REPO/skills/$name"; target="$DEST/$name"
    ours=0
    if [ -L "$target" ] && [ "$(readlink "$target")" = "$src" ]; then ours=1; fi
    if [ -f "$target/.super-design-skill" ]; then ours=1; fi
    if [ "$UNINSTALL" = 1 ]; then
      if [ "$ours" = 1 ]; then rm -rf "$target"; fi
      continue
    fi
    if [ -e "$target" ] || [ -L "$target" ]; then
      if [ "$ours" = 1 ]; then rm -rf "$target"
      else
        mkdir -p "$DEST/.super-design-backup-$STAMP"
        mv "$target" "$DEST/.super-design-backup-$STAMP/$name"
        echo "Moved your existing $name to $DEST/.super-design-backup-$STAMP/"
      fi
    fi
    if [ "$MODE" = link ]; then ln -s "$src" "$target"
    else cp -R "$src" "$target"; echo "installed by super-design-skills $STAMP" > "$target/.super-design-skill"; fi
  done
  if [ "$UNINSTALL" = 1 ]; then echo "Removed the skills from $DEST"; else echo "Installed ${#names[@]} skills into $DEST ($MODE)"; fi
done
[ "$UNINSTALL" = 1 ] && exit 0

if [ "$AWW" = 1 ]; then
  if command -v claude >/dev/null 2>&1; then
    if (cd "$HOME" && claude mcp get awwwards >/dev/null 2>&1); then echo "awwwards MCP server already registered"
    elif (cd "$HOME" && claude mcp add --scope user awwwards -- npx -y awwwards-mcp >/dev/null 2>&1); then echo "Registered the awwwards MCP server"
    else echo "Could not register the awwwards MCP server (skipped)"; fi
  else echo "Claude Code CLI not found: skipped the awwwards MCP server"; fi
fi

cat <<'MSG'

Done. Start a new agent session to load the skills:
  /design  /landing-page  /prototype  /scroll-site  /animate  /image
  /brand   /review        /demo       /marketing    /interview  /agentation
What each one does: SKILLS.md
Also worth getting (not included): REA, Reverse Engineer Anything: https://github.com/morluto/rea
MSG
