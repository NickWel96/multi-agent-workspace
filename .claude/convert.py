#!/usr/bin/env python3
"""Eenmalig conversiescript: Copilot-customizations -> Claude Code-customizations.
Behoudt de (tool-agnostische) persona-body en vertaalt de frontmatter."""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Copilot-tool -> Claude Code-tools
TOOLMAP = {
    "read":    ["Read"],
    "edit":    ["Edit", "Write"],
    "search":  ["Grep", "Glob"],
    "execute": ["Bash"],
    "agent":   ["Task"],
    "todo":    ["TodoWrite"],
    "fetch":   ["WebFetch", "WebSearch"],
}

def map_tools(cp_tools):
    out = []
    for t in cp_tools:
        for m in TOOLMAP.get(t.strip(), []):
            if m not in out:
                out.append(m)
    return out

def split_fm(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        raise ValueError("geen frontmatter")
    return m.group(1), m.group(2)

def parse_fm(fm):
    d = {}
    for line in fm.splitlines():
        m = re.match(r'^([A-Za-z0-9_-]+):\s*(.*)$', line)
        if not m:
            continue
        k, v = m.group(1), m.group(2).strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip('"').strip("'") for x in v[1:-1].split(",") if x.strip()]
        else:
            v = v.strip('"').strip("'")
        d[k] = v
    return d

def yamlstr(s):
    # quote als nodig
    return s.replace('"', '\\"')

# ---------- AGENTS ----------
agent_dir = ROOT / ".github" / "agents"
out_agents = ROOT / ".claude" / "agents"
for f in sorted(agent_dir.glob("*.agent.md")):
    fm, body = split_fm(f.read_text())
    meta = parse_fm(fm)
    name = f.name.replace(".agent.md", "")
    tools = map_tools(meta.get("tools", []))
    desc = meta.get("description", "")
    new_fm = [
        "---",
        f"name: {name}",
        f'description: "{yamlstr(desc)}"',
        f"tools: {', '.join(tools)}",
        "model: sonnet",
    ]
    if str(meta.get("user-invocable", "true")).lower() == "false":
        # in Claude Code zijn alle agents oproepbaar; markeer in body i.p.v. frontmatter
        pass
    new_fm.append("---")
    (out_agents / f"{name}.md").write_text("\n".join(new_fm) + "\n" + body.rstrip() + "\n")
    print("agent ->", name, tools)

# ---------- COMMANDS (prompts) ----------
prompt_dir = ROOT / ".github" / "prompts"
out_cmd = ROOT / ".claude" / "commands"
for f in sorted(prompt_dir.glob("*.prompt.md")):
    fm, body = split_fm(f.read_text())
    meta = parse_fm(fm)
    name = f.name.replace(".prompt.md", "")
    desc = meta.get("description", "")
    new_fm = ["---", f'description: "{yamlstr(desc)}"']
    if meta.get("argument-hint"):
        new_fm.append(f'argument-hint: "{yamlstr(meta["argument-hint"])}"')
    new_fm.append("model: sonnet")
    new_fm.append("---")
    (out_cmd / f"{name}.md").write_text("\n".join(new_fm) + "\n" + body.rstrip() + "\n")
    print("command ->", name)

print("klaar")
