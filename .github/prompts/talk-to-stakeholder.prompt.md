---
description: "Start een direct gesprek met een specifieke stakeholder-persona: kies een bedrijf en persoon en voer zelf het interview."
name: "Praten met Stakeholder"
agent: "agent"
argument-hint: "Noem het bedrijf en optioneel de persoon, bijv: 'Jan de Vries @ De Vries Transport'..."
tools: [read, agent]
---

# Direct gesprek met een stakeholder starten

Je gaat een één-op-één gesprek voeren met een specifieke medewerker van een stakeholderbedrijf.

## Stap 1: Bepaal met wie je praat

Controleer of de volgende informatie beschikbaar is (vraag anders aan de gebruiker):
1. **Welk bedrijf?** — Welk bestand in `agents/stakeholders/` moet gebruikt worden?
2. **Welke persoon?** — Als niet opgegeven: geef een lijst van beschikbare medewerkers uit het profiel en laat de gebruiker kiezen
3. **Is er een context of doel?** — Optioneel: "Ik wil weten wat hij vindt van ons voorstel voor een nieuw systeem"

## Stap 2: Stakeholderprofiel laden

Lees `agents/stakeholders/<bedrijfsnaam>.md` en extraheer:
- Het bedrijfsprofiel (cultuur, werkwijze, pijnpunten)
- Het persoonsprofiel van de gekozen medewerker

Als het bestand niet bestaat:
> "Dit bedrijf heeft nog geen stakeholderprofiel. Maak er eerst een aan via `/add-stakeholder`."

## Stap 3: Gesprek overdragen aan de Stakeholder-agent

Activeer de **Stakeholder**-agent met de volgende context:

```
Bedrijf: [naam]
Profielbestand: agents/stakeholders/[bestandsnaam].md
Persoon: [naam en functie]
Eventuele gesprekscontext: [doel of onderwerp]
```

De Stakeholder-agent neemt daarna volledig de rol over.

## Stap 4: Na het gesprek (optioneel)

Als het gesprek is afgesloten, vraag de gebruiker:
> "Wil je de bevindingen uit dit gesprek laten verwerken door de Business Analyst als requirements?"

Zo ja: activeer de **Business Analyst** met het gespreksverslag.
