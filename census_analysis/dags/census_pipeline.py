"""Airflow dag to demonstrate a simple analysis pipeline"""

import io
import os
from datetime import datetime
from datetime import timedelta
from pathlib import Path
from zipfile import ZipFile

import requests
from airflow import DAG
from airflow.operators.email_operator import EmailOperator
from airflow.operators.python_operator import PythonOperator

_dags_root = os.path.join(os.environ["HOME"], "airflow")
_data_root = os.path.join(_dags_root, "data/raw")

# Airflow-specific configs; these will be passed directly to airflow
default_args = {
    "owner": "admin",
    "depends_on_past": False,
    "start_date": datetime.now() - timedelta(days=5),
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
    "email_on_failure": False,
}

# --------------
# DAG methods
# --------------


def collect_data():
    url = "https://www2.census.gov/geo/tiger/TIGER2018/COUNTY/tl_2018_us_county.zip"
    site = requests.get(url)

    z = ZipFile(io.BytesIO(site.content))
    z.extractall(_data_root)

    print("Data collected")


# ---------------------
# DAG implementation
# ---------------------

dag = DAG(
    "census_pipeline",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)


t1 = PythonOperator(task_id="collect_data", python_callable=collect_data(), dag=dag)
