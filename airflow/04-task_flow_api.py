from airflow.decorators import datetime,timedelta

default_args = {
    'owner':'vedanth',
    'retries':5,
    'retry_delay': timedelta(minutes = 2)
}

@dag(dag_id = 'dag_with_taskflow',
     default_args = default_args,
     start_date = datetime(2023,10,26),
     schedule_interval = '@daily')

def hello_world_etl():

    @task()
    def get_name():
        return "Jerry"
    
    @task()
    def get_age():
        return 19
    
    @task()
    def greet(name,age):
        print(f"Hello World my name is {name}"
              f"Im {age} years old")
        
    name = get_name()
    age = get_age()
    greet(name = name,age = age)

greet_dag = hello_world_etl_dag()

# Multiple Outputs

from airflow.decorators import dag,tasks

default_args = {
    'owner':'vedanth',
    'retries':5,
    'retry_delay': timedelta(minutes = 2)
}

@dag(dag_id = 'dag_with_taskflow',
     default_args = default_args,
     start_date = datetime(2023,10,26),
     schedule_interval = '@daily')

def hello_world_etl():

    @task(multiple_output = True)
    def get_name():
        return {
            "first_name": 'Jerry',
            "last_name": 'Fridman'
        }
    
    @task()
    def get_age():
        return 19
    
    @task()
    def greet(first_name,last_name,age):
        print(f"Hello World my name is {name}"
              f"Im {age} years old")
        
    name_dict = get_name()
    age = get_age()
    greet(first_name = name_dict['first_name'],last_name = name_dict['last_name'],age = age)

greet_dag = hello_world_etl_dag()

