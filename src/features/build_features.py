"""Build model features from aligned PVDAQ + NSRDB tables (Act 2)."""

from __future__ import annotations

import pandas as pd


def placeholder_features(frame: pd.DataFrame) -> pd.DataFrame:
    """Return ``frame`` unchanged until Act 2 joins are implemented."""
    return frame.copy()
