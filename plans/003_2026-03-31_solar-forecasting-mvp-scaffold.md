# Plan: Solar forecasting MVP scaffold (`solar-forecasting-mvp`)

**Source (Cursor, not in git):** `~/.cursor/plans/solar-forecasting-mvp_0554d1c0.plan.md`  
**Executed in repo:** `feat: scaffold solar forecasting project (notebooks, PVDAQ, NSRDB)` (`f808761`)

## Goal / success criteria

- Work on a feature branch with protected `main`.
- PVDAQ facility selection tooling (data-driven).
- Repo scaffold: notebooks, `src/`, README, `.env.example`, NSRDB helper with cache/retries.
- Start Act 1: load PVDAQ, QA, first plots.

## Scope

- **In:** `notebooks/`, `src/`, `scripts/compare_pvdaq_facilities.py`, `src/data/pvdaq.py`, `src/data/nsrdb.py`, `README.md`, config examples.
- **Out:** full Act 2 modeling and Act 3 business narrative (later).

## Plan body (from Cursor)

---
name: solar-forecasting-mvp
overview: Create a protected-main workflow branch, pick one PVDAQ facility using a data-driven approach, scaffold a clean Python/Jupyter repo structure, and begin Act 1 data loading plus NSRDB API setup (including obtaining/storing an API key) in a reproducible way.
todos:
  - id: branch-off-main
    content: Create a feature branch from `main` and push it to origin.
    status: completed
  - id: choose-pvdaq-facility
    content: Download PVDAQ data locally, compute facility coverage stats, and pick a single facility with strongest data completeness/quality; record rationale.
    status: completed
  - id: scaffold-repo-structure
    content: Create the notebook and `src/` folder structure for the 3-act flow plus README + .env.example placeholders.
    status: completed
  - id: nsrdb-api-setup
    content: Add NSRDB key acquisition instructions and implement a cached, retrying NSRDB fetch helper wired to env vars.
    status: completed
  - id: start-act1-loading
    content: Implement initial PVDAQ loading + QA + first EDA plots in the Act 1 notebook.
    status: completed
  - id: open-pr
    content: Push branch and open a PR into `main` with summary + test plan.
    status: completed
isProject: false
---

## Starting point

- Remote: `speekerwolf/solar-power-forecasting`
- `main` is protected; use feature branches and PRs.

## What we’ll do next (high level)

- Create a feature branch off `main`.
- Download PVDAQ data locally (raw), inspect facilities, choose one facility.
- Scaffold the 3-act notebook story with reusable Python modules.
- Setup + Act 1: load PVDAQ, basic QA, first plots.
- NSRDB API setup: key in env, cached fetch helper.

## PR workflow

- Push the branch; open PR into `main` with summary, test plan, risks/follow-ups.

## Verification

- `pip install -r requirements.txt`; run `py -3 scripts/compare_pvdaq_facilities.py` with CSVs in `data/raw/`.
- Open `notebooks/00_setup.ipynb` then `01_act1_eda.ipynb`.
