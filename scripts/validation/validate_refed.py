import great_expectations as gx
from pathlib import Path
import pandas as pd
from great_expectations.data_context import FileDataContext

# Set up paths
REPO_ROOT = Path(__file__).resolve().parents[2]
CSV_FILE = REPO_ROOT / "data" / "raw" / "ReFED_US_Food_Surplus_Summary.csv"

# Load the data
df = pd.read_csv(CSV_FILE, skiprows=1)

# Create a persistent GE context
context = FileDataContext(context_root_dir=REPO_ROOT / "great_expectations")

# Add a Pandas datasource
data_source = context.sources.add_pandas(name="refed_summary_source")

# Register the DataFrame as an asset
asset = data_source.add_dataframe_asset(name="surplus_summary")

# Build a batch request for validation
batch_request = asset.build_batch_request(dataframe=df)

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
