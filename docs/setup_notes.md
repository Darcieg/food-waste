# Setup Notes: Great Expectations Integration

**Project:** Food Waste Data Pipeline (ReFED)

**Objective:**  
Validate and monitor data quality using [Great Expectations (GX)](https://greatexpectations.io/) as part of a Python-based AWS data pipeline.

---

## 1. Initial Exploration

- Began in a Jupyter notebook with CSV data loaded into a `pandas` DataFrame.
- Attempted to use `great_expectations.dataset.PandasDataset.from_pandas(df)` — but it was unavailable or deprecated.
- Pivoted to trying the `great_expectations` CLI to initialize a project.

---

## 2. CLI Installation Issues

- GE installed via `pip install great_expectations` inside a virtual environment.
- CLI command `great_expectations` **was not available**, despite successful installation:
  - No `great_expectations.exe` in `venv/Scripts`
  - No `entry_points.txt` in `.dist-info`
  - No `__main__.py` or `cli.py` inside the installed package

---

## 3. CLI Troubleshooting Attempts

- Manually removed `great_expectations` and `ruamel.yaml` packages (which GE depends on).
- Reinstalled with `--no-cache-dir`, `--force-reinstall`, and even created a `.bat` wrapper script.
- Still got errors like:

 No module named great_expectations.main

 - Observed this issue on both Python 3.9 and 3.12 (Windows).
- Discovered this is a known issue: sometimes pip does **not generate console scripts** on Windows for certain environments, especially Python 3.12.

---

## 4. Decision: Use GE Python API Instead

To avoid CLI dependency issues, switched to using the **Great Expectations Python API**, which supports all necessary functionality:

- Initializing a project folder: `DataContext.create()`
- Loading data into memory (via `pandas`)
- Running checkpoints: `context.run_checkpoint(checkpoint_name="...")`

---

## 5. Python Script Workflow

Created a standalone Python script (`run_ge_pipeline.py`) to:
- Initialize a GE project folder if it doesn't exist
- Load food waste data from CSV into a DataFrame
- Run an existing GE checkpoint
- Print validation results

No CLI required; script can be reused and automated.

---

## 6. Environment Notes

- Used Python 3.12.3 in a virtual environment
- Updated `pip`, `setuptools`, `wheel` to latest versions
- Still experienced missing CLI script
- Recommendation: if CLI access is ever required, test in a fresh venv using Python **3.10 or 3.11**

---

## 7. Next Steps

- Define expectation suites using the Python API
- Add more checkpoints and automate validation as part of data pipeline
- Optionally generate validation reports (Data Docs) using `context.build_data_docs()`

---

