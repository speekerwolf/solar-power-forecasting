# Plan: Versioned `plans/` directory

**Source:** executed in repo (documentation layout).  
**Commit:** `docs: add plans folder for saved project plans` (`9661f64`)

## Goal / success criteria

- Provide a dedicated folder in git for planning artifacts, separate from Cursor’s local plan storage.

## Scope

- **In:** `plans/README.md`, README layout table row for `plans/`.
- **Out:** migrating existing Cursor plans automatically (manual copy/export).

## Steps implemented

- Add `plans/README.md` describing purpose.
- Link `plans/` in `README.md` repository layout.

## Verification

- `plans/` exists and is tracked; contributors know to copy Cursor plans here for version history.
