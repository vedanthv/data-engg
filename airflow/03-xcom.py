from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'vedanth',
    'retries':5,
    'retry_delay': timedelta(minutes = 2)
}

def greet(ti):# ti -> task instance
    first_name = xcom_pull(task_ids = 'get_name',key = 'first_name') # from xcom get the values for the task_id = get_name
    last_name = ti.xcom_pull(task_ids = 'get_name',key = 'last_name')
    age = ti.xcom_pull(task_ids = 'get_age',key = 'age')
    print("Hello World My first name is {first_name}, last name is {last_name} and I'm {age} years old")

def get_name(ti):
    ti.xcom_push(key = 'first_name',val = 'jerry')
    ti.xcom_push(key = 'last_name',val = 'friedman')

def get_age(ti):
    ti.xcocm_push(key = 'age',val = 20)

with DAG(
    dag_id = "our_first_dag",
    default_args = default_args,
    description = 'This is out first dag',
    start_date = datetime(2021,7,29,2),
    schedule_interval = '@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id = 'greet',
        python_callable = greet()
        )

    # jerry pushed to XCom
    task2 = PythonOperator(
        task_id = 'get_name',
        python_callable = get_name
    )

    # jerry pushed to XCom
    task3 = PythonOperator(
        task_id = 'get_age',
        python_callable = get_age
    )

    [task2,task3] >> task1