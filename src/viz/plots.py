"""Publication-style plots for the portfolio notebook."""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def set_plot_style() -> None:
    """Apply a consistent seaborn theme."""
    sns.set_theme(style="whitegrid", context="talk")


def plot_daily_median_profile(
    frame: pd.DataFrame,
    *,
    ts_col: str = "_ts",
    value_col: str = "_target",
    ax: plt.Axes | None = None,
) -> plt.Axes:
    """Median generation by hour-of-day (local time of index)."""
    set_plot_style()
    df = frame[[ts_col, value_col]].dropna().copy()
    df["hour"] = df[ts_col].dt.hour
    if ax is None:
        _, ax = plt.subplots(figsize=(10, 5))
    med = df.groupby("hour")[value_col].median()
    med.plot(ax=ax, marker="o")
    ax.set_xlabel("Hour of day")
    ax.set_ylabel("Median output")
    ax.set_title("Median daily profile")
    return ax
