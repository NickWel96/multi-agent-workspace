---
description: "Voer een stakeholderinterview uit: ga naar één of meerdere bedrijven met een specifiek doel en inventariseer wensen, eisen en werkprocessen."
argument-hint: "Noem het/de stakeholderbedrijf/ven en het interviewdoel..."
model: sonnet
---

# Stakeholder Interview uitvoeren

De Business Analyst gaat op bezoek bij één of meerdere stakeholderbedrijven om wensen en eisen te inventariseren.

## Stap 1: Parameters ophalen

Verzamel (of vraag de gebruiker):
1. **Welke bedrijven?** — één of meerdere uit `agents/stakeholders/`
2. **Wat is het doel?** — Bijv. "inventariseer het huidige orderproces" of "achterhaal wat ze van een klantportaal verwachten"
3. **Zijn er specifieke vragen?** — Optioneel; anders bepaalt de BA zelf de vragen
4. **Is er een prioriteit?** — Bijv. "focus op must-haves voor de MVP"

## Stap 2: Lees de stakeholderprofielen

Voor elk opgegeven bedrijf:
- Lees `agents/stakeholders/<bedrijfsnaam>.md`
- Als het bestand niet bestaat: vraag de gebruiker het aan te maken via `/add-stakeholder`

## Stap 3: Delegeer aan de Business Analyst

Activeer de **Business Analyst**-agent met de volgende context:

```
Doel: [het opgegeven doel]
Bedrijven: [lijst van bedrijven]
Stakeholderprofielen: [verwijzing naar de bestanden]
Eventuele specifieke vragen: [of "bepaal zelf op basis van het doel"]
```

De Business Analyst:
1. Selecteert de relevante gesprekspartners per bedrijf
2. Voert de gesimuleerde interviews uit
3. Schrijft rapporten naar `agents/project/requirements/`
4. Schrijft user stories naar `agents/project/requirements/user-stories.md`

## Stap 4: Bij meerdere bedrijven — consolidatie

Als er meerdere stakeholderbedrijven zijn:
- Vergelijk de interviewrapporten
- Identificeer overeenkomsten en conflicten
- Schrijf een consolidatierapport: `agents/project/requirements/consolidation.md`

## Stap 5: Doorsturen naar het team

Na de interviews:
- **Planner**: update het projectplan op basis van de nieuw gevonden requirements
- **Architect**: bekijk of de architectuur aanpassingen nodig heeft
- Voeg nieuwe taken toe aan `agents/project/backlog.md`

## Stap 6: Rapporteer aan de gebruiker

Geef een overzicht van:
- Met wie is gesproken (per bedrijf)
- De top-5 belangrijkste bevindingen
- Eventuele showstoppers of conflicten
- Aantal gedocumenteerde user stories (US-XXX t/m US-YYY)
- Aanbevolen vervolgstappen
