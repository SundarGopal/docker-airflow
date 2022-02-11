# Base Image
FROM sundargopal/yararepo1:airflow


# Arguments that can be set with docker build
ARG AIRFLOW_HOME=/opt/airflow

# Export the environment variable AIRFLOW_HOME where airflow will be installed
ENV AIRFLOW_HOME=${AIRFLOW_HOME}

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
USER root
RUN  pip install --upgrade pip --user && \
   # useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow && \
     pip install  apache-airflow==2.1.0

USER 1001
# Copy the airflow.cfg file (config)
#COPY ./config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
USER root
# Set the owner of the files in AIRFLOW_HOME to the user airflow
RUN chown -R airflow: ${AIRFLOW_HOME}
USER 1001
# Copy the entrypoint.sh from host to container (at path AIRFLOW_HOME)
COPY ./start-airflow.sh ./start-airflow.sh
USER root
# Set the entrypoint.sh file to be executable
RUN chmod +x ./start-airflow.sh
USER 1001
# Set the username to use
USER root
# Create the folder dags inside $AIRFLOW_HOME
RUN mkdir -p ${AIRFLOW_HOME}/dags
USER 1001
# Expose ports (just to indicate that this container needs to map port)
EXPOSE 8080

# Execute start-airflow.sh
CMD [ "./start-airflow.sh" ]

    