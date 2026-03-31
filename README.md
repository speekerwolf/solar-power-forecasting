# Solar power forecasting (portfolio)

End-to-end solar PV output forecasting using **NREL PVDAQ** plant data and **NSRDB** weather/irradiance features. The narrative is organized in three acts (EDA, modeling, business insights) with a primary Jupyter notebook story.

- **PVDAQ (OpenEI submission 4568):** [Photovoltaic Data Acquisition (PVDAQ) Public Datasets](https://data.openei.org/submissions/4568)
- **NSRDB:** [National Solar Radiation Database](https://nsrdb.nrel.gov/)

## Repository layout

| Path | Purpose |
|------|---------|
| `notebooks/` | Story notebooks (setup, Act 1–3) |
| `src/` | Reusable Python modules (data, features, models, plots) |
| `data/raw/` | Downloaded PVDAQ CSVs (gitignored) |
| `cache/` | API response cache (gitignored) |
| `config/` | Chosen facility and project config |
| `plans/` | Saved project planning docs (markdown) |
| `reports/figures/` | Exported figures for README / deck |

## Quick start

1. Create a virtual environment and install dependencies:

   ```powershell
   py -3 -m pip install --user uv
   py -3 -m uv venv
   .\.venv\Scripts\Activate.ps1
   py -3 -m uv sync
   ```

2. Copy `.env.example` to `.env` and add your **NREL API key** (see below).

3. Place PVDAQ CSV exports under `data/raw/` (see `data/raw/README.md`).

4. Pick a facility (data-driven):

   ```powershell
   py -3 scripts/compare_pvdaq_facilities.py
   ```

   This writes `config/selected_facility.yaml` with the recommended `system_id`.

5. Open Jupyter and start with `notebooks/00_setup.ipynb`, then `01_act1_eda.ipynb`.

## NSRDB API key

1. Sign up at the [NREL Developer Network](https://developer.nrel.gov/signup/).
2. Create an API key in your account dashboard.
3. Set `NREL_API_KEY` in `.env` (never commit `.env`).

The client in `src/data/nsrdb.py` reads `NREL_API_KEY`, uses timeouts/retries, and caches JSON under `cache/nsrdb/` by default.

**Note:** NSRDB requests are dataset-specific; set `NSRDB_BASE_URL` in `.env` if you point at a particular NSRDB API endpoint from the [developer docs](https://developer.nrel.gov/docs/solar/nsrdb/).

## Git workflow

`main` is protected: use feature branches and pull requests. See `.cursor/rules/git-branch-protection-pr-workflow.mdc` for the expected workflow.

## License

Use of PVDAQ and NSRDB data is subject to their respective terms and attribution requirements.
