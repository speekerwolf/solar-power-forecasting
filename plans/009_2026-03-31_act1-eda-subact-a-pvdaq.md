# Act 1 EDA — Sub‑act A (PVDAQ-only)

Source plan (Cursor): `act1-eda-brainstorm_e1900dd1.plan.md`

## EDA intent (exploration-first)

- **Primary goal**: learn to understand the data (schema, units, time index/timezone, cadence, coverage, missingness, quirks).
- **Secondary goal**: notice emerging patterns worth investigating later.
- **After this sub‑act**: summarize insights + open questions.\n+- **No decisions/solutions yet** (save those for Act 2).

## Current reality check

- Our current PVDAQ pull for `system_id=11797` is **daily aggregates** (median interval \(1440\) minutes), not 15‑minute.\n+- We will still start PVDAQ EDA now (daily), and treat **15‑minute ingestion** as the next PVDAQ milestone once we locate the correct OEDI prefix for sub‑daily PVDAQ.

## Sub‑act template stages

- **Stage 1 — Snapshot table**: coverage, cadence, missingness %, duplicates, available columns
- **Stage 2 — Sanity plots**: distribution, seasonality, typical profile
- **Stage 3 — Data issues**: gaps/outliers; PV quirks (clipping proxies, night leakage if sub‑daily)
- **Stage 4 — Insights recap**: 3–5 bullets (observations/hypotheses/open questions)

## Steps to implement (PVDAQ-only)

### 1) Canonical dataset (derived)

- Inputs (raw, immutable): `data/raw/pvdaq/system_id=11797/*.csv`
- Output (derived, gitignored): `data/interim/pvdaq_11797_daily.csv` (or Parquet later)
- Manifest (tracked): `data/manifests/pvdaq_11797_daily.json`

### 2) Stage 1 — Snapshot table

Compute and display:
- start/end timestamps
- expected vs actual cadence
- missing days (and longest gap)
- duplicate timestamps
- per-column missingness

### 3) Stage 2 — Sanity plots

For both target candidates:
- `ac_power_*_daily_mean` (power proxy)\n+- `ac_energy_*_daily_sum` (daily energy)

Plots:
- time series line (with rolling median)\n+- histogram/KDE\n+- monthly boxplots\n+- year-over-year seasonal overlay (if enough years)

### 4) Stage 3 — Data issues

- gap visualizations (missing-days timeline)\n+- outlier days (top/bottom quantiles)\n+- simple clipping proxy (e.g., high daily max with low energy, as a hypothesis)\n+
Record hypotheses; do not pick fixes yet.

### 5) Stage 4 — Insights recap (PVDAQ)

End the PVDAQ sub‑act with:\n+- “What we learned” bullets\n+- “Open questions” bullets\n+- “Risks/caveats” bullets

## Verification

- Run `notebooks/01_act1_eda.ipynb` end-to-end with the `.venv` kernel.\n+- Ensure re-running the canonical build leaves `data/manifests/pvdaq_11797_daily.json` unchanged (deterministic manifest).

