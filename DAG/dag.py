from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


# Define the function to be executed by the PythonOperator
def print_message():
    print("This message is printed every 3 hours.")

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 11),  # Change this to your desired start date
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG with the schedule interval of 3 hours
dag = DAG(
    'run_every_3_hours',
    default_args=default_args,
    description='Run tasks every 3 hours',
    schedule_interval='0 */3 * * *',  # Cron expression for every 3 hours
)

# Define the PythonOperator
print_message_task = PythonOperator(
    task_id='print_message_task',
    python_callable=print_message,
    dag=dag,
)

# Set dependencies between tasks
print_message_task
