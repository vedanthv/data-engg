## Airflow for Data Pipelines

### Installation

#### Using pip package

1. Python 3.6 is the min version required.

2. Create a Python Virtual Environment ```python3 -m venv py_env```

3. Activate the Python Environment **py_env** ```source py_env/bin/activate```

4. Install airflow using ```pip install apache-airflow```

5. Now before creating a db, we have to set the path ```export AIRFLOW_HOME = .```

6. Initialize the db with ```airflow db init```

7. Start Airflow Web Server using ```airflow webserver -p 8080```

8. Create a username and password ```airflow users create --username admin --firstname ved --lastname baliga --role admin --email vedanthvbaliga@gmail.com``` and set the password.

9. Run ```airflow scheduler``` to start the scheduler.

### Using Docker for Installation

1. For Windows, first setup and setup WSL2. Check out the [video](https://www.youtube.com/watch?v=YByZ_sOOWsQ&pp=ygUdaW5zdGFsbGluZyB3c2wyIG9uIHdpbmRvd3MgMTE%3D) here.

2. Now download Docker Desktop from the [website](https://docs.docker.com/desktop/install/windows-install/)

3. Use this curl command to dowload Airflow yaml file via Docker Compose.[```curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.7.3/docker-compose.yaml'```]

4. Change the core executor in yaml file to LocalExecutor. Remove the Celery flower and celery-worker.

5. Initialize the Environment : ```mkdir -p ./dags ./logs ./plugins ./config echo -e "AIRFLOW_UID=$(id -u)" > .env```

6. Start the docker environment : ```docker compose up airflow-init```

7. Run Airflow : ```docker compose up```



