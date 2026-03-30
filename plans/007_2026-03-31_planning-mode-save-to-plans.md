# Plan: Save Planning Mode plans into `plans/` (numbered filenames)

**Source:** executed in repo (Cursor rule).  
**Commit:** `chore(cursor): save plans to plans folder` (`a8e351d`)

## Goal / success criteria

- Whenever execution starts from a Planning Mode plan, the final plan is saved under `plans/` **before** code changes.
- Filenames use `NNN_YYYY-MM-DD_<slug>.md` with monotonic `NNN`.

## Scope

- **In:** `.cursor/rules/planning-mode-save-plans.mdc` (`alwaysApply: true`).
- **Out:** Cursor product UI changes (rules only describe agent behavior).

## Steps implemented

- Add rule describing required behavior, filename convention, and minimum plan sections.

## Verification

- New work from Planning Mode produces a matching `plans/NNN_*.md` file in the same PR as the implementation when possible.
