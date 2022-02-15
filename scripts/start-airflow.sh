#!/usr/bin/env bash

# Initiliase the metadatabase
airflow db init

# Create User
airflow users create -e "admin@airflow.com" -f "airflow" -l "airflow" -p "airflow" -r "Admin" -u "airflow"

# Run the scheduler in background ,this format is unix defined one 
airflow scheduler &> /dev/null &

# Run the web sever in foreground (for docker logs)
exec airflow webserver