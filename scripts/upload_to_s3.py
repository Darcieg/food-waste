import os
import json
import boto3
from pathlib import Path
from botocore.exceptions import ClientError

# ===== CONFIG =====
BUCKET_NAME = "darcieg-food-pipeline"
REGION = "us-west-2"
REPO_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = REPO_ROOT / "data" / "raw"
GE_SUITE_FILE = REPO_ROOT / "great_expectations" / "expectations" / "refed_summary_suite.json"
S3_CSV_PREFIX = "raw_data/"
S3_EXPECTATIONS_PREFIX = "expectations/"

# ===== INIT S3 CLIENT =====
s3 = boto3.client("s3", region_name=REGION)

# ======== HELPERS ===============
def s3_key_exists(bucket_name: str, key: str)->bool:
    try:
        s3.head_object(Bucket=bucket_name, Key=key)
        return True
    except ClientError as e:
        if e.response['Error']['Code'] == "404":
            return False
        else:
            raise


# ===== 1. Create bucket if needed =====
def create_bucket_if_not_exists(bucket_name: str)->None:
    try:
        s3.head_bucket(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' already exists.")
    except ClientError as e:
        print(f"Bucket '{bucket_name}' not found. Creating...")
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": REGION}
        )
        print(f"Bucket '{bucket_name}' created.")

# ===== 2. Upload CSV files =====
def upload_csv_files():
    for file in RAW_DATA_DIR.glob("*.csv"):
        s3_key = S3_CSV_PREFIX + file.name
        if not s3_key_exists(BUCKET_NAME, s3_key):
            print(f"Uploading {file.name} to s3://{BUCKET_NAME}/{s3_key}")
            s3.upload_file(str(file), BUCKET_NAME, s3_key)
    print("All CSV files uploaded.")

# ===== 3. Upload GE expectation suite =====
def upload_ge_suite():
    if not GE_SUITE_FILE.exists():
        print(f"Expectation suite file not found at: {GE_SUITE_FILE}")
        return
    with open(GE_SUITE_FILE, "r") as f:
        suite_json = json.load(f)

    suite_str = json.dumps(suite_json, indent=2)
    s3_key = S3_EXPECTATIONS_PREFIX + GE_SUITE_FILE.name

    print(f"Uploading GE suite to s3://{BUCKET_NAME}/{s3_key}")
    s3.put_object(Bucket=BUCKET_NAME, Key=s3_key, Body=suite_str)
    print("GE suite uploaded.")


# ===== RUN =====
if __name__ == "__main__":
    create_bucket_if_not_exists(BUCKET_NAME)
    upload_csv_files()
    upload_ge_suite()
