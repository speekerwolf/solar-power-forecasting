# Raw data (not tracked by git)

Place **PVDAQ** exports here. This repo expects one or more CSV files you download from the [PVDAQ public datasets on OpenEI](https://data.openei.org/submissions/4568).

## Suggested workflow

1. Download a CSV (or multiple) for candidate systems from OpenEI / PVDAQ tooling.
2. Save as e.g. `pvdaq_system_2105.csv` under this folder.
3. Run facility comparison (from repo root):

   ```powershell
   py -3 scripts/compare_pvdaq_facilities.py
   ```

4. Note the recommended `system_id` and copy it into `config/selected_facility.yaml` (see `config/selected_facility.example.yaml`).

## Column expectations

The loader in `src/data/pvdaq.py` accepts flexible column names, including:

- Time: `measured_on`, `utc_measured_on`, `timestamp`, `time`, `datetime`
- System: `system_id`
- Power / output: `ac_power`, `power`, `dc_power`, `value` (with a metric column if long-format)

If your export uses different names, adjust the mapping in `load_pvdaq_csv` or preprocess the CSV.
