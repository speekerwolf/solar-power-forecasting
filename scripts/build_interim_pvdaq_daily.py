"""Build a canonical PVDAQ daily dataset in data/interim/ from raw PVDAQ chunks.

Raw PVDAQ downloads remain in data/raw/ (immutable). This script produces a single
derived table suitable for notebooks/models.

This script is intentionally dependency-light (stdlib only) so it can run even
before you set up the Python environment.
"""

from __future__ import annotations

import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main() -> None:
    system_id = 11797
    raw_dir = ROOT / "data" / "raw" / "pvdaq" / f"system_id={system_id}"
    interim_dir = ROOT / "data" / "interim"
    manifests_dir = ROOT / "data" / "manifests"
    interim_dir.mkdir(parents=True, exist_ok=True)
    manifests_dir.mkdir(parents=True, exist_ok=True)

    paths = sorted(raw_dir.glob("*.csv"))
    if not paths:
        raise FileNotFoundError(f"No CSV files found in {raw_dir}")

    # Input files have a blank first column header which holds the date.
    # We'll normalize it to a real `date` column and add `system_id`.
    out_path = interim_dir / f"pvdaq_{system_id}_daily.csv"
    fieldnames: list[str] | None = None

    date_min: str | None = None
    date_max: str | None = None
    row_count = 0

    with out_path.open("w", newline="", encoding="utf-8") as out_f:
        writer: csv.DictWriter[str] | None = None

        for p in paths:
            with p.open("r", newline="", encoding="utf-8") as in_f:
                reader = csv.DictReader(in_f)
                if reader.fieldnames is None:
                    continue

                # First column is blank header -> maps to "" key in DictReader.
                # Normalize to `date`.
                metric_fields = [c for c in reader.fieldnames if c and c.strip() != ""]
                current_fields = ["date", "system_id", *metric_fields]
                if fieldnames is None:
                    fieldnames = current_fields
                    writer = csv.DictWriter(out_f, fieldnames=fieldnames)
                    writer.writeheader()
                else:
                    if current_fields != fieldnames:
                        raise ValueError(
                            "Inconsistent columns across raw chunks. "
                            f"Expected {fieldnames} but got {current_fields} from {p.name}."
                        )

                assert writer is not None
                for row in reader:
                    d = (row.get("") or "").strip()
                    if not d:
                        continue
                    if date_min is None or d < date_min:
                        date_min = d
                    if date_max is None or d > date_max:
                        date_max = d

                    out_row: dict[str, str] = {"date": d, "system_id": str(system_id)}
                    for f in metric_fields:
                        out_row[f] = (row.get(f) or "").strip()
                    writer.writerow(out_row)
                    row_count += 1

    manifest = {
        "dataset": "pvdaq_daily_aggregate",
        "system_id": system_id,
        "raw_input_dir": str(raw_dir.as_posix()),
        "raw_files": sorted(p.name for p in raw_dir.glob("*.csv")),
        "output_file": str(out_path.as_posix()),
        "row_count": row_count,
        "date_min": date_min,
        "date_max": date_max,
        "built_at_utc": datetime.now(timezone.utc).isoformat(),
        "columns": fieldnames,
    }
    manifest_path = manifests_dir / f"pvdaq_{system_id}_daily.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"Wrote {out_path} ({out_path.stat().st_size} bytes)")
    print(f"Wrote {manifest_path}")


if __name__ == "__main__":
    main()

