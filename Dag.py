## Libraries import 

from airflow import DAG 
from airflow.operators.bash import BashOperator
import datetime as dt
import glob
import json
import pandas as pd
import os 

## Dag parameters set_up

default_args={
'owner':'ismo',
'start_date':dt.datetime.today(),
'retries':1,
'retry_delay':dt.timedelta(minutes=2) }  

### Instanciating the Dag 

dag=DAG(
   'JSON_to_DB_ETL',
   description='ETL to transform and load data from JSON to a Postgres DB',
   default_args=default_args,
   schedule_interval=None # Dag will be triggered mannualy 
)

# Dag tasks Definitions




# Pipeline Definition


