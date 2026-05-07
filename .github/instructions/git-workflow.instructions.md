---
description: "Use when working with Git, creating branches, making commits, opening pull requests, reviewing code, or merging features. Enforces the project's branching strategy and PR workflow."
---

# Git Werkwijze

## Branchingstrategie

```
main              ← Stabiele productietak — direct pushen is VERBODEN
└── develop       ← Integratiebranch — features worden hier in gemerged
    └── feature/<scope>/<beschrijving>   ← Nieuwe features
    └── fix/<scope>/<beschrijving>       ← Bugfixes
    └── chore/<beschrijving>             ← Technische schuld, refactoring
    └── docs/<beschrijving>              ← Documentatie
```

## Branchnamen

Formaat: `<type>/<scope>/<korte-beschrijving-kebab-case>`

| Type | Wanneer |
|------|---------|
| `feature/` | Nieuwe functionaliteit |
| `fix/` | Bugfix |
| `chore/` | Refactoring, dependency-updates, technische schuld |
| `docs/` | Documentatie-updates |
| `release/` | Release-voorbereiding |

**Voorbeelden**:
```
feature/auth/user-login
feature/orders/create-order-api
fix/auth/token-expiry-not-handled
chore/cleanup/remove-deprecated-endpoints
```

## Commit-conventies

Formaat: `type(scope): beschrijving` — schrijf in de tegenwoordige tijd, Nederlandstalig of Engelstalig (consistent binnen project)

```
feat(auth): voeg JWT refresh token toe
fix(orders): herstel null-pointer bij lege orderlijst
test(auth): voeg integratietests toe voor login endpoint
refactor(users): extraheer validatielogica naar service
docs(api): update OpenAPI spec voor orders endpoint
chore(deps): upgrade Entity Framework naar 9.0
```

**Types**: `feat`, `fix`, `test`, `refactor`, `docs`, `chore`, `style`, `perf`

## Pull Requests

### Scope-regels
- Eén PR = één logisch afgerond geheel (feature, fix of refactoring)
- Een feature **mag en moet** opgesplitst worden in meerdere PR's als dit de review verbetert
- Richtlijn: ≤ 400 gewijzigde regels per PR — bij meer, overweeg opsplitsing
- Een PR bevat **altijd** de bijbehorende tests
- Merge nooit rechtstreeks in `main` — altijd via `develop`

### PR-titels

Gebruik hetzelfde formaat als commit-messages:
```
feat(auth): implementeer JWT-authenticatie
fix(orders): herstel berekeningsfout bij kortingen
```

### PR-beschrijving (verplicht)

```markdown
## Wat doet deze PR?
[Korte omschrijving van de wijziging]

## Gerelateerde user story / taak
US-NNN of backlog-item [ID]

## Type wijziging
- [ ] Nieuwe feature
- [ ] Bugfix
- [ ] Refactoring
- [ ] Documentatie

## Testbewijs
- [ ] Unit tests toegevoegd / bijgewerkt
- [ ] Integratietests toegevoegd / bijgewerkt
- [ ] Handmatig getest (beschrijf scenario)

## Breaking changes?
Ja / Nee — [toelichting]

## Review-aandachtspunten
[Waar wil je specifiek feedback op?]
```

### Review-regels

- Elke PR vereist minimaal **één goedkeuring** voor merge
- De **Tester** reviewt op testdekking en correctheid
- De **Architect** reviewt op conformiteit met de architectuur bij structurele wijzigingen
- Reviewers laten constructieve, specifieke opmerkingen achter
- Een PR mag pas gemerged worden als:
  - Alle CI-checks groen zijn
  - Alle reviewopmerkingen zijn afgehandeld
  - Minimaal één approval is gegeven

### Merge-strategie

- Gebruik **Squash and Merge** voor feature-branches → schone `develop`-history
- Gebruik **Merge commit** voor release-branches naar `main`
- Verwijder de branch na merge

## Agents en Git

Agents mogen zelfstandig:
- Een feature-branch aanmaken
- Commits doen op die branch
- Een PR openen met correcte beschrijving
- Een PR reviewen en goedkeuren (mits niet de eigen PR)

Agents mogen **NIET** zelfstandig:
- Direct pushen naar `main` of `develop`
- Een PR mergen zonder minimaal één approval van een andere agent of de gebruiker
- Branches verwijderen die nog niet gemerged zijn

## Branch aanmaken — werkwijze voor agents

Voor elke nieuwe feature of fix:
1. Zorg dat je op de laatste versie van `develop` zit
2. Maak een branch aan: `git checkout -b feature/<scope>/<naam>`
3. Implementeer en commit in kleine, logische stappen
4. Push de branch: `git push -u origin feature/<scope>/<naam>`
5. Open een PR naar `develop` met de verplichte beschrijving
6. Vraag review aan bij de Tester (en Architect bij structurele wijzigingen)
