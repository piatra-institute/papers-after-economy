"""Orchestrator: reproduces every numerical claim in the paper.

    cd simulation
    uv run run_all.py

Writes output/results.json and output/figures/. Every numeric value cited in
the paper is a key in the JSON file.
"""
from __future__ import annotations

import json
from pathlib import Path

from allocation import run
from figures import plot_allocation, plot_loss

OUT = Path(__file__).parent / "output"


def main() -> None:
    (OUT / "figures").mkdir(parents=True, exist_ok=True)
    results = run()
    (OUT / "results.json").write_text(json.dumps(results, indent=2))
    plot_allocation(results["financialised"]["distortion"],
                    str(OUT / "figures" / "allocation.png"))
    plot_loss(results["distortion_sweep"], str(OUT / "figures" / "viability_loss.png"))
    fin = results["financialised"]
    print("optimum viability     :", results["constraint_optimum"]["viability"])
    print("faithful divergence   :", results["faithful_price"]["divergence_from_optimum"])
    print(f"financialised (d={fin['distortion']:g}) loss:", fin["viability_loss_pct"], "%")
    print("finance share opt->fin:", fin["finance_share_optimum"], "->", fin["finance_share"])
    print("wrote", OUT / "results.json")


if __name__ == "__main__":
    main()
