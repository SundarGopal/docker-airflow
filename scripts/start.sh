#!/usr/bin/env bash
airflow db init
airflow users create -e "admin@airflow.com" -f "airflow" -l "airflow" -p "airflow" -r "Admin" -u "airflow"
pip install apache-airflow-providers-slack
exec airflow webserver