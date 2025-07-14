# ☁️ Cloud Upload Log – Sustainable Ag Data Pipeline

**Date:** July 9, 2025  
**User:** Darcie Gurley  
**Project:** `sustainable-ag-data-pipeline`  
**Bucket:** `darcieg-food-pipeline` (Region: `us-west-2`)

---

## ✅ What Was Uploaded

### 📁 Raw Data Files

Uploaded from:  
`data/raw/`

Uploaded to:  
`s3://darcieg-food-pipeline/raw_data/`

Files:
- `ReFED_US_Food_Surplus_Cause_Summary.csv` (1.9 MB)
- `ReFED_US_Food_Surplus_Detail.csv` (5.6 MB)
- `ReFED_US_Food_Surplus_Summary.csv` (1.7 MB)
- `ReFED_US_State_Food_Surplus_Detail.csv` (252.1 MB)
- `ReFED_US_State_Food_Surplus_Summary.csv` (85.4 MB)

---

### 📁 Expectation Suite (Great Expectations)

Saved locally via:  
`validate_refed.py` (using `FileDataContext`)  

Expectation suite filename:  
`refed_summary_suite.json`  

Uploaded to S3 key:  
`s3://darcieg-food-pipeline/expectations/refed_summary_suite.json`

---

## 🧹 Cleanup Performed

- Deleted legacy/test buckets:
  - `darcie-test-bucket-123`
  - `aws-glue-assets-022269453456-us-west-2`
- Confirmed only **active** bucket is:  
  `darcieg-food-pipeline`

---

## 🛠 Next Steps

- [ ] Create expectation suites for:
  - `refed_detail`
  - `state_summary`
  - `state_detail`
  - `cause_summary`
- [ ] Prepare Python 3.10 environment for AWS Glue compatibility
- [ ] Package validation as a Glue job
- [ ] Automate upload + validation for incoming data

---

_This log tracks key data assets and validation resources as they move into cloud infrastructure. Add one entry per milestone._
