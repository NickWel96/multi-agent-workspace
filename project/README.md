# Project Deliverables

> Dit is de **werkmap** voor alle projectopbrengsten: broncode, designs, documentatie, presentaties en verslagen.  
> Beheerbestanden (planning, milestones, backlog) staan in `agents/project/`.

---

## Mapstructuur

```
project/
  src/          ← Broncode (backend, frontend, services, etc.)
  docs/         ← Verslagen, rapporten, presentaties, handleidingen
  designs/      ← UI/UX designs, mockups, wireframes, style guides
```

## Richtlijnen

### Broncode (`src/`)
- Organiseer per component, service of laag (bijv. `src/api/`, `src/frontend/`, `src/shared/`)
- Volg de projectspecifieke mapstructuur zoals vastgelegd in `agents/project/decisions.md`
- Alle code-wijzigingen verlopen via feature-branches en pull requests (zie `.github/instructions/git-workflow.instructions.md`)

### Documentatie (`docs/`)
Bewaar hier alle **niet-code deliverables**:
- Verslagen en meeting-notulen
- Technische documentatie en handleidingen
- Presentaties (PowerPoint, Keynote, PDF)
- Functionele specificaties

### Designs (`designs/`)
Bewaar hier alle **visuele ontwerpen**:
- Wireframes en prototypes
- UI-mockups en schermen
- Style guides en designsystemen
- Exportbestanden (.fig, .sketch, .pdf, .png)

---

## Naamconventie bestanden

| Type | Voorbeeld |
|------|-----------|
| Verslag | `docs/verslag-sprint-1.md` |
| Presentatie | `docs/presentatie-kickoff.pdf` |
| Wireframe | `designs/wireframe-dashboard-v1.png` |
| Technisch doc | `docs/api-documentatie.md` |

---

_Dit bestand wordt aangemaakt bij het starten van een nieuw project. Pas de structuur aan op de specifieke projectbehoeften._
