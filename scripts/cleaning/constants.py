# constants.py

SHARED_COLUMNS_SURPLUS = [
    "food_type", 
    "sector", 
    "sub_sector", 
    "year",
]

# -----------------------------
# Shared Columns (for non-cause summary files)
# This is the same schema as *detail, with the addition of "tons_inedible_parts" and "tons_not_fit_for_human_consumption"
# and missing "food category"
# -----------------------------

SHARED_COLUMNS_SUMMARY = [
    "food_type", 
    "gallons_water_footprint", 
    "meals_wasted", 
    "sector", 
    "sub_sector", 
    "sub_sector_category", 
    "surplus_downstream_100_year_mtch4_footprint", 
    "surplus_downstream_100_year_mtco2e_footprint", 
    "surplus_total_100_year_mtch4_footprint", 
    "surplus_total_100_year_mtco2e_footprint", 
    "surplus_upstream_100_year_mtch4_footprint", 
    "surplus_upstream_100_year_mtco2e_footprint", 
    "tons_anaerobic_digestion", 
    "tons_animal_feed", 
    "tons_composting", 
    "tons_donations", 
    "tons_dumping", 
    "tons_incineration", 
    "tons_industrial_uses", 
    "tons_inedible_parts", 
    "tons_land_application", 
    "tons_landfill", 
    "tons_not_fit_for_human_consumption", 
    "tons_not_harvested", 
    "tons_sewer", 
    "tons_supply", 
    "tons_surplus", 
    "tons_uneaten", 
    "tons_waste", 
    "us_dollars_surplus", 
    "year",
]

SHARED_COLUMNS_DETAIL = [
    "food_category", 
    "food_type", 
    "gallons_water_footprint", 
    "meals_wasted", 
    "sector", 
    "state", 
    "sub_sector", 
    "sub_sector_category", 
    "surplus_downstream_100_year_mtch4_footprint", 
    "surplus_downstream_100_year_mtco2e_footprint", 
    "surplus_total_100_year_mtch4_footprint", 
    "surplus_total_100_year_mtco2e_footprint", 
    "surplus_upstream_100_year_mtch4_footprint", 
    "surplus_upstream_100_year_mtco2e_footprint", 
    "tons_anaerobic_digestion", 
    "tons_animal_feed", 
    "tons_composting", 
    "tons_donations", 
    "tons_dumping", 
    "tons_incineration", 
    "tons_industrial_uses", 
    "tons_land_application", 
    "tons_landfill", 
    "tons_not_harvested", 
    "tons_sewer", 
    "tons_supply", 
    "tons_surplus", 
    "tons_uneaten", 
    "tons_waste", 
    "us_dollars_surplus", 
    "year",
]

COLUMNS_SURPLUS_CAUSE = [
    "cause_group", 
    "cause_name", 
    "tons_surplus_due_to_cause", 
    "us_dollars_surplus_due_to_cause",
]

SHARED_COLUMNS_SURPLUS_AND_SOLUTIONS = [
    "food_type", 
    "sector", 
    "sub_sector", 
]

COLUMNS_SOLUTIONS_DETAIL = [
    "solution_group", 
    "solution_priority_action_area", 
    "solution_name",
    "sector", 
    "sub_sector", 
    "sub_sector_category", 
    "state", 
    "food_type",
    "annual_tons_diversion_potential",
    "annual_100_year_mtco2e_reduction_potential",
    "annual_100_year_mtch4_reduction_potential",
    "annual_gallons_water_savings_potential",
    "annual_meal_equivalents_diverted", "jobs_created",
    "annual_us_dollars_cost", "annual_us_dollars_gross_financial_benefit",
    "annual_us_dollars_net_financial_benefit",
]

COLUMNS_SOLUTIONS_SUMMARY = [
    "annual_100_year_mtch4_reduction_potential",
    "annual_100_year_mtco2e_reduction_potential",
    "annual_gallons_water_savings_potential",
    "annual_meal_equivalents_diverted",
    "annual_tons_diversion_potential",
    "annual_us_dollars_cost",
    "annual_us_dollars_gross_financial_benefit",
    "annual_us_dollars_net_financial_benefit",
    "jobs_created", 
    "solution_group", 
    "solution_name", 
    "solution_priority_action_area",
]

COLUMNS_SOLUTIONS_FINANCIAL = [
    "solution_group", 
    "solution_priority_action_area", 
    "solution_name",
    "stakeholder", 
    "annual_us_dollars_cost",
    "annual_us_dollars_gross_financial_benefit",
    "annual_us_dollars_net_financial_benefit",
]
# --------------------------
# Helper for Exploratory Data Analysis
# I used this in a Jupyter Notebook to generate the column lists in this file
# --------------------------

def get_column_overlap(*dfs):
    """Return set of shared columns across multiple DataFrames"""
    sets = [set(df.columns) for df in dfs]
    return set.intersection(*sets)

def get_column_diff(df1, df2):
    """Return columns in df1 that are not in df2"""
    return list(set(df1.columns) - set(df2.columns))