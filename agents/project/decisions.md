# Architectuurbeslissingen (ADR's)

> Beheerd door de **Architect**-agent. Elke significante technische beslissing wordt hier gedocumenteerd.

## Technologiestack samenvatting
_[Wordt ingevuld na de eerste architectuursessie]_

---

## ADR's

_[Wordt gegenereerd door de Architect. Zie onderstaand formaat.]_

---

## ADR-formaat (sjabloon)

```markdown
## ADR-NNN: [Titel]
**Datum**: YYYY-MM-DD
**Status**: Proposed | Accepted | Deprecated | Superseded by ADR-NNN
**Auteur**: Architect

### Context
[Waarom moest er een beslissing worden genomen? Wat was het probleem of de vraag?]

### Beslissing
[Wat is besloten? Wees concreet.]

### Consequenties
**Positief**:
- ...
**Negatief / Trade-offs**:
- ...

### Overwogen alternatieven
| Alternatief | Reden afgewezen |
|-------------|----------------|
| ... | ... |
```

---

## LAR-formaat (sjabloon voor juridische beslissingen)

> Beheerd door de **Legal**-agent. Elke juridische beoordeling, compliance-bevinding of wettelijke afweging wordt hier vastgelegd ten behoeve van auditeerbaarheid.

```markdown
## LAR-NNN: [Titel]
**Datum**: YYYY-MM-DD
**Status**: Open | Geaccepteerd | Opgevolgd | Niet van toepassing
**Risico**: 🟢 Laag | 🟡 Middel | 🔴 Hoog | 🚨 Kritiek
**Auteur**: Legal
**Gerelateerde ADR**: ADR-NNN (indien van toepassing)

### Juridische context
[Welke wet of regelgeving is van toepassing? Welk artikel?]

### Bevinding
[Wat is geconstateerd? Is er een risico of overtreding?]

### Advies
[Wat wordt aanbevolen om compliant te zijn of het risico te mitigeren?]

### Beslissing door team
[Wat heeft het team besloten naar aanleiding van dit advies?]

### Actiepunten
- [ ] [Concrete actie] — verantwoordelijk: [agent/persoon]
```

---

## LAR's

_[Wordt gegenereerd door de Legal agent.]_

---
_Laatste update: [datum]_
_Bijgewerkt door: Architect / Legal_
