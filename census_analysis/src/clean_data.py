import os

from pathlib import Path
from datetime import datetime as dt

import pandas as pd
import gzip


# we will use today date
today = dt.today().strftime("%d-%b-%y")


# data folder and paths
RAW_DATA_PATH = Path("../data/raw/")
INTERIM_DATA_PATH = Path("../data/interim/")
PROCESSED_DATA_PATH = Path("../data/processed/")
FINAL_DATA_PATH = Path("../data/final/")


# supporting functions
# ------------------------


def dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    else:
        print(f"{dir_path} found, skipping")


def load_data(data_path):
    """load data into a pd dataframe
    
    Args:
        data_path (path): path to the gzipped data
    """
    with gzip.open(RAW_DATA_PATH / "acs_data.dta.gz") as file:
        data = pd.read_stata(file)
        return data


def state_mask(state, df):
    """Used to select only one state
    
    Args:
        state (string): state to be masked
    
    Returns:
        df: subset of the data
    """
    mask_state = df["statefip"] == f"{state}"
    return df[mask_state].copy()


def clean_masked(df):
    df.drop(columns=["related", "raced", "hispand"], inplace=True)
    mask_household = (df["gq"] == "households under 1970 definition") | (
        df["gq"] == "additional households under 1990 definition"
    )
    return df[mask_household].copy()


def save_df(data_path, df):
    df.to_stata(f"{data_path}/state_data-{today}.dta", write_index=False)


if __name__ == "__main__":
    state = "ohio"
    raw_data = load_data(RAW_DATA_PATH)
    state_data = state_mask(state, raw_data)
    clean_state = clean_masked(state_data)
    save_df(INTERIM_DATA_PATH, clean_state)

    print(f"Completed cleaning for {state}")

