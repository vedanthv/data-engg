from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner':'vedanth',
    'retries':5,
    'retry_delay': timedelta(minutes = 2)
}

with DAG(
    dag_id = "our_first_dag",
    default_args = default_args,
    description = 'This is out first dag',
    start_date = datetime(2021,7,29,2),
    schedule_interval = '@daily'
) as dag:
    task1 = BashOperator(
        task_id = 'first_task',
        bash_command = "echo hello world, this is my first task"
    )

    task2 = BashOperator(
        task_id = 'second_task',
        bash_command = "echo im task2 and i will be running after task1"
    )

    task1.set_downstream(task2)