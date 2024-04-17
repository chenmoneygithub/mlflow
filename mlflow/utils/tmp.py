import mlflow
import time

mlflow.config.enable_async_logging()

with mlflow.start_run():
    for i in range(100):
        mlflow.log_metric("i", i, step=i)
        time.sleep(0.2)

mlflow.flush_async_logging()
