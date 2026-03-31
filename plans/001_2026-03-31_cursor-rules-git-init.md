# Plan: Cursor rules + git init (`cursor-rules`)

**Source (Cursor, not in git):** `~/.cursor/plans/cursor-rules_742c4aed.plan.md`  
**Executed in repo:** initial rules + `chore: initial commit` (`c126082`)

## Goal / success criteria

- Choose appropriate Cursor rule templates for a Python/Jupyter solar forecasting project.
- Add `.cursor/rules/*.mdc` files and initialize git with a sensible `.gitignore`.

## Scope

- **In:** rule selection from [awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules), project-specific API/data guidance, repo bootstrap.
- **Out:** full application code (came in later plans).

## Plan body (from Cursor)

---
name: cursor-rules
overview: Select the most relevant rule templates from `awesome-cursorrules`, adapt them for your Python/Jupyter solar-forecasting project, and prepare a small set of Cursor rules under `.cursor/rules/`. Then initialize a Git repo after the rules are in place.
todos:
  - id: select-templates
    content: "Confirm the template set: skip `Database and API` verbatim templates; use Python/Pandas/Documentation templates as base; define one custom NSRDB API ingestion rule checklist."
    status: completed
  - id: create-mdc-rules
    content: Create 3 `.cursor/rules/*.mdc` files implementing the proposed standards, with globs that apply to `**/*.py` and `**/*.ipynb`.
    status: completed
  - id: init-git
    content: Initialize a git repo in the project root and add a sensible `.gitignore` for Python/Jupyter plus a local data-cache folder.
    status: completed
isProject: false
---

## Decision: what to use from `awesome-cursorrules`

### Directly from `Database and API`

- The repo’s `Database and API` section contains only:
  - `GraphQL (Apollo Client)`
  - `TypeScript (Axios)`
  These don’t map cleanly to your Python client-side NSRDB API usage (REST/HTTP + `requests`-style flows), so I recommend not copying them verbatim. Cite: [awesome-cursorrules#database-and-api](https://github.com/PatrickJS/awesome-cursorrules#database-and-api).

### Better approach (recommended)

Use Python/data-science-focused templates from other sections as the base for your rules, and create one custom API ingestion rule for NSRDB/PVDAQ:

- General Python quality: `Python Best Practices` / `Python Developer`
- Data/ML pipeline structure: `Pandas (scikit-learn Guide)`
- Notebook/documentation tone: `How-To Documentation`
- Custom (project-specific): an NSRDB API client rule emphasizing caching, timezones, retries/timeouts, and reproducibility.

## Proposed deliverables (rule set)

- `.cursor/rules/python-ml-standards.mdc` (later superseded by verbatim copies; see repo history)
  - Apply on `**/*.py` and `**/*.ipynb`
- `.cursor/rules/api-data-ingestion.mdc`
  - Apply on `**/*.py` and `**/*.ipynb`
- `.cursor/rules/documentation-and-storytelling.mdc`
  - Apply on `**/*.ipynb` and `**/*.py`

## Git repo initialization

After the `.mdc` rules are created, initialize a Git repo at the project root, and add a baseline `.gitignore` for typical Python/Jupyter artifacts (`.ipynb_checkpoints/`, `__pycache__/`, local data caches, etc.).

## Verification

- `git status` shows expected new files; initial commit on `main`.
