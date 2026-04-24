import os
import smtplib
from email.mime.text import MIMEText
from app.utils.config import EMAIL, APP_PASSWORD
from worker.celery_app import celery

def send_email(to_email: str, subject: str, body: str):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)

    return {"status": "success", "email": to_email}


@celery.task
def send_email_task(to_email: str, subject: str, body: str):
    print("TASK EXECUTED") 
    try:
        return send_email(to_email, subject, body)
    except Exception as e:
        return {"status": "error", "email": to_email, "error": str(e)}
