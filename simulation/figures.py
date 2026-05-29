"""Figures for the after-economy allocation model."""
from __future__ import annotations

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from allocation import SECTORS, allocate, water_fill, prices_with_distortion, true_viability


def plot_allocation(distortion_ref: float, path: str) -> None:
    x_opt = water_fill(prices_with_distortion(0.0))
    x_fin, _, _ = allocate(distortion_ref)
    idx = np.arange(len(SECTORS))
    width = 0.38
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.bar(idx - width / 2, x_opt, width, label="constraint optimum (no price / faithful price)")
    ax.bar(idx + width / 2, x_fin, width,
           label=f"financialised price (finance markup d={distortion_ref:g})")
    ax.set_xticks(idx)
    ax.set_xticklabels(SECTORS, rotation=20, ha="right")
    ax.set_ylabel("budget allocated")
    ax.set_title("Allocation under constraint vs under a distorted price interface")
    ax.legend(frameon=False, fontsize=9)
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)


def plot_loss(sweep_rows, path: str) -> None:
    d = [r["distortion"] for r in sweep_rows]
    loss = [r["viability_loss_pct"] for r in sweep_rows]
    share = [100.0 * r["finance_share"] for r in sweep_rows]
    fig, ax1 = plt.subplots(figsize=(7.5, 4.2))
    ax1.plot(d, loss, "o-", color="#b2182b", label="viability loss (%)")
    ax1.set_xlabel("finance price distortion  d")
    ax1.set_ylabel("true-viability loss vs optimum (%)", color="#b2182b")
    ax1.tick_params(axis="y", labelcolor="#b2182b")
    ax2 = ax1.twinx()
    ax2.plot(d, share, "s--", color="#2166ac", label="finance budget share (%)")
    ax2.set_ylabel("finance share of budget (%)", color="#2166ac")
    ax2.tick_params(axis="y", labelcolor="#2166ac")
    ax1.set_title("Cost of a distorted price interface")
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
