# Multi-Agent AI Ontwikkelomgeving — Claude Code-handleiding

Deze workspace draait een team van gespecialiseerde AI-agents. Deze handleiding beschrijft het
gebruik met **Claude Code** (CLI, desktop, web of IDE-extensie). Gebruik je liever GitHub
Copilot in VS Code? Zie dan `INSTRUCTIONS.md`.

> De agents, commando's en regels zijn identiek voor beide tools — alleen de manier van
> aanroepen verschilt. Claude Code laadt automatisch `CLAUDE.md` als projectgeheugen.

---

## 1. Hoe het werkt in Claude Code

In Claude Code is er één **hoofdsessie** (de assistant waarmee je praat). Die fungeert als
**Orchestrator**: hij leest `CLAUDE.md`, coördineert het werk en schakelt **subagents** in via
het Task-tool wanneer specialistische expertise nodig is.

```
Jij  ──>  Hoofdsessie (Orchestrator)  ──Task──>  Subagent (bv. backend)
                  ▲                                      │
                  └──────────── rapport ◄────────────────┘
```

- **Subagents** = de specialisten in `.claude/agents/*.md`. Elke subagent draait geïsoleerd met
  zijn eigen tools en geeft een rapport terug.
- **Subagents kunnen zelf geen subagents starten.** Delegatieketens lopen dus altijd via de
  hoofdsessie.
- **Slash-commando's** = workflows in `.claude/commands/*.md`, uitgevoerd in de hoofdsessie.

---

## 2. Het team

| Agent | Inschakelen | Expertise |
|-------|-------------|-----------|
| **Orchestrator** | meestal de hoofdsessie zelf | Coördinatie, taakverdeling, voortgang |
| **Planner** | "gebruik de planner-agent…" | Projectplan, fasen, mijlpalen |
| **Business Analyst** | `business-analyst` | Stakeholderinterviews, requirements, user stories |
| **Architect** | `architect` | Technische architectuur, ADR's, API-design |
| **Backend** | `backend` | API's, database, serverlogica |
| **Frontend** | `frontend` | UI-componenten, pagina's, state |
| **UX Designer** | `ux-designer` | Wireframes, mockups, design system, Google Stitch |
| **Tester** | `tester` | Tests, kwaliteitsreviews, bugs |
| **DevOps** | `devops` | CI/CD, Docker, infrastructuur |
| **Legal** | `legal` | NL & EU-wetgeving, compliance, juridisch advies |
| **Stakeholder** | `stakeholder` | Speelt een stakeholder-persona |

### Een agent inschakelen

Je hoeft geen `@`-notatie te gebruiken zoals in Copilot. Beschrijf gewoon wat je wilt, of
benoem de agent expliciet:

```
Laat de architect een datamodel ontwerpen voor een bestelsysteem.
Gebruik de backend-agent om POST /api/orders te implementeren volgens ADR-002.
```

Claude Code kiest dan automatisch de juiste subagent op basis van zijn `description`, of jij
stuurt expliciet bij.

---

## 3. Slash-commando's

| Commando | Doel |
|----------|------|
| `/new-project` | Nieuw project opstarten |
| `/standup` | Dagelijkse voortgangsrapportage |
| `/milestone-review` | Een mijlpaal reviewen |
| `/add-agent` | Een nieuwe specialistagent toevoegen |
| `/add-stakeholder` | Een nieuw stakeholderbedrijf definiëren |
| `/interview-stakeholder` | BA stuurt naar één of meer stakeholders |
| `/talk-to-stakeholder` | Zelf met een stakeholder-persona praten |

Voorbeeld:

```
/new-project
> Ik wil een webapp bouwen voor ritplanning bij transportbedrijven…
```

---

## 4. Aan de slag

1. **Start een sessie** in deze map. Claude Code laadt automatisch `CLAUDE.md`.
2. **Start een project**: `/new-project` en beschrijf je idee.
3. **Laat het team werken**: de Planner schrijft `agents/project/plan.md`, de Architect vult
   `agents/project/decisions.md`, de Orchestrator vult de backlog en richt `project/` in.
4. **Ontwikkel**: "Gebruik de backend-agent om de eerste endpoint te bouwen volgens het plan."
5. **Bewaak voortgang**: `/standup` en `/milestone-review`.

---

## 5. Agents en commando's aanpassen

De **bron** van waarheid zijn de Copilot-bestanden in `.github/agents/` en `.github/prompts/`.
De Claude Code-versies in `.claude/` worden daaruit gegenereerd.

- **Bestaande agent aanpassen**: wijzig `.github/agents/<naam>.agent.md` én
  `.claude/agents/<naam>.md` — of wijzig de Copilot-bron en draai daarna:
  ```
  python3 .claude/convert.py
  ```
  Dit hergenereert alle `.claude/agents/*.md` en `.claude/commands/*.md`.
- **Nieuwe agent**: gebruik `/add-agent`. Maak het bestand in beide formaten aan (of draai het
  convert-script). Vergeet niet het geheugenbestand in `agents/memory/<naam>.md`.

### Tool-mapping (Copilot → Claude Code)

| Copilot | Claude Code |
|---------|-------------|
| `read` | `Read` |
| `edit` | `Edit`, `Write` |
| `search` | `Grep`, `Glob` |
| `execute` | `Bash` |
| `agent` | `Task` |
| `todo` | `TodoWrite` |
| `fetch` | `WebFetch`, `WebSearch` |

---

## 6. Permissies & veiligheid

`.claude/settings.json` staat veelvoorkomende, veilige acties automatisch toe (lezen, zoeken,
bestanden bewerken, niet-destructieve git) zodat het team vlot agentic kan werken. Het blokkeert
push naar `main`/`develop`, force-push, `git reset --hard` en `rm -rf`. Implementatiecode hoort
altijd op een `feature/`-, `fix/`- of `chore/`-branch met een PR.

---

## 7. Projectbestanden

| Bestand/Map | Inhoud | Beheerd door |
|-------------|--------|-------------|
| `agents/project/plan.md` | Projectplan + `legal_agent_enabled` | Planner |
| `agents/project/milestones.md` | Mijlpalen met acceptatiecriteria | Orchestrator + Planner |
| `agents/project/decisions.md` | ADR's + juridische LAR's | Architect + Legal |
| `agents/project/backlog.md` | Openstaande taken en bugs | Orchestrator |
| `project/src/` | Broncode | Backend / Frontend / DevOps |
| `project/docs/` | Verslagen, rapporten, presentaties | Alle agents |
| `project/designs/` | UI/UX designs en mockups | UX Designer / Frontend |

---

## 8. Problemen oplossen

- **Een subagent wordt niet gekozen** → benoem hem expliciet ("gebruik de tester-agent…") of
  controleer de `description` in `.claude/agents/<naam>.md`.
- **Slash-commando ontbreekt** → het bestand moet in `.claude/commands/` staan en op `.md`
  eindigen; herstart de sessie na toevoegen.
- **`.claude/` loopt uit de pas met `.github/`** → draai `python3 .claude/convert.py`.
- **Te veel permissie-prompts** → voeg de actie toe aan de `allow`-lijst in
  `.claude/settings.json` (of gebruik het `/fewer-permission-prompts`-hulpmiddel).

---

*Omgeving compatibel met zowel Claude Code als GitHub Copilot. Documentatie:
[code.claude.com/docs](https://code.claude.com/docs) — [code.visualstudio.com/docs/copilot](https://code.visualstudio.com/docs/copilot)*
