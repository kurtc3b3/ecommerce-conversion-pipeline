"""Daily batch training DAG: dbt → Feast materialize → MLflow train."""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.decorators import task

default_args = {
    "owner": "ml-platform",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="conversion_batch_training",
    description="Build features and retrain the conversion model on a schedule",
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["training", "conversion", "batch"],
    default_args=default_args,
) as dag:

    @task
    def run_dbt() -> None:
        """Run dbt models to refresh warehouse feature tables."""
        raise NotImplementedError("Run: cd /opt/airflow/project/dbt && dbt run")

    @task
    def materialize_feast_features() -> None:
        """Push offline features to Redis online store."""
        raise NotImplementedError(
            "Run: cd /opt/airflow/project/feast && feast materialize-incremental ..."
        )

    @task
    def train_conversion_model() -> None:
        """Train model and log metrics/artifacts to MLflow."""
        raise NotImplementedError("Run: python /opt/airflow/project/training/train.py")

    @task
    def validate_model() -> None:
        """Gate promotion — compare new run against production baseline."""
        raise NotImplementedError("Implement MLflow model validation thresholds")

    run_dbt() >> materialize_feast_features() >> train_conversion_model() >> validate_model()
