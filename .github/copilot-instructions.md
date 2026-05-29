# Multi-Agent Development Team — Globale Instructies

Dit project maakt gebruik van een team van gespecialiseerde AI-agents. Elke agent heeft een eigen expertise, een eigen geheugenbestand en werkt samen met de andere teamleden.

> **Dual-tool compatibiliteit**: Deze workspace werkt met **GitHub Copilot** (`.github/`) én **Claude Code** (`.claude/` + `CLAUDE.md`). De `.github/`-bestanden zijn de bron; de `.claude/`-equivalenten worden hieruit gegenereerd met `python3 .claude/convert.py`. Wijzig je een agent of prompt, draai dan dat script (of werk beide bij) zodat de tools in sync blijven. Zie `CLAUDE_CODE.md` voor de Claude Code-handleiding.

## Projectstructuur

```
.github/agents/             → Agent-definitiebestanden (.agent.md)
.github/prompts/            → Herbruikbare prompt-workflows (.prompt.md)
.github/instructions/       → Codestandaarden en richtlijnen (.instructions.md)
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
3. **Consulteer experts**: Weet je iets niet? Delegeer aan de juiste specialistagent.
4. **Documenteer beslissingen**: Architectuurkeuzes horen in `agents/project/decisions.md`.
5. **Houd mijlpalen bij**: Status-updates gaan naar `agents/project/milestones.md`.
6. **Wees beknopt maar compleet**: Rapporteer duidelijk wat je hebt gedaan en wat er nog moet.
7. **Gebruik het backlog**: Nieuwe taken toevoegen aan `agents/project/backlog.md`.
8. **Werk altijd op een branch**: Implementatiecode gaat nooit direct op `main` of `develop`. Maak een `feature/`, `fix/` of `chore/`-branch aan, open een PR en vraag review aan.
9. **PR's zijn scoped**: één logisch geheel per PR. Splits op als dit de review verbetert.
10. **Deliverables in `project/`**: Alle projectopbrengsten worden geplaatst in de `project/`-map:
    - Broncode → `project/src/`
    - Verslagen, rapporten, presentaties → `project/docs/`
    - UI/UX designs, mockups, wireframes → `project/designs/`
11. **Houd beide AI-modellen in sync** (zie sectie hieronder): wijzig je een model-specifiek
    bestand, pas dan in dezelfde taak het equivalent voor het andere model aan. Harde regel.

## ⚠️ Synchronisatie tussen Copilot en Claude Code (VERPLICHT)

Deze workspace ondersteunt **twee AI-tools tegelijk**: GitHub Copilot (`.github/`) en Claude
Code (`.claude/` + `CLAUDE.md`). Beide moeten **altijd** dezelfde agents, commando's en regels
beschrijven.

> **Harde regel**: Wijzig of voeg je een model-specifiek bestand toe, dan pas je in
> **dezelfde taak** ook de tegenhanger voor het andere model aan. Lever nooit een wijziging op
> die maar één van beide tools bijwerkt. Meld expliciet dat beide kanten zijn bijgewerkt.

| Onderwerp | GitHub Copilot | Claude Code |
|-----------|----------------|-------------|
| Agent-definities | `.github/agents/<naam>.agent.md` | `.claude/agents/<naam>.md` |
| Prompts / slash-commando's | `.github/prompts/<naam>.prompt.md` | `.claude/commands/<naam>.md` |
| Globale instructies | `.github/copilot-instructions.md` | `CLAUDE.md` |
| Codestandaarden / git / workflow | `.github/instructions/*.instructions.md` (gedeeld) | idem |

**Werkwijze bij een wijziging:**
1. De **bron** is `.github/` (Copilot-formaat). Wijzig daar de agent of prompt.
2. Draai `python3 .claude/convert.py` om `.claude/agents/` en `.claude/commands/` te
   hergenereren (vertaalt frontmatter/tools automatisch, body blijft identiek).
3. Wijzig je deze instructies handmatig, breng dezelfde wijziging aan in `CLAUDE.md` — die
   wordt níét door het script gesynchroniseerd.
4. Commit beide kanten samen.

## Taakverdeling — Wie doet wat?

| Agent | Bestand | Expertise |
|-------|---------|-----------|
| Orchestrator | `orchestrator.agent.md` | Taakverdeling, coördinatie, voortgang |
| Planner | `planner.agent.md` | Projectplanning, mijlpalen, risico's |
| Business Analyst | `business-analyst.agent.md` | Stakeholderinterviews, requirements, user stories |
| Architect | `architect.agent.md` | Systeemontwerp, technische beslissingen |
| Backend | `backend.agent.md` | API's, database, serverlogica |
| Frontend | `frontend.agent.md` | UI/UX, componenten, state management |
| UX Designer | `ux-designer.agent.md` | Wireframes, mockups, design system, Google Stitch, handoff |
| Tester | `tester.agent.md` | Testplannen, unit/integratie/e2e-tests |
| DevOps | `devops.agent.md` | CI/CD, infrastructuur, deployment |
| Legal | `legal.agent.md` | Nederlandse & Europese wetgeving, compliance-audits, juridisch advies |

## Interactieprotocol

Wanneer een agent werk delegeert:
- Geef de ontvangende agent expliciete context over de taak
- Vermeld het relevante deel van het projectplan
- Verwacht een statusrapport terug

Wanneer een agent een vraag stelt aan een expert:
- Formuleer de vraag concreet en beknopt
- Geef aan welke beslissing ervan afhangt
- Wacht op bevestiging voor je verdergaat
