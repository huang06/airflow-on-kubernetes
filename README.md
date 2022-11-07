# Airflow On Kubernetes

TBD

## Run with Kubernetes Executor

```bash
kubectl create ns airflow
```

Prepare Volumes for `dags` and `logs`.

```bash
kubectl apply -f volumes.yaml
```

```bash
helm upgrade --install airflow apache-airflow/airflow \
 --namespace airflow \
 --create-namespace \
 -f override-values.yaml
```
