# Data policy

## `data/raw/` is immutable

Treat `data/raw/` as read-only: never edit, overwrite, or delete original downloaded files.

If raw data has issues (missing intervals, bad timestamps, outliers), handle it by:
- documenting the issue, and
- cleaning in code, or writing a new derived artifact elsewhere.

## Where derived data should go

- `data/interim/`: lightly cleaned, standardized schema (close to raw)
- `data/processed/`: model-ready tables/features

Raw downloads stay in `data/raw/`. API responses can be cached under `cache/`.

