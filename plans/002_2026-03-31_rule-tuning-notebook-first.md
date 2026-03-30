# Plan: Rule tuning + forecasting splits (`rule-tuning`)

**Source (Cursor, not in git):** `~/.cursor/plans/rule-tuning_ce419a7d.plan.md`  
**Executed in repo:** `.cursor/rules/time-series-forecasting-splits.mdc` and scoped GitHub-related rules (see git history)

## Goal / success criteria

- Keep GitHub/code-quality Cursor rules from dominating notebook work.
- Add a time-series forecasting rule with leakage-safe splits and PVDAQ–NSRDB alignment checks.

## Scope

- **In:** `globs` on selected `.mdc` files; new `time-series-forecasting-splits.mdc`.
- **Out:** application code.

## Plan body (from Cursor)

---
name: rule-tuning
overview: Tune your Cursor rules for a notebook-first solar forecasting workflow by scoping the GitHub/code-quality rules away from notebooks, and add a dedicated time-series forecasting + leakage prevention rule.
todos:
  - id: scope-github-globs
    content: Edit `github-code-quality.mdc`, `github-instructions.mdc`, and `git-conventional-commit-messages.mdc` to reduce `globs` so they apply to `**/*.md` (and optionally `.github/**/*.yml|yaml`) rather than `**/*`.
    status: completed
  - id: add-forecasting-rule
    content: Add `time-series-forecasting-splits.mdc` with a leakage-safe, time-aware forecasting split checklist; scope it to `**/*.{py,ipynb}`.
    status: completed
  - id: verify-rule-selection
    content: Sanity-check that notebook work triggers forecasting rules but not the GitHub/code-quality strict rules (by opening relevant files and observing Cursor behavior).
    status: completed
isProject: false
---

## Goals

- Make GitHub/code-quality rules apply mainly when you’re editing docs/config for GitHub/PR/CI, not while exploring/writing notebooks.
- Add a forecasting-focused rule that enforces time-aware splits and leakage-safe feature construction for solar forecasting.

## Changes to make

### 1) Scope down GitHub/code-quality rules during notebook work

Update the `globs` in these rules so they don’t apply to your Python notebooks/code by default:

- `.cursor/rules/github-code-quality.mdc`
- `.cursor/rules/github-instructions.mdc`
- `.cursor/rules/git-conventional-commit-messages.mdc`

Rationale: avoid extra strictness while doing notebook EDA/modeling.

### 2) Add a forecasting-focused rule

Add `.cursor/rules/time-series-forecasting-splits.mdc` with `globs: "**/*.{py,ipynb}"` and checklist for splits, leakage, evaluation metrics, reproducibility.

## Testing/verification

- Open a Python file and an `.ipynb` and confirm rule behavior matches intent.
- Optionally lint the `.mdc` files.
