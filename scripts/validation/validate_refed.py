import great_expectations as gx
from great_expectations.checkpoint import Checkpoint
from pathlib import Path
import pandas as pd

# Set up paths
REPO_ROOT = Path(__file__).resolve().parents[2]
CSV_FILE = REPO_ROOT / "data" / "raw" / "ReFED_US_Food_Surplus_Summary.csv"

# Load the data
df = pd.read_csv(CSV_FILE, skiprows=1)

# Create an in-memory GE context
context = gx.get_context(mode="ephemeral")

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

results = validator.validate()

# Fail the script if expectations are not met
if not results["success"]:
    raise ValueError("Data validation failed!")
