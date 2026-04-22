from celery import Celery
import time

celery = Celery(
    "worker",
    broker = "redis://localhost:6379/0"
) 

@celery.task
def send_email_task(email):
    print(f"Sending email to {email}")
    time.sleep(5)
    print("Email sent successfully!")
    