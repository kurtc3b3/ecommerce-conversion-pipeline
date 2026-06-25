"""Train a baseline conversion model and log to MLflow."""

import mlflow


def main() -> None:
    mlflow.set_experiment("conversion-prediction")
    with mlflow.start_run():
        mlflow.log_param("model", "placeholder")
        mlflow.log_metric("auc", 0.0)
        print("Training stub — implement after features are materialized.")


if __name__ == "__main__":
    main()
