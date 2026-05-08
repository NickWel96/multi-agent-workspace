# Multi-Agent Development Team — Globale Instructies

Dit project maakt gebruik van een team van gespecialiseerde AI-agents. Elke agent heeft een eigen expertise, een eigen geheugenbestand en werkt samen met de andere teamleden.

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

## Taakverdeling — Wie doet wat?

| Agent | Bestand | Expertise |
|-------|---------|-----------|
| Orchestrator | `orchestrator.agent.md` | Taakverdeling, coördinatie, voortgang |
| Planner | `planner.agent.md` | Projectplanning, mijlpalen, risico's |
| Business Analyst | `business-analyst.agent.md` | Stakeholderinterviews, requirements, user stories |
| Architect | `architect.agent.md` | Systeemontwerp, technische beslissingen |
| Backend | `backend.agent.md` | API's, database, serverlogica |
| Frontend | `frontend.agent.md` | UI/UX, componenten, state management |
| Tester | `tester.agent.md` | Testplannen, unit/integratie/e2e-tests |
| DevOps | `devops.agent.md` | CI/CD, infrastructuur, deployment |

## Interactieprotocol

Wanneer een agent werk delegeert:
- Geef de ontvangende agent expliciete context over de taak
- Vermeld het relevante deel van het projectplan
- Verwacht een statusrapport terug

Wanneer een agent een vraag stelt aan een expert:
- Formuleer de vraag concreet en beknopt
- Geef aan welke beslissing ervan afhangt
- Wacht op bevestiging voor je verdergaat
