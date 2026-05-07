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
| Testcriteria | Tester + Planner |
| Deployment aanpak | DevOps + Architect |
| Planning aanpassen | Planner + Orchestrator |

## Kwaliteitspoorten

Vóór een mijlpaal als voltooid wordt gemarkeerd:
- [ ] Alle acceptatiecriteria zijn aangevinkt
- [ ] Tester heeft de tests uitgevoerd
- [ ] Architect heeft de conformiteitscheck gedaan
- [ ] Geen openstaande 🔴 kritieke items in het backlog
