from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.google.cloud.operators.cloud_sql import CloudSQLExecuteQueryOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

import json
import requests

def fetch_weather_data(**context):
    """Fetch weather data from the API"""
    venue_id = context['params']['venue_id']
    start_date = context['params']['start_date']
    end_date = context['params']['end_date']
    
    url = f"http://<{FLASK_APP_HOST}>:5000/fetch_weather"
    payload = {
        "venue_id": venue_id,
        "start_date": start_date,
        "end_date": end_date
    }
    response = requests.post(url, json=payload)
    
    if response.status_code != 200:
        raise Exception("API request failed")
    
    return response.json()

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'start_date': days_ago(1),
}

dag=DAG(
    'weather_data_dag',
    default_args=default_args,
    description='DAG to fetch weather data and insert into Google Cloud SQL',
    schedule_interval='@daily',
    catchup=False,
)

dummy_start=DummyOperator(
    task_id='start',
    dag=dag
)
fetch_weather = PythonOperator(
        task_id='fetch_weather',
        python_callable=fetch_weather_data,
        provide_context=True,
        params={
            'venue_id': f'{venue_id}', 
            'start_date': '2024-01-01',
            'end_date': '2024-01-02'
        },
        dag=dag
)
insert_weather_data = CloudSQLExecuteQueryOperator(
        task_id='insert_weather_data',
        sql="""
        INSERT INTO weather (venue_id, timestamp, temperature, relative_humidity, dewpoint, apparent_temperature, precipitation, rain, showers, snowfall, snow_depth)
        VALUES 
        (1, '2024-01-01 00:00:00', 10.0, 80, 5.0, 9.0, 0.0, 0.0, 0.0, 0.0, 0.0),
        (1, '2024-01-01 01:00:00', 11.0, 75, 6.0, 10.0, 0.0, 0.0, 0.0, 0.0, 0.0);
        """,
        gcp_conn_id="google_cloud_default",
        instance='cloud-sql-instance',
        database='database-name',
        dag=dag
)

dummy_end=DummyOperator(
    task_id='End',
    dag=dag
)
dummy_start >> fetch_weather >> insert_weather_data >> dummy_end
