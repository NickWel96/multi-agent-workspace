---
description: "Start een nieuw project op: laat het team een plan opstellen, de architectuur definiëren en de eerste mijlpalen bepalen."
name: "Nieuw Project Starten"
agent: "agent"
argument-hint: "Beschrijf het project dat je wilt bouwen..."
tools: [read, edit, search, agent, todo]
---

# Nieuw project opstarten

Je gaat een nieuw softwareproject starten met het multi-agent team. Volg deze stappen:

## Stap 1: Projectbeschrijving ophalen

Vraag de gebruiker (als nog niet opgegeven) om:
1. Wat is de naam en het doel van het project?
2. Wat zijn de belangrijkste functionaliteiten (top 3-5)?
3. Welke technologiestack heeft de voorkeur (of is er vrijheid)?
4. Wat zijn eventuele constraints (deadline, budget, team-grootte)?
5. Wie zijn de eindgebruikers?

## Stap 2: Planner activeert het projectplan

Delegeer aan de **Planner**-agent:
- Maak een volledig projectplan in `agents/project/plan.md`
- Definieer minimaal 3 fasen (MVP → uitbreiding → optimalisatie)
- Maak mijlpalen aan in `agents/project/milestones.md`

## Stap 3: Architect definieert de technische basis

Delegeer aan de **Architect**-agent:
- Selecteer de technologiestack
- Documenteer als ADR-001 in `agents/project/decisions.md`
- Maak een high-level architectuurschema (Mermaid)
- Definieer de eerste API-contracten

## Stap 4: Orchestrator initialiseert de werkstructuur

Na de bovenstaande stappen:
1. Update `agents/memory/orchestrator.md` met het nieuwe project
2. Vul de teamstatus-tabel in
3. Zet de eerste sprint-taken in `agents/project/backlog.md`
4. Maak de **project-deliverables-mapstructuur** aan als die nog niet bestaat:
   - `project/src/` — voor alle broncode
   - `project/docs/` — voor verslagen, rapporten en presentaties
   - `project/designs/` — voor designs en mockups
   - Pas `project/README.md` aan met de projectnaam en een korte beschrijving

## Stap 5: Rapporteer aan de gebruiker

Geef een overzicht van:
- Het projectplan (samenvatting per fase)
- De gekozen architectuur
- De eerste 5 prioriteitstaken
- Welke agent als volgende aan de beurt is
