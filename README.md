# multi-agent-workspace

(Dutch)

Een kant-en-klare workspace met een team van gespecialiseerde AI-agents om mee te beginnen aan
het ontwikkelen van een softwareproduct. De omgeving is **compatibel met zowel Claude Code als
GitHub Copilot**.

## Aan de slag

| Tool | Handleiding | Configuratie |
|------|-------------|--------------|
| **Claude Code** (CLI/desktop/web/IDE) | [`CLAUDE_CODE.md`](CLAUDE_CODE.md) | `CLAUDE.md`, `.claude/` |
| **GitHub Copilot** (VS Code) | [`INSTRUCTIONS.md`](INSTRUCTIONS.md) | `.github/` |

- **Claude Code**: open deze map en start een sessie. `CLAUDE.md` wordt automatisch geladen.
  Begin met `/new-project`.
- **GitHub Copilot**: open de Chat-view in VS Code en gebruik `/new-project` of `@AgentNaam`.

## Het team

Orchestrator · Planner · Business Analyst · Architect · Backend · Frontend · UX Designer ·
Tester · DevOps · Legal · Stakeholder.

## Structuur in het kort

- `.claude/agents/` · `.github/agents/` — agent-definities (Claude Code / Copilot)
- `.claude/commands/` · `.github/prompts/` — herbruikbare workflows / slash-commando's
- `.github/instructions/` — codestandaarden, git-werkwijze, multi-agent-protocol
- `agents/` — geheugenbestanden, projectbeheer (plan, backlog, beslissingen), stakeholders
- `project/` — de daadwerkelijke deliverables (`src/`, `docs/`, `designs/`)

De Claude Code-definities in `.claude/` worden gegenereerd uit de Copilot-bronnen in `.github/`
met `python3 .claude/convert.py`. Houd beide in sync bij wijzigingen.
