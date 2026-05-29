#!/usr/bin/env python3
"""PostToolUse-hook: herinnert Claude Code eraan de tegenhanger voor het andere AI-model
(GitHub Copilot) bij te werken zodra een model-specifiek bestand is bewerkt.

Niet-blokkerend: injecteert alleen extra context via additionalContext."""
import json, sys, re

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

path = (data.get("tool_input") or {}).get("file_path", "") or ""
if not path:
    sys.exit(0)

# Normaliseer naar repo-relatief pad-fragment
p = path.replace("\\", "/")

reminder = None
if "/.claude/agents/" in p or p.endswith(".agent.md") or "/.github/agents/" in p:
    reminder = ("Agent-definitie gewijzigd. Houd beide modellen in sync: werk zowel "
                "`.github/agents/<naam>.agent.md` (Copilot-bron) als `.claude/agents/<naam>.md` "
                "(Claude Code) bij — draai `python3 .claude/convert.py` om te hergenereren.")
elif "/.claude/commands/" in p or p.endswith(".prompt.md") or "/.github/prompts/" in p:
    reminder = ("Prompt/slash-commando gewijzigd. Werk zowel `.github/prompts/<naam>.prompt.md` "
                "(bron) als `.claude/commands/<naam>.md` bij — draai `python3 .claude/convert.py`.")
elif re.search(r"(^|/)CLAUDE\.md$", p):
    reminder = ("`CLAUDE.md` gewijzigd. Breng dezelfde regelwijziging aan in "
                "`.github/copilot-instructions.md` zodat Copilot en Claude Code gelijk blijven.")
elif "copilot-instructions.md" in p:
    reminder = ("`.github/copilot-instructions.md` gewijzigd. Breng dezelfde regelwijziging aan "
                "in `CLAUDE.md` zodat Claude Code en Copilot gelijk blijven.")

if reminder:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": "⚠️ Sync-regel: " + reminder,
        }
    }))

sys.exit(0)
