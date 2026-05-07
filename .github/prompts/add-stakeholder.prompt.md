---
description: "Voeg een nieuw stakeholderbedrijf toe: definieer het bedrijfsprofiel, de bedrijfscultuur en de medewerkers die geïnterviewd kunnen worden."
name: "Stakeholder Toevoegen"
agent: "agent"
argument-hint: "Beschrijf het bedrijf dat je als stakeholder wilt toevoegen..."
tools: [read, edit, search]
---

# Nieuw stakeholderbedrijf toevoegen

Maak een volledig stakeholderprofiel aan voor een nieuw bedrijf.

## Stap 1: Basisinformatie verzamelen

Vraag de gebruiker om de volgende informatie (of verwerk wat al opgegeven is):

**Over het bedrijf:**
1. Bedrijfsnaam en sector?
2. Grootte van het bedrijf (aantal medewerkers, MKB/enterprise)?
3. Wat doet het bedrijf hoofdzakelijk?
4. Wie zijn hun klanten (B2B / B2C / overheid)?
5. Beschrijf de bedrijfscultuur en werkwijze in een paar zinnen

**Huidige situatie:**
6. Wat zijn de bekende pijnpunten of uitdagingen?
7. Welke systemen gebruiken ze al?
8. Hebben ze eerder slechte ervaringen met IT-projecten?

## Stap 2: Medewerkers definiëren

Voor elke medewerker:
1. Naam en functie
2. Afdeling en ervaringsniveau
3. Beslissingsbevoegdheid (wie heeft het laatste woord?)
4. Expertisegebieden
5. Prioriteiten en belangen (wat vindt hij/zij belangrijk?)
6. Communicatiestijl (direct/uitgebreid, technisch/functioneel, sceptisch/enthousiast)
7. Bekende zorgen of weerstand

**Tip**: Vraag de gebruiker minstens 2–4 medewerkers te definiëren voor realistische gespreksgroepen:
- Minimaal één beslisser (manager/directeur)
- Minimaal één dagelijkse gebruiker (operationeel medewerker)
- Optioneel: IT-verantwoordelijke, financieel verantwoordelijke

## Stap 3: Bestand aanmaken

Maak het bestand `agents/stakeholders/<bedrijfsnaam-lowercase-zonder-spaties>.md` aan.
Gebruik het sjabloon `agents/stakeholders/_template.md` als basis.

Vul alle secties in op basis van de verzamelde informatie.

## Stap 4: README bijwerken

Voeg het bedrijf toe aan de tabel in `agents/stakeholders/README.md`.

## Stap 5: Bevestig aan de gebruiker

Rapporteer:
- Welk bestand is aangemaakt
- Hoeveel medewerkers zijn gedefinieerd
- Suggestie voor eerste interviewdoel:
  > "Gebruik `/interview-stakeholder` om de Business Analyst naar [bedrijfsnaam] te sturen."
