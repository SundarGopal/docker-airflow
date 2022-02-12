#!/usr/bin/env bash
airflow db init
airflow users create -e "admin@airflow.com" -f "airflow" -l "airflow" -p "airflow" -r "Admin" -u "airflow"
exec airflow webserver