# Multi-Agent AI Ontwikkelomgeving — Gebruikersinstructies

Welkom bij jouw persoonlijke AI-ontwikkelteam. Deze omgeving maakt gebruik van **GitHub Copilot** in VS Code met een team van gespecialiseerde agents die samen aan jouw project werken.

---

## Inhoudsopgave

1. [Bestandsstructuur](#1-bestandsstructuur)
2. [Het team: de agents](#2-het-team-de-agents)
3. [Aan de slag: nieuw project starten](#3-aan-de-slag-nieuw-project-starten)
4. [Dagelijks gebruik](#4-dagelijks-gebruik)
5. [Stakeholders beheren en interviewen](#5-stakeholders-beheren-en-interviewen)
6. [Agents aanpassen of toevoegen](#6-agents-aanpassen-of-toevoegen)
7. [Projectvoortgang bewaken](#7-projectvoortgang-bewaken)
8. [GitHub Copilot features overzicht](#8-github-copilot-features-overzicht)
9. [Tips & tricks](#9-tips--tricks)
10. [Problemen oplossen](#10-problemen-oplossen)

---

## 1. Bestandsstructuur

```
.github/
  copilot-instructions.md          ← Globale regels voor alle agents
  agents/
    orchestrator.agent.md
    planner.agent.md
    business-analyst.agent.md      ← Requirements & stakeholderinterviews
    architect.agent.md
    backend.agent.md
    frontend.agent.md
    ux-designer.agent.md           ← Wireframes, mockups, design system, Google Stitch
    tester.agent.md
    devops.agent.md
    stakeholder.agent.md           ← Persona-agent voor directe stakeholdergesprekken
  prompts/
    new-project.prompt.md
    milestone-review.prompt.md
    add-agent.prompt.md
    standup.prompt.md
    add-stakeholder.prompt.md      ← Nieuw stakeholderbedrijf definiëren
    interview-stakeholder.prompt.md← Stakeholderinterview uitvoeren
  instructions/
    coding-standards.instructions.md
    workflow.instructions.md
    git-workflow.instructions.md        ← Branchingstrategie, commits, PR-regels
agents/
  memory/                          ← Per-agent geheugenbestanden
  project/
    plan.md
    milestones.md
    decisions.md
    backlog.md
    requirements/                  ← User stories & interviewrapporten
      user-stories.md
      consolidation.md
  stakeholders/                    ← Bedrijfsprofielen
    _template.md                   ← Sjabloon voor nieuw bedrijf
project/                           ← PROJECTDELIVERABLES (aangemaakt bij nieuw project)
  src/                             ← Broncode (backend, frontend, infra)
  docs/                            ← Verslagen, rapporten, presentaties, handleidingen
  designs/                         ← UI/UX designs, mockups, wireframes
  README.md                        ← Projectoverzicht
INSTRUCTIONS.md                    ← Dit bestand
```

> **Belangrijk**: `agents/project/` bevat **beheerbestanden** (planning, beslissingen, backlog).  
> `project/` bevat de **daadwerkelijke deliverables** die aan de opdrachtgever worden opgeleverd.

---

## 2. Het team: de agents

| Agent | Activeren met | Expertise |
|-------|--------------|-----------|
| **Orchestrator** | `@Orchestrator` | Coördinatie, taakverdeling, voortgang |
| **Planner** | `@Planner` | Projectplan, fasen, mijlpalen |
| **Business Analyst** | `@Business Analyst` | Stakeholderinterviews, requirements, user stories |
| **Architect** | `@Architect` | Technische architectuur, ADR's, API-design |
| **Backend** | `@Backend` | API's, database, serverlogica |
| **Frontend** | `@Frontend` | UI-componenten, pagina's, state management |
| **UX Designer** | `@UX Designer` | Wireframes, mockups, design system, Google Stitch, handoff |
| **Tester** | `@Tester` | Tests schrijven, kwaliteitsreviews, bugs |
| **DevOps** | `@DevOps` | CI/CD, Docker, infrastructuur |
| **Stakeholder** | `@Stakeholder` | Speelt een stakeholder-persona — voor directe gesprekken |

### Een agent activeren

Open de **Chat-view** in VS Code (`Ctrl+Alt+I`) en selecteer een agent via het agent-dropdown bovenaan, of typ `@<Agentnaam>` in de chatinvoer.

---

## 3. Aan de slag: nieuw project starten

### Stap 1: Open Chat
Druk op `Ctrl+Alt+I` om de Copilot Chat te openen.

### Stap 2: Start het new-project prompt
Typ in de chat:
```
/new-project
```
Of via het slash-commando menu (typ `/` en kies `Nieuw Project Starten`).

### Stap 3: Beantwoord de vragen van de Planner
De agent zal vragen stellen over:
- De projectnaam en het doel
- De gewenste functionaliteiten
- Technologiestack-voorkeuren
- Eventuele beperkingen

### Stap 4: Laat het team werken
Na de initiële input:
1. De **Planner** schrijft het projectplan naar `agents/project/plan.md`
2. De **Architect** definieert de technische architectuur in `agents/project/decisions.md`
3. De **Orchestrator** vult de backlog met eerste taken in `agents/project/backlog.md`
4. De **Orchestrator** richt de `project/`-map in als deliverables-werkruimte

### Stap 5: Begin met ontwikkelen
Activeer de relevante agent voor de eerste taak:
```
@Backend Implementeer de eerste API-endpoint zoals beschreven in agents/project/plan.md
```

---

## 4. Dagelijks gebruik

### Voortgangsrapportage ophalen
```
/standup
```
Je krijgt een overzicht van wat gedaan is, de huidige blokkades en de aanbevolen volgende stap.

### Een specifieke agent direct aanspreken
```
@Architect Welke technologie zou het beste passen voor real-time notificaties?

@Backend Implementeer de user-authenticatie op basis van ADR-002 in decisions.md

@Tester Schrijf integratietests voor het /api/users endpoint

@DevOps Maak een GitHub Actions pipeline voor automatisch deployen naar staging
```

### De Orchestrator alles laten coördineren
```
@Orchestrator We zijn klaar met fase 1. Wat is de volgende prioriteit?
```

### Werk delegeren via de Orchestrator
```
@Orchestrator Zorg dat de login-feature volledig is: backend, frontend én tests
```
De Orchestrator verdeelt dit automatisch over Backend, Frontend en Tester.

---

## 5. Stakeholders beheren en interviewen

### Een nieuw stakeholderbedrijf definiëren

Gebruik het prompt:
```
/add-stakeholder
```
Je wordt begeleid bij het invullen van:
- **Bedrijfsprofiel** — naam, sector, grootte, werkwijze, pijnpunten, systemen
- **Medewerkers** — naam, functie, expertise, communicatiestijl, prioriteiten, beslissingsbevoegdheid

Het resultaat is een bestand `agents/stakeholders/<bedrijfsnaam>.md`. Hoe gedetailleerder dit profiel, hoe realistischer de Business Analyst de gesprekken simuleert.

**Of handmatig**: Kopieer `agents/stakeholders/_template.md` en vul het in.

### Een stakeholderinterview uitvoeren

```
/interview-stakeholder
```

De Business Analyst:
1. Leest het bedrijfsprofiel
2. Selecteert zelf de relevante gesprekspartners op basis van het doel
3. Voert gesimuleerde interviews uit — realistisch, gebaseerd op de persona's
4. Schrijft een interviewrapport naar `agents/project/requirements/`
5. Vertaalt de bevindingen naar user stories in `agents/project/requirements/user-stories.md`

**Voorbeeld**:
```
/interview-stakeholder
> Bedrijf: Transportbedrijf De Vries (agents/stakeholders/de-vries.md)
> Doel: Inventariseer hoe ze nu ritten plannen en wat ze van een digitale oplossing verwachten
```

### Meerdere stakeholderbedrijven tegelijk

Je kunt de BA naar meerdere bedrijven sturen:
```
@Business Analyst Ga naar zowel De Vries Transport als Logistiek Noord.
Doel: vergelijk hun planningsprocessen en inventariseer gedeelde behoeften.
Schrijf daarna een consolidatierapport.
```

De BA voert afzonderlijke interviews per bedrijf en maakt daarna een vergelijkend consolidatierapport in `agents/project/requirements/consolidation.md`.

### Zelf een gesprek voeren met een stakeholder

Je kunt ook zelf rechtstreeks een gesprek voeren met een specifieke medewerker. De **Stakeholder**-agent neemt volledig de rol van die persoon over en antwoordt zoals die persoon zou antwoorden — met zijn expertise, zijn zorgen en zijn communicatiestijl.

```
/talk-to-stakeholder
```

Of direct:
```
@Stakeholder Ik wil praten met de operations manager van De Vries Transport.
Lees agents/stakeholders/de-vries.md voor het profiel.
```

Tijdens het gesprek:
- Stel vragen zoals je dat in een echt gesprek zou doen
- De persona reageert realistisch — inclusief twijfels, weerstand of enthousiasme
- De persona weet alleen wat zijn functie hem/haar zou laten weten

Gesprek beëindigen en analyseren:
```
stop
```
De agent stapt dan uit de rol en geeft een observatie: welke thema's kwamen naar boven, waar zat weerstand, welke requirements zijn impliciet geuit?

Na het gesprek kun je de bevindingen laten verwerken:
```
@Business Analyst Verwerk de bevindingen uit mijn gesprek met [persoon] als requirements en user stories
```

### Requirements doorzetten naar het team

Na de interviews:
```
@Planner Verwerk de user stories uit agents/project/requirements/user-stories.md in het projectplan

@Architect Bekijk agents/project/requirements/consolidation.md en bepaal de architectuurimplicaties
```

---

## 6. Agents aanpassen of toevoegen

### Een bestaande agent aanpassen

Bewerk het `.agent.md`-bestand van de agent direct in VS Code:
- `.github/agents/<naam>.agent.md`

Of gebruik het **Agent Customizations editor** (`Ctrl+Shift+P` → `Chat: Open Customizations`).

**Wat kun je aanpassen?**
- `description` — Wanneer wordt deze agent gekozen?
- `tools` — Welke tools heeft de agent toegang tot?
- `model` — Welk taalmodel gebruikt de agent?
- De inhoud (persona, werkwijze, beperkingen)

### Een nieuwe agent toevoegen

Gebruik het prompt:
```
/add-agent
```
Of typ:
```
Voeg een nieuwe agent toe aan het team met expertise in [jouw onderwerp]
```
Het prompt begeleidt je stap voor stap door het aanmaken van:
1. Het `.agent.md`-bestand
2. Het geheugenbestand in `agents/memory/`
3. De updates in de Orchestrator en copilot-instructies

### Tijdelijk een agent beperken

Voeg `user-invocable: false` toe aan de frontmatter van de agent om deze uit het keuzemenu te verbergen.

---

## 7. Projectvoortgang bewaken

### Projectbestanden bekijken

| Bestand/Map | Inhoud | Beheerd door |
|-------------|--------|-------------|
| `agents/project/plan.md` | Volledig projectplan per fase | Planner |
| `agents/project/milestones.md` | Mijlpalen met acceptatiecriteria | Orchestrator + Planner |
| `agents/project/decisions.md` | Architectuurbeslissingen (ADR's) | Architect |
| `agents/project/backlog.md` | Openstaande taken en bugs | Orchestrator |
| `project/src/` | Broncode van het project | Backend / Frontend / DevOps |
| `project/docs/` | Verslagen, rapporten, presentaties | Alle agents |
| `project/designs/` | UI/UX designs en mockups | Architect / Frontend |

### Een mijlpaal reviewen

```
/milestone-review
```
Of:
```
@Orchestrator Review Mijlpaal 1 en geef aan wat nog open staat
```

### Agents instrueren de voortgang bij te werken

```
@Orchestrator Update het backlog op basis van de voltooide taken van vandaag

@Tester Voer alle tests uit en rapporteer de status in milestones.md
```

---

## 8. GitHub Copilot Features Overzicht

### Custom Agents (`.github/agents/*.agent.md`)
Gespecialiseerde AI-persona's met eigen tools, instructies en gedragsregels. Elke agent heeft:
- Een `description` die bepaalt wanneer de agent automatisch wordt gekozen
- Een gefilterde set `tools` (bijv. geen `execute` voor de Planner)
- Een eigen persona en werkwijze in de inhoud

**Activeren**: Selecteer in de agent-dropdown of gebruik `@AgentNaam` in chat.

### Custom Instructions (`.github/instructions/*.instructions.md`)
Automatisch toegepaste richtlijnen die de Copilot altijd volgt voor bepaalde bestandstypen:
- `coding-standards.instructions.md` — Geldt voor alle codebestanden (via `applyTo`)
- `workflow.instructions.md` — Geldt voor multi-agent interacties

### Prompt Files (`.github/prompts/*.prompt.md`)
Herbruikbare taaksjablonen die je oproept via `/`:
```
/new-project           ← Start een nieuw project
/milestone-review      ← Review een mijlpaal
/add-agent             ← Voeg een agent toe
/standup               ← Dagelijkse standup
/add-stakeholder       ← Definieer een nieuw stakeholderbedrijf
/interview-stakeholder ← Stuur de BA naar een of meer stakeholders
/talk-to-stakeholder   ← Voer zelf een gesprek met een stakeholder-persona
```
**Tip**: Maak je eigen prompts voor taken die je vaak herhaalt.

### Copilot-instructies (`.github/copilot-instructions.md`)
Altijd-actieve globale instructies voor alle Copilot-interacties in dit project. Hier staan de teamregels, het delegatieprotocol en de taakoverzichtstabel.

### Agent Customizations Editor
Open via `Ctrl+Shift+P` → `Chat: Open Customizations`.
Geeft een overzicht van alle agents, prompts, instructions en MCP-servers.

### Subagents
Agents kunnen elkaar aanroepen. De Orchestrator roept automatisch de juiste specialist aan. Je kunt dit ook handmatig doen door in een agent-context een andere agent te noemen.

### MCP Servers (optioneel uitbreiden)
Voeg externe tools toe via `.vscode/mcp.json`:
- **GitHub MCP** — Issues, PR's, commits
- **Playwright MCP** — Browser-automatisering voor E2E-tests
- **Database MCP** — Directe databasetoegang

Zie [VS Code MCP documentatie](https://code.visualstudio.com/docs/copilot/chat/mcp-servers).

---

## 9. Tips & Tricks

### Geef altijd context mee
Agents werken beter met expliciete context:
```
@Backend Implementeer endpoint POST /api/orders — zie agents/project/decisions.md voor het datamodel
```

### Gebruik het geheugen effectief
Na een lange sessie, vraag de agent expliciet het geheugen bij te werken:
```
@Architect Update je geheugenbestand met de beslissingen die we vandaag hebben genomen
```

### Ketting van agents
Je kunt een workflow bouwen waarbij agents elkaar aanroepen:
```
@Orchestrator Laat de Architect het datamodel ontwerpen en geef dat daarna aan de Backend om te implementeren
```

### Agents vergelijken
Twijfel je over een aanpak? Vraag meerdere agents:
```
@Architect Wat zijn de trade-offs van MongoDB vs PostgreSQL voor dit project?
```

### Scopebewaking
Als een agent buiten zijn expertise treedt, corrigeer dit expliciet:
```
@Backend Dat is een DevOps-vraag. Vraag dit aan @DevOps.
```

### Plan regelmatig een review
Gebruik `/milestone-review` na elke voltooide fase om kwaliteitsborging te garanderen.

---

## 10. Problemen oplossen

### Agent reageert niet op `@AgentNaam`
- Controleer of `user-invocable: true` in de frontmatter staat
- Controleer of het bestand in `.github/agents/` staat (niet elders)
- Open de Agent Customizations Editor: `Ctrl+Shift+P` → `Chat: Open Customizations`

### Agent volgt de instructies niet
- Controleer of `.github/copilot-instructions.md` bestaat en valide Markdown is
- Bekijk de debug-logs: `...` menu in Chat → `Show Agent Debug Logs`
- Zorg dat de `description` duidelijke trigger-keywords bevat

### Prompt `/commando` werkt niet
- Bestand moet eindigen op `.prompt.md` in `.github/prompts/`
- Controleer YAML-frontmatter op syntax-fouten (gebruik tabs nooit, alleen spaties)
- Herlaad VS Code: `Ctrl+Shift+P` → `Developer: Reload Window`

### Agent gebruikt verkeerde tools
- Pas de `tools`-lijst aan in het `.agent.md`-bestand
- Gebruik minimale tool-sets: geef agents alleen wat ze echt nodig hebben

### Geheugenbestand raakt verouderd
Vraag de agent expliciet het bestand te resetten:
```
@Planner Lees het huidige plan opnieuw en synchroniseer je geheugenbestand
```

---

## Snelle referentie

| Actie | Commando |
|-------|---------|
| Nieuw project starten | `/new-project` |
| Dagelijkse standup | `/standup` |
| Mijlpaal reviewen | `/milestone-review` |
| Nieuwe agent toevoegen | `/add-agent` |
| Stakeholder toevoegen | `/add-stakeholder` |
| Stakeholder interviewen (door BA) | `/interview-stakeholder` |
| Zelf met stakeholder praten | `/talk-to-stakeholder` |
| Agent customizations openen | `Ctrl+Shift+P` → `Chat: Open Customizations` |
| Copilot Chat openen | `Ctrl+Alt+I` |
| Agent activeren | `@AgentNaam` in chat |
| Debug-logs bekijken | `...` → `Show Agent Debug Logs` in Chat |

---

*Omgeving opgezet met GitHub Copilot Custom Agents — VS Code*
*Documentatie: [code.visualstudio.com/docs/copilot](https://code.visualstudio.com/docs/copilot)*
