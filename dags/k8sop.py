from datetime import datetime, timedelta
from airflow import DAG
from airflow.configuration import conf
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2022, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="example_kubernetes_pod", 
    schedule="@once", 
    default_args=default_args
) as dag:
    KubernetesPodOperator(
        namespace="airflow",
        image="hello-world",
        name="airflow-test-pod",
        task_id="task-one",
        in_cluster=True, 
        cluster_context="docker-desktop", 
        config_file=None,
        is_delete_operator_pod=True,
        get_logs=True,
    )
