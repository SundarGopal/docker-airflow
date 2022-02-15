# Base Image
FROM sundargopal/yararepo1:airflow


USER root
# Install dependencies and tools
RUN apt-get update -y && \
    apt-get upgrade -yqq && \
    apt-get install -yqq --no-install-recommends \
    python3-dev \
    wget \
    libczmq-dev \
    curl \
    libssl-dev \
    git \
    inetutils-telnet \
    bind9utils freetds-dev \
    libkrb5-dev \
    libsasl2-dev \
    libffi-dev libpq-dev \
    freetds-bin build-essential \
    default-libmysqlclient-dev \
    apt-utils \
    rsync \
    zip \
    unzip \
    gcc \
    vim \
    netcat \
    && apt-get autoremove -yqq --purge && apt-get clean
USER 1001

# Upgrade pip
# Create airflow user 
# Install apache airflow with subpackages
USER airflow
RUN  pip install --upgrade pip --user && \
   # useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow && \
     pip install  apache-airflow==2.1.0 && \
     pip install psycopg2


    