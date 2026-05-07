---
description: "Use when writing any code in this project. Enforces coding standards, naming conventions, security practices, and documentation requirements."
applyTo: "**/*.{ts,tsx,cs,js,jsx,py,go,java}"
---

# Codestandaarden

## Algemene principes

- **SOLID** — Volg de SOLID-principes in alle klassen en modules
- **DRY** — Dupliceer geen logica; maak herbruikbare functies/componenten
- **KISS** — Houd implementaties zo eenvoudig mogelijk
- **YAGNI** — Bouw geen features die nu niet nodig zijn

## Naamgeving

- Variabelen en functies: `camelCase` (JS/TS/Java/C#) of `snake_case` (Python/Go)
- Klassen en types: `PascalCase`
- Constanten: `UPPER_SNAKE_CASE`
- Private members: prefix `_` of gebruik access modifiers
- Bestandsnamen: volg de conventie van het framework

## Commentaar en documentatie

- Schrijf commentaar alleen als de code zelf niet duidelijk is
- Gebruik JSDoc/XML-doc/docstrings voor publieke API's
- Elke module/klasse heeft een korte beschrijving van het doel

## Foutafhandeling

- Gebruik specifieke exception-types (geen generieke `catch (e)`)
- Log fouten met context (wat, waar, wanneer)
- Return nooit `null` waar een lege collectie of `Optional` beter is
- Valideer altijd externe input (gebruikersinvoer, API-responses)

## Security (OWASP Top 10)

- Gebruik altijd parameterized queries of ORM — nooit string-concatenation in SQL
- Valideer en saniteer alle input aan de serverkant
- Sla nooit wachtwoorden, secrets of API-keys op in code of logbestanden
- Gebruik HTTPS voor alle externe communicatie
- Implementeer rate limiting voor publieke API-endpoints

## Tests

- Minimaal één unit test per publieke functie/methode
- Gebruik het AAA-patroon: Arrange / Act / Assert
- Testnamen beschrijven het scenario: `should_throw_when_input_is_null`
- Geen hardcoded test-data in productie-code

## Git-conventies

Zie de volledige Git-werkwijze in `.github/instructions/git-workflow.instructions.md`.

- Werk altijd op een **feature-branch** — nooit direct op `main` of `develop`
- Branch-formaat: `feature/<scope>/<naam>`, `fix/<scope>/<naam>`, `chore/<naam>`
- Commit messages: `type(scope): beschrijving` (bijv. `feat(auth): voeg JWT refresh toe`)
- Types: `feat`, `fix`, `test`, `refactor`, `docs`, `chore`, `style`, `perf`
- Pull requests zijn **scoped**: één logisch geheel per PR
- Grote features **opsplitsen** in meerdere PR's als dit de review verbetert
- Elke PR bevat de bijbehorende tests
- Minimaal één approval vereist voor merge
