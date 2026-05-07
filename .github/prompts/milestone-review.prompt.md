---
description: "Beoordeel de voortgang van een mijlpaal: laat de Tester testen, rapporteer blokkades en bepaal de volgende stappen."
name: "Mijlpaal Review"
agent: "agent"
argument-hint: "Welke mijlpaal wil je reviewen? (bijv. Mijlpaal 1)"
tools: [read, edit, search, agent, todo]
---

# Mijlpaal Review

Voer een volledige review uit van de opgegeven mijlpaal.

## Stap 1: Huidige status ophalen

Lees:
- `agents/project/milestones.md` — status van de mijlpaal
- `agents/project/backlog.md` — openstaande taken
- `agents/project/decisions.md` — relevante architectuurbeslissingen

## Stap 2: Technische kwaliteitscheck

Delegeer aan de **Tester**-agent:
- Voer testplannen uit voor de geïmplementeerde features
- Rapporteer: welke tests slagen, welke falen
- Voeg gevonden bugs toe aan `agents/project/backlog.md`

## Stap 3: Architectuurconformiteitscheck

Delegeer aan de **Architect**-agent:
- Controleer of de implementatie overeenkomt met de ADR's
- Signaleer afwijkingen of technische schuld

## Stap 4: Mijlpaalstatus bijwerken

Op basis van de resultaten:
- Update de acceptatiecriteria-checkboxes in `agents/project/milestones.md`
- Markeer de mijlpaal als ✅ Voltooid of 🔄 In uitvoering
- Voeg openstaande punten toe aan het backlog

## Stap 5: Rapporteer aan de gebruiker

Geef een overzicht van:
- Wat is opgeleverd (✅ acceptatiecriteria)
- Wat is nog open (❌ acceptatiecriteria + bugs)
- Aanbeveling: doorgaan naar volgende mijlpaal of eerst herstellen?
- Volgende stappen voor het team
