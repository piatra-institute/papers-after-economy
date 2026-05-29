"""Allocation under constraint, with and without a price interface.

The paper's claim is structural: allocation under viability constraint is the
deep operation; price is a late commensuration *interface* layered on top, not
the substrate. This model instruments that claim.

A system divides a fixed budget B across sectors, each with concave viability
returns V_i(x) = w_i log(1 + x/s_i). Three coordinators allocate the same budget:

  1. constraint    — maximise total viability directly under the budget
                     constraint (the cell/organism case: cost, no price). This
                     is the optimum, by water-filling on marginal viability.
  2. faithful price — a price system whose prices carry no distortion (p_i = 1).
                     It reproduces the constraint optimum exactly: price as a
                     transparent interface.
  3. financialised  — the same price system, but one sector (finance) carries a
                     speculative markup p = 1 + d. The allocator now maximises
                     price-weighted return sum p_i V_i, over-allocating to the
                     marked-up sector and losing true viability.

Faithful price recovers the optimum; financialised price diverges from it. The
gap is the viability cost of letting a distorted price interface stand in for
the allocation it was meant to coordinate. The numbers are facts about this
model's geometry, not measurements of any real economy.
"""
from __future__ import annotations

import numpy as np

# Sectors and their TRUE viability parameters. Weights are real contribution to
# system viability; scales set diminishing-returns onset. Finance has a modest
# true weight — it coordinates, it does not itself sustain — yet it is the
# sector that attracts the speculative price markup.
SECTORS = ["subsistence", "infrastructure", "care", "knowledge", "ecology", "finance"]
W = np.array([1.00, 0.80, 0.70, 0.60, 0.90, 0.30])
S = np.array([0.50, 0.50, 0.50, 0.50, 0.50, 0.50])
BUDGET = 6.0
FINANCE = SECTORS.index("finance")


def water_fill(prices: np.ndarray, budget: float = BUDGET,
               w: np.ndarray = W, s: np.ndarray = S) -> np.ndarray:
    """Allocation that maximises sum_i prices_i * w_i log(1 + x_i/s_i) s.t.
    sum x_i = budget, x_i >= 0. FOC: prices_i w_i /(s_i + x_i) = lambda, so
    x_i = max(0, prices_i w_i / lambda - s_i). Bisect lambda (total is
    monotonically decreasing in lambda)."""
    ew = prices * w
    lo, hi = 1e-9, ew.max() / s.min() * 10 + 1.0

    def total(lam):
        return np.maximum(0.0, ew / lam - s).sum()

    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if total(mid) > budget:
            lo = mid
        else:
            hi = mid
    lam = 0.5 * (lo + hi)
    return np.maximum(0.0, ew / lam - s)


def true_viability(x: np.ndarray, w: np.ndarray = W, s: np.ndarray = S) -> float:
    return float(np.sum(w * np.log1p(x / s)))


def prices_with_distortion(d: float) -> np.ndarray:
    p = np.ones(len(SECTORS))
    p[FINANCE] = 1.0 + d
    return p


def allocate(d: float):
    """Return (allocation, true_viability, finance_share) under finance markup d."""
    x = water_fill(prices_with_distortion(d))
    return x, true_viability(x), float(x[FINANCE] / x.sum())


def run(distortion_ref: float = 3.0,
        sweep=(0.0, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0)) -> dict:
    # constraint optimum == faithful price (d = 0)
    x_opt = water_fill(np.ones(len(SECTORS)))
    v_opt = true_viability(x_opt)

    x_ref, v_ref, fin_ref = allocate(distortion_ref)

    sweep_rows = []
    for d in sweep:
        x, v, fin = allocate(d)
        sweep_rows.append({
            "distortion": float(d),
            "viability": round(v, 6),
            "viability_loss_pct": round(100.0 * (v_opt - v) / v_opt, 4),
            "finance_share": round(fin, 6),
        })

    def alloc_map(x):
        return {sec: round(float(v), 6) for sec, v in zip(SECTORS, x)}

    return {
        "sectors": SECTORS,
        "budget": BUDGET,
        "true_weights": {s: round(float(w), 3) for s, w in zip(SECTORS, W)},
        "constraint_optimum": {
            "allocation": alloc_map(x_opt),
            "viability": round(v_opt, 6),
            "note": "max total viability under the budget constraint; no prices",
        },
        "faithful_price": {
            "allocation": alloc_map(water_fill(prices_with_distortion(0.0))),
            "viability": round(true_viability(water_fill(prices_with_distortion(0.0))), 6),
            "divergence_from_optimum": round(
                v_opt - true_viability(water_fill(prices_with_distortion(0.0))), 8),
            "note": "undistorted prices reproduce the constraint optimum exactly",
        },
        "financialised": {
            "distortion": distortion_ref,
            "allocation": alloc_map(x_ref),
            "viability": round(v_ref, 6),
            "viability_loss_pct": round(100.0 * (v_opt - v_ref) / v_opt, 4),
            "finance_share": round(fin_ref, 6),
            "finance_share_optimum": round(float(x_opt[FINANCE] / x_opt.sum()), 6),
            "note": "a speculative markup on finance over-allocates to it and "
                    "loses true viability the price interface was meant to track",
        },
        "distortion_sweep": sweep_rows,
    }
