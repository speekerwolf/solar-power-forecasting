# Plan: Raw data immutability

**Source:** executed in repo (policy + Cursor rule).  
**Commit:** `chore(data): enforce raw data immutability` (`5cd8598`)

## Goal / success criteria

- Treat `data/raw/` as read-only source-of-truth; never overwrite or “fix in place” raw downloads.
- Document where derived artifacts go (`data/interim/`, `data/processed/`, `cache/`, `reports/figures/`).

## Scope

- **In:** `.cursor/rules/data-immutability.mdc`, `data/README.md`.
- **Out:** automated enforcement beyond team conventions (no pre-commit hook in this change).

## Steps implemented

- Add Cursor rule scoped to `**/*.{py,ipynb}`.
- Add human-readable data policy in `data/README.md`.

## Verification

- Notebooks and scripts only write derived outputs outside `data/raw/` (except adding new raw files as downloads).
