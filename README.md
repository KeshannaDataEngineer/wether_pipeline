# Weather Data Pipeline

## Overview
This project creates a data pipeline to fetch weather data from an external API, process it, and store it in a database using a cloud platform. The pipeline is implemented using Python and Flask, with a MySQL database for storage. The API follows the OpenAPI 3.0 specification.

### **Features**:
- Fetch hourly weather data based on the venue location and date range.
- Save weather data into the MySQL database.
- Ensure data quality with SQL scripts for validation.
- Automated CI/CD pipeline using GitHub Actions.

## Project Structure
weather-data-pipeline/
│
├── api/
│   ├── app.py                    
│   ├── db_config.py             
│   ├── fetch_weather.py          
│   ├── openapi.yaml              
│
├── sql/
│   ├── create_tables/
│   │   ├── create_venues_table.sql      
│   │   ├── create_weather_table.sql     
│   ├── qa_checks/
│   │   ├── duplicate_check.sql          
│   │   ├── range_check.sql              
│
├── ci-cd/
│   ├── .github/
│   │   ├── workflows/
│   │   │   ├── ci-cd.yml                
│   ├── deploy.sh                      
│
├── README.md                          
└── requirements.txt 
|
|---dags/
|   |
|   |--wether_data_dag.py
|
|---tests/
|   | 
|   |--test_app.py
|   |--test_db_config.py
|   |--test_fetch_wether.py
  

## Setup Instructions

### **Step 1: Clone the Repository**
```bash
git clone <repository-url>
cd weather-data-pipeline

Setup the Database
Create a MySQL database and run the SQL scripts located in sql/create_tables/ to create the necessary tables

mysql -u <user> -p -h <host> < database-name < sql/create_tables/create_venues_table.sql
mysql -u <user> -p -h <host> < database-name < sql/create_tables/create_weather_table.sql

Configure the API
In api/db_config.py, update the database connection parameters with your MySQL credentials.

Install Dependencies
pip install -r requirements.txt

Run the API Locally
python api/app.py

Test the API
Use Postman or Curl to send a POST request to http://localhost:5000/fetch_weather with JSON data.

Run Unit Tests

python -m unittest discover -s tests


Setup Airflow
Install Apache Airflow using the instructions provided in Airflow Installation Guide.
Copy the weather_data_dag.py file to your Airflow dags folder.
Start the Airflow scheduler and webserver


airflow scheduler
airflow webserver

Deploy to Google Cloud
Modify and run ci-cd/deploy.sh to deploy the API to Google Cloud Run or any other cloud environment.