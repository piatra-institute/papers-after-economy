# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-06-13 — voice reform

Scope: density and rhythm pass against the house voice guide. The paper read
clean on the gate but ran on a metronome of reflexive enumerations.

Changes:
- Tricolon reflex: brought the three-plus-item-list proxy from 86 to 61 by
  varying the worst reflexive enumerations across §1-§12 (asyndeton, semicolon
  regrouping, "each/all" recasts, occasional trims), leaving genuine
  enumerations intact. No item carrying argument was dropped.
- §12 closers de-metronomed: the nine-fold "X shows Y" recap and the six-item
  final list rewritten so the rhythm varies; "Conclusion" retitled to "What
  Survives Price."
- Syntax warns (4 inline-contrastive ", not Z") rewritten as positive
  declaratives in §3 (ATP), §9 (calculation/domination), §11 (model scope, two).

Verification: voice 0 errors, 0 review-candidates; refs advisory (narrative
citations, unchanged); claims 0 unmatched (no number touched); build clean;
check => PASS. Status unchanged.

## 2026-05-29 — upgrade pass (Group B)

Scope: integrate the §11 model better and flag the biological-cost metaphor.

Changes:
- §3: dropped the "This point blocks a common reduction" throat-clear; flagged
  that the cellular/organismal "cost" is read as analogy, not identity; added a
  forward-reference to the §11 model so it no longer arrives unannounced.
- §11: added a model-epistemology statement (what the stylised model claims —
  mechanism and direction, not magnitude of any real economy).

Verification: voice 0 errors; refs advisory (humanities); claims 0 unmatched
(no new numbers); build clean; check => PASS. Status remains `built` (off-web).

## 2026-05-29 — computational layer added

Scope: instrument the "price is an interface, not ontology" thesis with a
simulation; bring to the publication bar.

Changes:
- New `simulation/`: allocation of a fixed budget across six sectors with
  concave viability returns, by three coordinators — constraint (no price),
  faithful price, and financialised price (speculative markup on finance).
  Water-filling on marginal viability; `output/results.json` + two figures.
- New §11 "A model of allocation under constraint"; Conclusion renumbered §12.
  Abstract gains one sentence carrying the headline numbers.
- metadata: `has_simulation: true`, `claims_target: results.json`.

Verification:
- claims: 6 prose decimals, **0 unmatched** — all trace to results.json
  (optimum viability 4.97; faithful-price divergence 0.0; financialised d=3
  loses 8.08% with finance share 0.02 → 0.26; 25.1% loss at d=8).
- voice: 0 errors (humanities `, not` contrasts kept as warns).
- refs: advisory (primary-source title-year style; reconcile by hand).
- build: clean, 11 pages, zero missing-character warnings. check => PASS.

Outstanding: GitHub repo private; not yet on the web papers page.
