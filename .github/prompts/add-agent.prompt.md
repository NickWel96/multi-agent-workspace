---
description: "Voeg een nieuwe specialistagent toe aan het team: definieer de expertise, maak het agent-bestand en het geheugenbestand aan."
name: "Agent Toevoegen"
agent: "agent"
argument-hint: "Beschrijf de expertise van de nieuwe agent (bijv. 'Security Expert' of 'Data Scientist')..."
tools: [read, edit, search, todo]
---

# Nieuwe agent toevoegen aan het team

Maak een nieuwe specialistagent aan op basis van de opgegeven expertise.

## Stap 1: Agentprofiel bepalen

Verzamel de volgende informatie (vraag de gebruiker als niet opgegeven):
1. **Naam van de agent**: (bijv. "Security Expert")
2. **Bestandsnaam**: (bijv. `security.agent.md`)
3. **Expertise**: Wat weet deze agent als geen ander?
4. **Taken**: Welke taken worden aan deze agent gedelegeerd?
5. **Tools nodig**: (read, edit, search, execute, agent?)
6. **Interactie met andere agents**: Met wie werkt deze agent samen?

## Stap 2: Agent-definitiebestand aanmaken

Maak `.github/agents/<naam>.agent.md` aan met:
- Correcte frontmatter (description met trigger-keywords, tools, model)
- Duidelijke persona en verantwoordelijkheden
- Werkwijze met concrete stappen
- Beperkingen (wat doet deze agent NIET)
- Instructie om het geheugenbestand te lezen/schrijven

## Stap 3: Geheugenbestand aanmaken

Maak `agents/memory/<naam>.md` aan met:
- Standaard secties (Technologiestack, Patronen, Geleerde lessen)
- Initiële lege waarden
- Datum-placeholder

## Stap 4: Orchestrator bijwerken

Update `agents/memory/orchestrator.md`:
- Voeg de nieuwe agent toe aan de teamstatus-tabel
- Voeg de agent toe aan de taakverdeling

## Stap 5: Copilot-instructies bijwerken

Update `.github/copilot-instructions.md`:
- Voeg de nieuwe agent toe aan de taakoverzichtstabel

## Stap 6: Rapporteer

Geef een overzicht van:
- Welke bestanden zijn aangemaakt
- Hoe de nieuwe agent te activeren is (via `@<naam>` in chat)
- Welke bestaande taken eventueel aan de nieuwe agent gedelegeerd kunnen worden
