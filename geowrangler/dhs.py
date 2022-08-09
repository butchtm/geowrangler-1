# AUTOGENERATED! DO NOT EDIT! File to edit: ../notebooks/04_dhs_data.ipynb.

# %% auto 0
__all__ = ['get_approximate_col_name', 'generate_dhs_cluster_data']

# %% ../notebooks/04_dhs_data.ipynb 4
from typing import List

import geopandas as gpd
import pandas as pd

# %% ../notebooks/04_dhs_data.ipynb 5
def get_approximate_col_name(columns: List[str], col_name: str):
    """Get the approximate name of a column from a colname"""
    query_set = set(col_name.split())
    most_likely_column = next(
        (col for col in columns if query_set.issubset(set(col.lower().split()))), None
    )
    if most_likely_column is None:
        raise IndexError(f"Could not find {col_name} in {columns}")
    return most_likely_column

# %% ../notebooks/04_dhs_data.ipynb 6
def generate_dhs_cluster_data(household_data: str, gps_coordinates: str):
    # Read stata file and rename files
    dhs_reader = pd.read_stata(
        household_data, convert_categoricals=False, iterator=True
    )
    dhs_dict = dhs_reader.variable_labels()
    with dhs_reader:
        dhs_df = dhs_reader.read()
    dhs_df.rename(columns=dhs_dict, inplace=True)
    # Due to each file having different column names we get each approximate col name for cluster and wealth index
    cluster_col_name = get_approximate_col_name(dhs_df.columns, "cluster")
    wealth_col_name = get_approximate_col_name(dhs_df.columns, "wealth index factor")
    summarized = (
        dhs_df[[wealth_col_name, cluster_col_name]].groupby(cluster_col_name).mean()
    )
    summarized.reset_index(inplace=True)
    summarized.columns = ["DHSCLUST", "Wealth Index"]
    dhs_shp = gpd.read_file(gps_coordinates)
    survey_geo = pd.merge(summarized, dhs_shp, on="DHSCLUST")
    return survey_geo
