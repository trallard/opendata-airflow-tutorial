import gzip
import os
from datetime import datetime as dt
from pathlib import Path

import pandas as pd

# data folder and paths
RAW_DATA_PATH = Path("../data/raw/")
INTERIM_DATA_PATH = Path("../data/interim/")
PROCESSED_DATA_PATH = Path("../data/processed/")
FINAL_DATA_PATH = Path("../data/final/")


# analysis methods


def load_data(date):
    data = pd.read_stata(INTERIM_DATA_PATH / f"working_data-{date}.dta")

    return data


def drop_rows(data):
    """Drop observations where pernum does not equal 1
    """
    mask_pernum = data["pernum"] == 1
    return data[mask_pernum].copy()


def define_groups(data):
    mask_latino = data["hispan"] != "not hispanic"
    mask_white = (data["hispan"] == "not hispanic") & (data["race"] == "white")
    mask_black = (data["hispan"] == "not hispanic") & (
        data["race"].str.contains("black")
    )
    mask_native = (data["hispan"] == "not hispanic") & (
        data["race"] == "american indian or alaska native"
    )
    mask_API = (data["hispan"] == "not hispanic") & (
        (data["race"] >= "chinese")
        & (data["race"] <= "other asian or pacific islander")
    )
    mask_other = (data["hispan"] == "not hispanic") & (
        data["race"] >= "other race, nec"
    )

    data.loc[mask_latino, "racen"] = "Latino"
    data.loc[mask_white, "racen"] = "White"
    data.loc[mask_black, "racen"] = "Black/African-American"
    data.loc[mask_native, "racen"] = "Am. Indian / Alaska Native"
    data.loc[mask_API, "racen"] = "Asian / Pacific Islander"
    data.loc[mask_other, "racen"] = "other"

    return data


def analyse_data(data):
    cihispeed_by_racen = data.groupby(["racen", "cihispeed"])[["hhwt"]].sum()
    households_by_racen = data.groupby("racen")[["hhwt"]].sum()

    shares_cihispeed_by_racen = cihispeed_by_racen / households_by_racen
    shares_cihispeed_by_racen = shares_cihispeed_by_racen.reset_index()

    mask_yes_cihispeed = (
        shares_cihispeed_by_racen["cihispeed"]
        == "yes (cable modem, fiber optic or dsl service)"
    )

    return shares_cihispeed_by_racen[mask_yes_cihispeed]


if __name__ == "__main__":

    date = dt.today().strftime("%d-%b-%y")
    raw_data = load_data(date)
    data = drop_rows(raw_data)
    data_groups = define_groups(data)
    speed_data = analyse_data(data_groups)
    speed_data.to_csv(f"{FINAL_DATA_PATH}/{date}-internet-speed.csv", "r")
