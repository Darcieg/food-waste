import pandas as pd
import great_expectations as gx
from pathlib import Path
from great_expectations.data_context import FileDataContext

# Constants
REPO_ROOT = Path(__file__).resolve().parents[2]
GE_CONTEXT_DIR = REPO_ROOT / "great_expectations"
S3_CSV_PATH = "s3://darcieg-food-pipeline/raw_data/ReFED_US_Food_Surplus_Summary.csv"

def main():
    context = FileDataContext(context_root_dir=GE_CONTEXT_DIR)

    # Load the data
    df = pd.read_csv(S3_CSV_PATH, skiprows=1)

    batch_request = context.get_datasource("refed_summary_source") \
                      .get_asset("surplus_summary") \
                      .build_batch_request(dataframe=df)

    # Get a validator
    validator = context.get_validator(batch_request=batch_request)
    df_ge = validator.active_batch.data.dataframe
    print("GE sees columns:", df_ge.columns.tolist())

    # Define expectations
    validator.expect_column_values_to_not_be_null("tons_surplus")
    validator.expect_column_values_to_be_between("tons_surplus", min_value=0)

    # Save the expectation suite to disk
    suite = validator.get_expectation_suite()
    context.save_expectation_suite(suite)

    results = validator.validate()
    print(results.to_json_dict())
    print("Validation completed successfully.")

if __name__ == "__main__":
    main()
