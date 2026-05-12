---
description: "Use when planning, coordinating, or reviewing multi-agent workflows. Describes how agents interact, delegate tasks, and maintain project state."
---

# Multi-Agent Workflow Richtlijnen

## Sessieprotocol

Elke agent volgt dit protocol aan het begin en einde van een sessie:

### Begin van de sessie
1. Lees je geheugenbestand (`agents/memory/<agent-naam>.md`)
2. Lees de relevante projectbestanden (plan, milestones, decisions)
3. Bevestig wat de opdracht is en welk resultaat verwacht wordt

### Einde van de sessie
1. Documenteer voltooide werk in de relevante projectbestanden
2. Update je geheugenbestand met nieuwe inzichten
3. Rapporteer aan de Orchestrator: wat gedaan, wat open staat

## Delegatieprotocol

Wanneer een agent een taak delegeert:
```
Delegeer aan [Agent]:
- Taak: [concrete omschrijving]
- Context: [relevante informatie]
- Verwachte output: [wat moet er terugkomen]
- Afhankelijkheden: [wat moet al klaar zijn]
```

## Escalatieprotocol

Een agent escaleert naar de Orchestrator als:
- De taak buiten de eigen expertise valt
- Er een blokkade is die externe input vereist
- Er tegenstrijdige requirements zijn
- Een beslissing buiten de agent-scope valt

## Beslissingsauthoriteit

| Beslissingstype | Bevoegde agent |
|----------------|---------------|
| Projectscope aanpassen | Orchestrator + gebruiker |
| Architectuurkeuze | Architect |
| Implementatiedetails | Backend / Frontend |
| Design- en UX-beslissingen | UX Designer |
| Testcriteria | Tester + Planner |
| Deployment aanpak | DevOps + Architect |
| Planning aanpassen | Planner + Orchestrator |
| Juridische compliance & wetgeving | Legal (vastleggen als LAR in decisions.md) |

## Kwaliteitspoorten

Vóór een mijlpaal als voltooid wordt gemarkeerd:
- [ ] Alle acceptatiecriteria zijn aangevinkt
- [ ] Tester heeft de tests uitgevoerd
- [ ] Architect heeft de conformiteitscheck gedaan
- [ ] Legal heeft compliance-check gedaan voor mijlpalen met juridische impact
- [ ] Geen openstaande 🔴 kritieke items in het backlog

## Projectdeliverables-mapstructuur

Alle opbrengsten van het project worden opgeslagen in de `project/`-map in de root:

```
project/
  src/        ← Broncode (backend, frontend, services, infra-configs)
  docs/       ← Verslagen, rapporten, presentaties, handleidingen
  designs/    ← UI/UX designs, mockups, wireframes, style guides
  README.md   ← Projectoverzicht en mapbeschrijving
```

### Toewijzingsregels per agent

| Agent | Levert op in |
|-------|-------------|
| Backend | `project/src/` |
| Frontend | `project/src/` |
| DevOps | `project/src/infra/` of `project/src/` |
| Architect | `project/designs/` (schema's), `project/docs/` (ADR-exports) |
| UX Designer | `project/designs/` (wireframes, mockups, design system, handoff, Stitch-exports) || Legal | `project/docs/legal/` (auditrapportages, LAR-exports, compliance-checklists) || Planner | `project/docs/` (plannings- en voortgangsverslagen) |
| Business Analyst | `project/docs/` (interviewrapporten, requirement-specs) |
| Tester | `project/src/` (tests naast de broncode) |

> **Onderscheid**: `agents/project/` bevat **beheerbestanden** (plan, milestones, backlog, decisions).  
> `project/` bevat de **daadwerkelijke deliverables** die worden opgeleverd aan de opdrachtgever.
