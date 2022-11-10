import pendulum
from airflow import DAG
from airflow.configuration import conf
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator

with DAG(
    dag_id="example_k8spod", 
    start_date=pendulum.datetime(2022, 11, 10, tz="UTC"),
    schedule=None, 
) as dag:
    KubernetesPodOperator(
        name="k8spod",
        task_id="k8spod",
        namespace="airflow",
        image="hello-world",
        in_cluster=True, 
        is_delete_operator_pod=True,
        get_logs=True,
    )
