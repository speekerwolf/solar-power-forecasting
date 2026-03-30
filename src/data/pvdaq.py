"""Load and quality-check PVDAQ CSV exports."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


TIME_CANDIDATES: tuple[str, ...] = (
    "utc_measured_on",
    "measured_on",
    "timestamp",
    "time",
    "datetime",
    "date",
)
SYSTEM_CANDIDATES: tuple[str, ...] = ("system_id", "system", "site_id")
POWER_CANDIDATES: tuple[str, ...] = (
    "ac_power",
    "power",
    "dc_power",
    "pac",
    "value",
)


@dataclass(frozen=True)
class FacilityStats:
    """Summary statistics for one PVDAQ system in a dataframe."""

    system_id: Any
    row_count: int
    time_start: pd.Timestamp | None
    time_end: pd.Timestamp | None
    median_interval_minutes: float | None
    pct_missing_target: float
    longest_gap_hours: float | None


def _first_existing_column(df: pd.DataFrame, candidates: tuple[str, ...]) -> str | None:
    for col in candidates:
        if col in df.columns:
            return col
    return None


def load_pvdaq_csv(path: Path | str, *, timezone: str | None = "UTC") -> pd.DataFrame:
    """Load a PVDAQ CSV and normalize timestamp + system id + target column.

    Parameters
    ----------
    path:
        Path to CSV.
    timezone:
        If set, timestamps are localized or converted to this timezone-aware index.
    """
    path = Path(path)
    df = pd.read_csv(path)
    df.columns = [str(c).strip() for c in df.columns]

    time_col = _first_existing_column(df, TIME_CANDIDATES)
    if time_col is None:
        raise ValueError(
            f"No time column found. Expected one of {TIME_CANDIDATES}. Columns: {list(df.columns)}"
        )

    ts = pd.to_datetime(df[time_col], utc=True, errors="coerce")
    df = df.assign(_ts=ts).dropna(subset=["_ts"])
    if timezone:
        df["_ts"] = df["_ts"].dt.tz_convert(timezone)

    sys_col = _first_existing_column(df, SYSTEM_CANDIDATES)
    if sys_col is None:
        df["_system_id"] = Path(path).stem
    else:
        df = df.rename(columns={sys_col: "_system_id"})

    power_col = _first_existing_column(df, POWER_CANDIDATES)
    if power_col is None:
        df["_target"] = np.nan
    else:
        df = df.rename(columns={power_col: "_target"})
        df["_target"] = pd.to_numeric(df["_target"], errors="coerce")

    out = df.sort_values("_ts").reset_index(drop=True)
    return out


def compute_facility_stats(frame: pd.DataFrame) -> FacilityStats:
    """Compute coverage stats for a normalized PVDAQ frame."""
    if frame.empty:
        return FacilityStats(
            system_id=None,
            row_count=0,
            time_start=None,
            time_end=None,
            median_interval_minutes=None,
            pct_missing_target=100.0,
            longest_gap_hours=None,
        )

    system_id = frame["_system_id"].iloc[0]
    row_count = len(frame)
    time_start = frame["_ts"].min()
    time_end = frame["_ts"].max()

    diffs = frame["_ts"].diff().dropna()
    median_interval_minutes = (
        float(diffs.median().total_seconds() / 60.0) if not diffs.empty else None
    )

    if "_target" in frame.columns:
        pct_missing_target = float(frame["_target"].isna().mean() * 100.0)
    else:
        pct_missing_target = 100.0

    gap_seconds = diffs.dt.total_seconds()
    longest_gap_hours = float(gap_seconds.max() / 3600.0) if not gap_seconds.empty else None

    return FacilityStats(
        system_id=system_id,
        row_count=row_count,
        time_start=time_start,
        time_end=time_end,
        median_interval_minutes=median_interval_minutes,
        pct_missing_target=pct_missing_target,
        longest_gap_hours=longest_gap_hours,
    )


def score_facility(stats: FacilityStats) -> float:
    """Higher is better for ranking candidate facilities."""
    if stats.row_count == 0:
        return -np.inf
    span_days = 0.0
    if stats.time_start is not None and stats.time_end is not None:
        span_days = (stats.time_end - stats.time_start).total_seconds() / 86400.0
    missing_penalty = stats.pct_missing_target
    gap_penalty = 0.0 if stats.longest_gap_hours is None else min(stats.longest_gap_hours, 168.0)
    return span_days * np.log1p(stats.row_count) - missing_penalty - 0.1 * gap_penalty


def load_all_raw_csvs(raw_dir: Path | str) -> dict[Any, pd.DataFrame]:
    """Load every CSV under ``data/raw`` into normalized frames keyed by system id."""
    raw_dir = Path(raw_dir)
    frames: dict[Any, pd.DataFrame] = {}
    for csv_path in sorted(raw_dir.glob("*.csv")):
        df = load_pvdaq_csv(csv_path)
        for sid, group in df.groupby("_system_id", sort=False):
            chunk = group.sort_values("_ts").reset_index(drop=True)
            if sid in frames:
                frames[sid] = (
                    pd.concat([frames[sid], chunk], ignore_index=True)
                    .sort_values("_ts")
                    .reset_index(drop=True)
                )
            else:
                frames[sid] = chunk
    return frames
