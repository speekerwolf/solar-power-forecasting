# Plan: Protected `main` + PR workflow rules

**Source:** executed in repo (no separate Cursor `.plan.md` file in the saved set); aligns with branch protection on GitHub.  
**Commit:** `chore(rules): align with protected main PR workflow` (`83b027a`)

## Goal / success criteria

- Document and enforce: no direct commits to `main`, feature branches, Conventional Commits, PR descriptions with test plan.
- Keep GitHub-oriented rules scoped to markdown / `.github` workflows where appropriate.

## Scope

- **In:** `.cursor/rules/git-branch-protection-pr-workflow.mdc` (always on); updates to `github-code-quality.mdc`, `github-instructions.mdc`, `git-conventional-commit-messages.mdc` globs.
- **Out:** application code.

## Steps implemented

- Add always-on rule for feature branches + PR requirements.
- Scope strict GitHub helper rules to `**/*.md` and `**/.github/**/*.{yml,yaml}` (see commit diff).

## Verification

- Rule files present under `.cursor/rules/`.
- Team follows PR workflow when merging to `main`.
