# Audit

Dated log of editorial passes and verification runs. Newest first.

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
