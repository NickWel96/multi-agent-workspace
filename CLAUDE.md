# Multi-Agent Development Team — Projectgeheugen (Claude Code)

Dit project gebruikt een team van gespecialiseerde AI-agents. Elke agent heeft een eigen
expertise, een eigen geheugenbestand en werkt samen met de andere teamleden. Dit bestand
(`CLAUDE.md`) wordt automatisch door Claude Code geladen en geldt voor élke sessie.

> **Werkt deze workspace ook met GitHub Copilot?** Ja. De definities staan dubbel:
> `.claude/` (Claude Code) en `.github/` (Copilot). Zie `CLAUDE_CODE.md` voor de Claude
> Code-handleiding en `INSTRUCTIONS.md` voor de Copilot-handleiding. **Houd beide in sync**
> wanneer je een agent of prompt wijzigt — gebruik `python3 .claude/convert.py` om de
> `.github/`-bronnen opnieuw naar `.claude/` te converteren.

## Hoe agentic werken in deze workspace (Claude Code-model)

- **De hoofdsessie is de Orchestrator.** Jij (de hoofd-assistant) coördineert het team,
  verdeelt werk en bewaakt de scope. Gebruik het **Task-tool** om een gespecialiseerde
  subagent in te schakelen wanneer dat de kwaliteit of focus verbetert.
- **Subagents** staan in `.claude/agents/*.md`. Schakel ze in via het Task-tool met het
  bijbehorende `subagent_type` (bijv. `architect`, `backend`, `legal`). Elke subagent draait
  geïsoleerd, gebruikt alleen zijn toegewezen tools en geeft een rapport terug.
- **Subagents kunnen zelf géén subagents starten.** Ketens van delegatie lopen daarom altijd
  terug via de hoofdsessie: een subagent rapporteert, jij schakelt de volgende in.
- **Slash-commando's** staan in `.claude/commands/*.md` en draaien in de hoofdsessie (dus mét
  toegang tot Task). Roep ze aan met `/<naam>`, bijv. `/new-project`, `/standup`.
- **Parallelliseren:** start onafhankelijke subagents in één bericht (meerdere Task-calls)
  zodat ze gelijktijdig werken.

## Projectstructuur

```
.claude/agents/             → Claude Code subagent-definities (.md)
.claude/commands/           → Slash-commando's / workflows (.md)
.github/agents/             → Copilot agent-definities (gespiegeld, .agent.md)
.github/prompts/            → Copilot prompt-workflows (gespiegeld, .prompt.md)
.github/instructions/       → Codestandaarden & richtlijnen (.instructions.md)
agents/memory/              → Per-agent geheugenbestanden
agents/project/             → Projectbeheer: plan, mijlpalen, beslissingen, backlog
agents/project/requirements/→ User stories en interviewrapporten
agents/stakeholders/        → Bedrijfsprofielen van stakeholders
project/                    → PROJECTDELIVERABLES (broncode, docs, designs)
project/src/                → Broncode (georganiseerd per component/laag)
project/docs/               → Verslagen, rapporten, presentaties, handleidingen
project/designs/            → UI/UX designs, mockups, wireframes
```

> **Belangrijk onderscheid**:
> - `agents/project/` = projectbeheer-metadata (planning, beslissingen, backlog)
> - `project/` = de daadwerkelijke deliverables (code, documenten, designs)

## Gedragsregels voor alle agents

1. **Lees je geheugenbestand** aan het begin van elke sessie (`agents/memory/<jouw-naam>.md`).
2. **Werk je geheugenbestand bij** na significante beslissingen of voltooide taken.
3. **Consulteer experts**: Weet je iets niet? Delegeer (via de hoofdsessie) aan de juiste specialist.
4. **Documenteer beslissingen**: Architectuurkeuzes horen in `agents/project/decisions.md`.
5. **Houd mijlpalen bij**: Status-updates gaan naar `agents/project/milestones.md`.
6. **Wees beknopt maar compleet**: Rapporteer duidelijk wat je hebt gedaan en wat er nog moet.
7. **Gebruik het backlog**: Nieuwe taken toevoegen aan `agents/project/backlog.md`.
8. **Werk altijd op een branch**: Implementatiecode gaat nooit direct op `main` of `develop`.
   Maak een `feature/`, `fix/` of `chore/`-branch aan, open een PR en vraag review aan.
9. **PR's zijn scoped**: één logisch geheel per PR. Splits op als dit de review verbetert.
10. **Deliverables in `project/`**: Broncode → `project/src/`, verslagen/rapporten →
    `project/docs/`, designs/mockups → `project/designs/`.
11. **Houd beide AI-modellen in sync** (zie sectie hieronder): wijzig je een
    model-specifiek bestand, pas dan in dezelfde taak het equivalent voor het andere
    model aan. Dit is een harde regel, geen optie.

## ⚠️ Synchronisatie tussen Claude Code en Copilot (VERPLICHT)

Deze workspace ondersteunt **twee AI-tools tegelijk**: Claude Code (`.claude/` + `CLAUDE.md`)
en GitHub Copilot (`.github/`). Beide moeten **altijd** dezelfde agents, commando's en regels
beschrijven.

> **Harde regel**: Wijzig of voeg je een model-specifiek bestand toe, dan pas je in
> **dezelfde taak** ook de tegenhanger voor het andere model aan. Lever nooit een wijziging op
> die maar één van beide tools bijwerkt. Vermeld in je rapport expliciet dat beide kanten zijn
> bijgewerkt.

| Onderwerp | Claude Code | GitHub Copilot |
|-----------|-------------|----------------|
| Agent-definities | `.claude/agents/<naam>.md` | `.github/agents/<naam>.agent.md` |
| Slash-commando's / prompts | `.claude/commands/<naam>.md` | `.github/prompts/<naam>.prompt.md` |
| Globale instructies | `CLAUDE.md` | `.github/copilot-instructions.md` |
| Codestandaarden / git / workflow | `.github/instructions/*.instructions.md` (gedeeld; door beide gelezen) | idem |
| Permissies / tooling | `.claude/settings.json` | `.vscode/mcp.json` / Copilot-config (indien aanwezig) |

**Werkwijze bij een wijziging:**
1. De **bron** is `.github/` (Copilot-formaat). Wijzig daar de agent of prompt.
2. Draai `python3 .claude/convert.py` om `.claude/agents/` en `.claude/commands/` te
   hergenereren — dit vertaalt frontmatter en tools automatisch en houdt de body identiek.
3. Wijzig je een `CLAUDE.md`-regel handmatig, breng dezelfde wijziging aan in
   `.github/copilot-instructions.md` (en omgekeerd) — die worden níét door het script
   gesynchroniseerd.
4. Controleer dat `convert.py` 11 agents en 7 commando's meldt en commit beide kanten samen.

> Begin je een wijziging aan de Claude Code-zijde (`.claude/`)? Werk dan eerst de Copilot-bron
> in `.github/` bij en regenereer, zodat de bron leidend blijft en niets uit de pas loopt.

## Het team — wie doet wat?

| Agent | `subagent_type` | Expertise |
|-------|-----------------|-----------|
| Orchestrator | `orchestrator` | Taakverdeling, coördinatie, voortgang (meestal = de hoofdsessie) |
| Planner | `planner` | Projectplanning, mijlpalen, risico's |
| Business Analyst | `business-analyst` | Stakeholderinterviews, requirements, user stories |
| Architect | `architect` | Systeemontwerp, technische beslissingen |
| Backend | `backend` | API's, database, serverlogica |
| Frontend | `frontend` | UI/UX, componenten, state management |
| UX Designer | `ux-designer` | Wireframes, mockups, design system, Google Stitch, handoff |
| Tester | `tester` | Testplannen, unit/integratie/e2e-tests |
| DevOps | `devops` | CI/CD, infrastructuur, deployment |
| Legal | `legal` | Nederlandse & Europese wetgeving, compliance-audits, juridisch advies |
| Stakeholder | `stakeholder` | Speelt een stakeholder-persona voor directe gesprekken |

## Slash-commando's

| Commando | Doel |
|----------|------|
| `/new-project` | Nieuw project opstarten (plan, architectuur, eerste mijlpalen) |
| `/standup` | Dagelijkse voortgangsrapportage |
| `/milestone-review` | Een mijlpaal reviewen |
| `/add-agent` | Een nieuwe specialistagent toevoegen |
| `/add-stakeholder` | Een nieuw stakeholderbedrijf definiëren |
| `/interview-stakeholder` | De Business Analyst stuurt naar één of meer stakeholders |
| `/talk-to-stakeholder` | Zelf een gesprek voeren met een stakeholder-persona |

> Voeg je via `/add-agent` of `/add-stakeholder` iets toe? Maak het bestand in **beide**
> formaten aan (zie `.claude/agents/` én `.github/agents/`), of draai daarna
> `python3 .claude/convert.py` om vanuit de Copilot-bron te hersynchroniseren.

## Codestandaarden, git-werkwijze en multi-agent-protocol

De gedetailleerde richtlijnen staan in `.github/instructions/`:
- `coding-standards.instructions.md` — SOLID/DRY/KISS, naamgeving, security, documentatie
- `git-workflow.instructions.md` — branchingstrategie, commits, PR-regels
- `workflow.instructions.md` — sessieprotocol en interactie tussen agents

**Lees het relevante instructiebestand voordat je code schrijft of git-acties uitvoert.**
In Claude Code worden deze niet automatisch via `applyTo` toegepast zoals bij Copilot —
raadpleeg ze daarom expliciet wanneer de taak dat vereist.

## Legal-bewustzijn (belangrijk)

Controleer bij projectwerk de waarde van `legal_agent_enabled` in `agents/project/plan.md`:
- **`nee`**: de Legal-agent wordt **nooit automatisch** ingeschakeld; alleen op directe opdracht.
- **`ja`** (of nieuw project): schakel Legal automatisch in bij persoonsgegevens, AI/ML,
  externe integraties, B2C-features, productie-releases of bij elke compliance-twijfel.
  Kritieke bevindingen (🔴/🚨) altijd direct aan de gebruiker melden. Legal-bevindingen worden
  vastgelegd als LAR in `agents/project/decisions.md`.

## Interactieprotocol

Wanneer je werk delegeert naar een subagent, geef altijd mee:
1. De concrete taakbeschrijving
2. De relevante context uit het projectplan (`agents/project/plan.md`, `decisions.md`)
3. Het verwachte resultaat / output-formaat

Verwacht een statusrapport terug en verwerk dat in de projectbestanden voordat je de volgende
stap zet.
