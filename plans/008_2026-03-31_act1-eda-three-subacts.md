# Act 1 EDA: three sub-acts (PVDAQ, NSRDB, combined)

## Goal / success criteria

- **Primary goal (Act 1)**: explore to understand the data deeply (schema, units, time index/timezone, cadence, coverage, missingness, quirks).
- **Secondary goal**: surface emerging patterns worth investigating later.
- Produce an EDA story with **clear summary tables** and **publication-quality plots**.
- After each sub-act, write an **insights recap** (observations + hypotheses + open questions).
- **Defer decisions and solutions to Act 2** (EDA can list options but should not commit).

## Scope (in/out)

- **In**
  - Sub-act A: **PVDAQ-only** exploration
  - Sub-act B: **NSRDB-only** exploration
  - Sub-act C: **PVDAQ + NSRDB combined** (join sanity + alignment checks)
  - Canonicalized derived datasets in `data/interim/` (gitignored) and tracked manifests in `data/manifests/`
- **Out**
  - Modeling, feature engineering, and “final choices” (Act 2)
  - Business framing (Act 3)

## Common sub-act template (use for all three)

- **Stage 1 — Snapshot table**: coverage (start/end), cadence, missingness %, duplicates, key columns
- **Stage 2 — Sanity plots**: distribution, seasonality, typical profiles
- **Stage 3 — Data issues**: gaps/outliers; PV-specific checks (clipping, night leakage) where applicable
- **Stage 4 — Insights recap**: 3–5 bullets (what we learned / hypotheses / open questions)

Important: **don’t “solve” in Act 1**. Record candidate approaches, but keep commitments for Act 2.

## Sub-act A (start here): PVDAQ-only

### Data acquisition

- Identify correct PVDAQ OEDI prefix for **15-minute** time-series for the chosen `system_id`.
- Download a bounded window first (6–12 months) to validate schema/timezone quickly, then expand.
- Record keys, date coverage, and notes in `data/manifests/`.

### Canonical dataset

- Produce a deterministic canonical table (preferred Parquet; otherwise CSV) with:
  - `timestamp` (timezone-aware)
  - `system_id`
  - candidate target columns (power + energy if available)
  - optional provenance columns (source file, QC flags)

### PVDAQ EDA content

- Snapshot + missingness/gap tables
- Typical day/hour profiles (if sub-hourly), seasonal patterns, anomaly highlights
- End with PVDAQ insights recap

## Sub-act B: NSRDB-only

- Fetch and cache NSRDB for the chosen location/time range.
- EDA NSRDB variables (GHI/DNI/DHI, temp, wind) for coverage/seasonality/outliers.
- End with NSRDB insights recap.

## Sub-act C: PVDAQ + NSRDB combined

- Join on timestamp (and verify timezone + cadence alignment).
- Post-join overlap diagnostics (coverage table + missingness heatmap).
- Sanity plots (PV vs irradiance; expected relationships).
- End with combined insights recap + open questions for Act 2.

## Verification / test plan

- Run notebooks with the `.venv` kernel.
- Re-run canonicalization twice to ensure:
  - raw untouched
  - `data/interim` rebuild is deterministic
  - `data/manifests` unchanged unless inputs change

