# Audit

Dated log of editorial passes and verification runs. Newest first.

## 2026-09-23 — structured-evidence migration

Structured-evidence migration (references and claims).
- references.yaml: 45 CSL entries, entered by hand (only 7 of 47 legacy entries had automatic Crossref matches); DOIs checked for bourdieu1972, epstein2005, friston2010, georgescuroegen1971, goody1986, krippner2011, mitchell1998, molenaar2009, ostrom1990, scott2010, scott2017, stern2011, varela1991.
- Corrections: legacy entries that paired English translation titles with the original publisher and year now carry the original titles (Bataille, La part maudite; Braudel, Civilisation matérielle, économie et capitalisme; Girard, La violence et le sacré; Marx, Das Kapital; Nietzsche, Zur Genealogie der Moral; Simmel, Philosophie des Geldes; Uexküll and Kriszat, Streifzüge durch die Umwelten von Tieren und Menschen, with Kriszat added as co-author; Weber, Die protestantische Ethik und der "Geist" des Kapitalismus). Accents restored in French and German titles. Baudrillard 1972 and Lyotard 1974 removed (listed but never cited).
- Citations: possessive forms converted to suppress-author citations ("Deacon's [-@deacon2011] account"), which render as before.
- claims.yaml: 27 claims (14 computation, 3 source, 5 interpretation, 2 assumption, 2 definition, 1 normative). Every model number in the abstract and section 11 is bound to simulation/output/results.json; "more than half" and "monotonically and faster than linearly" are interpretations citing the stored sweep. Source claims checked against OpenAlex abstracts: Molenaar et al. (cellular resource allocation), Mitchell (the economy as a mid-twentieth-century object), Ostrom (commons outside state and market).
- Not bound (books without retrievable abstracts, or abstract silent): Friston 2010, Hayek, Mises, Mauss, Polanyi, Graeber, Krippner's definition of financialization, Scott 2017, Hudson, Nissen et al., Simon on attention, Banks, and the other book-length sources.
- Execution receipt: run after-economy (uv run python run_all.py); results.json reproduced byte-identically.
- metadata claims_target: results.json -> claim-ledger.

## 2026-09-23 — prose revision

Prose revised against the house standards. Headings: Abstract; 1. Introduction; 2. Constraint and flow; 3. Cost in cells and organisms; 4. Sensorimotor transaction; 5. Gift and obligation; 6. Blood compensation; 7. Fiscal administration before capitalism; 8. Money, markets, and capital; 9. Financialization and computational allocation; 10. Ecological limits and post-scarcity; 11. A stylized allocation model; 12. Conclusion; Reproducibility.
Tic counts before -> after: 'rather than' 4 -> 0; inline ', not X' 2 -> 0; exactly/precisely 2 -> 0; 'nothing more' removed. American spelling kept throughout.
Citations: authors previously named without dates (Deacon, Prigogine, Schrodinger, Gibson, Uexkull, Mauss, Bourdieu, Polanyi, Sahlins, Graeber, Nietzsche, Girard, Bataille, Scott, Goody, Schmandt-Besserat, Hudson, Mitchell, Simmel, Marx, Weber, Braudel, Krippner, Hayek, Mises, Beer, Cockshott, Georgescu-Roegen, Daly, Banks) now carry author-year citations; previously uncited bibliography entries now cited where they support the text (Molenaar et al. 2009, Scott et al. 2010, Varela et al. 1991, Friston 2010, Hyams 2003, Nissen et al. 1993, Stern 2011, Epstein 2005, Arrighi 1994, Srnicek 2017, Zuboff 2019, Simon 1971, Benkler 2006, Ostrom 1990). Baudrillard and Lyotard remain uncited, as before. Krippner's definition restated with "primarily" (his wording) in place of "increasingly".
Correction: section 11 said viability falls "in proportion to how far it is distorted". The sweep shows loss/markup rising from 0.60 (d = 0.25) to 3.14 (d = 8), so the loss is monotone and faster than linear; text corrected, and a monotonicity assertion added to allocation.py.
Grid audit: allocations were computed by 200-step bisection on the multiplier (converged, not a grid). Added water_fill_closed_form (lambda = sum p w / (B + sum s)); max abs difference from bisection 8.9e-16 over all markups, recorded as closed_form_max_abs_error; the closed form is stated in section 11. All quoted numbers verified: 4.97 (4.965855), 0.02 (0.021318), 0.26 (0.262821), 8.08 (8.0812), more than half (0.521144), 25.1 (25.1286), divergence 0.0. results.json changed only by the added field.
Figure title "Cost of a distorted price interface" replaced by "Viability loss and finance share versus finance price markup" (figure not embedded in the paper).

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
