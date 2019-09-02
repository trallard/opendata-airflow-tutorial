import io
from pathlib import Path
from zipfile import ZipFile

import requests

RAW_DATA_PATH = Path("data/raw/counties/")

url = "https://www2.census.gov/geo/tiger/TIGER2018/COUNTY/tl_2018_us_county.zip"
site = requests.get(url)

z = ZipFile(io.BytesIO(site.content))
z.extractall(RAW_DATA_PATH)
