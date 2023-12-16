from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'vedanth',
    'retries':5,
    'retry_delay': timedelta(minutes = 2)
}

def greet(age,ti):# ti -> task instance
    name = ti.xcom_pull(task_ids = 'get_name') # from xcom get the values for the task_id = get_name
    print("Hello World My name is {name} and I'm {age} years old")

def get_name():
    return 'Jerry'


with DAG(
    dag_id = "our_first_dag",
    default_args = default_args,
    description = 'This is out first dag',
    start_date = datetime(2021,7,29,2),
    schedule_interval = '@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id = 'greet',
        python_callable = greet(),
        op_kwargs = {'age':20}
    )

    # jerry pushed to XCom
    task2 = PythonOperator(
        task_id = 'get_name',
        python_callable = get_name
    )

    task2 >> task1