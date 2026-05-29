---
description: "Voeg een nieuwe specialistagent toe aan het team: definieer de expertise, maak het agent-bestand en het geheugenbestand aan."
argument-hint: "Beschrijf de expertise van de nieuwe agent (bijv. 'Security Expert' of 'Data Scientist')..."
model: sonnet
---

# Nieuwe agent toevoegen aan het team

Maak een nieuwe specialistagent aan op basis van de opgegeven expertise.

## Stap 1: Agentprofiel bepalen

Verzamel de volgende informatie (vraag de gebruiker als niet opgegeven):
1. **Naam van de agent**: (bijv. "Security Expert")
2. **Bestandsnaam (kebab-case)**: (bijv. `security`)
3. **Expertise**: Wat weet deze agent als geen ander?
4. **Taken**: Welke taken worden aan deze agent gedelegeerd?
5. **Tools nodig**: (read, edit, search, execute, agent, fetch?)
6. **Interactie met andere agents**: Met wie werkt deze agent samen?

## Stap 2: Agent-definitiebestanden aanmaken (BEIDE formaten)

Maak de Copilot-bron `.github/agents/<naam>.agent.md` aan met:
- Correcte frontmatter (description met trigger-keywords, tools, model)
- Duidelijke persona en verantwoordelijkheden
- Werkwijze met concrete stappen
- Beperkingen (wat doet deze agent NIET)
- Instructie om het geheugenbestand te lezen/schrijven

Genereer daarna de Claude Code-versie met `python3 .claude/convert.py` (maakt
`.claude/agents/<naam>.md`), of maak die handmatig met de Claude Code-frontmatter.

## Stap 3: Geheugenbestand aanmaken

Maak `agents/memory/<naam>.md` aan met:
- Standaard secties (Technologiestack, Patronen, Geleerde lessen)
- Initiële lege waarden
- Datum-placeholder

## Stap 4: Orchestrator bijwerken

Update `agents/memory/orchestrator.md`:
- Voeg de nieuwe agent toe aan de teamstatus-tabel
- Voeg de agent toe aan de taakverdeling

## Stap 5: Globale instructies bijwerken (BEIDE)

- `.github/copilot-instructions.md` — voeg de agent toe aan de taakoverzichtstabel
- `CLAUDE.md` — voeg de agent toe aan de team-tabel (met zijn `subagent_type`)

## Stap 6: Rapporteer

Geef een overzicht van:
- Welke bestanden zijn aangemaakt (`.github/agents/`, `.claude/agents/`, geheugen)
- Hoe de agent te activeren is: Copilot → `@<naam>`; Claude Code → benoem hem / `subagent_type`
- Welke bestaande taken eventueel aan de nieuwe agent gedelegeerd kunnen worden
