## 🧐 THE QUEST: Validating Food Waste Data with Great Expectations

### ⚔️ The Battle Begins (v1.5.4 Woes)

You started by trying to validate a DataFrame using Great Expectations (GE) with version **1.5.4**, relying on the official docs.

But:

* The **CLI refused to install** cleanly.
* The **Python API examples didn’t work**.
* You hit errors like:

  ```
  PandasDatasource.add_dataframe_asset() got an unexpected keyword argument 'dataframe'
  ```

Why? Because you were following **docs for v0.18.x**, but had **v1.5.4 installed**, which introduced major breaking changes.

---

### 🛠️ Fixing the Version Mismatch

You uninstalled 1.5.4 and **installed GE 0.18.11**, the latest version compatible with the docs and stable API.

After that:

* `add_dataframe_asset(...)` worked
* You successfully created an ephemeral `context`

But you hit another issue...

---

### 😵 The “Column Does Not Exist” Mystery

GE kept saying:

```
The column "tons_surplus" in BatchData does not exist.
```

Even though you verified in a Jupyter notebook that the column **did exist**.

**Root cause:** The CSV had a descriptive header row, so you had to load it like this:

```python
pd.read_csv(CSV_FILE, skiprows=1)
```

Once that was fixed, GE recognized the column.

---

### ️❓ Next Boss: Checkpoint Constructor Error

You then ran into this:

```
TypeError: Checkpoint.__init__() got an unexpected keyword argument 'context'
```

Turns out:

* In **v0.18.11**, Checkpoints are no longer instantiated with `context` and `validator` directly.
* Instead, **you validate directly via**:

  ```python
  validator.validate()
  ```

---

### ✅ Final Fix & Victory

You simplified the flow to avoid Checkpoints and just ran:

```python
results = validator.validate()
```

And the validation worked — metrics calculated, expectations passed, data validated 🎉

---

### 🏑 Final Working Setup

* Great Expectations version: **0.18.11**
* GE context: **ephemeral**, no CLI
* CSV fix: **`skiprows=1`** to remove metadata row
* Validation: **direct call to `validator.validate()`**
* Outcome: **Success!**

---

### 🎉 What You Gained

* A working data validation pipeline using GE
* Deeper understanding of GE versioning, APIs, and error tracing
* Confidence in debugging GE’s layers, from context to validator
* A complete working script that runs standalone — no CLI needed
