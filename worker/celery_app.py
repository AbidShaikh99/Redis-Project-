from celery import Celery

celery = Celery(
    "worker",
    broker="redis://localhost:6379/0",   
    backend="redis://localhost:6379/0",
    include=["worker.tasks"]   
)

celery.conf.update(
    timezone="UTC",
    enable_utc=True
)

