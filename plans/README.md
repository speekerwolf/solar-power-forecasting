# Plans

Save **project planning documents** here (implementation plans, milestones, decision logs).

## What to put here

- Markdown exports or copies of planning docs you want versioned with the repo
- Short notes on scope, open questions, and next steps for each phase

## Cursor IDE vs this repo

Cursor keeps its own Planning Mode plans on your machine (for example under your user `.cursor/plans/`). Those files are **not** automatically part of git.

This `plans/` directory is the **versioned** copy: anything you want in PR history, on GitHub, or shared with collaborators should live here.

Use the naming convention from `.cursor/rules/planning-mode-save-plans.mdc`:

`plans/NNN_YYYY-MM-DD_<short-indicative-slug>.md`

After you execute a plan in Cursor, copy or export the final markdown into `plans/` with the next `NNN`.
