import os
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv

from worker.Worker import celery

load_dotenv()

EMAIL = os.getenv("EMAIL", "abidshaikh0401@gmail.com")
APP_PASSWORD = os.getenv("APP_PASSWORD", "yxdb vcnb dcmh ypjt")


def send_email(to_email: str, subject: str, body: str):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)

    return {"status": "success", "email": to_email}


@celery.task(name="worker.send_email_task")
def send_email_task(to_email: str, subject: str, body: str):
    try:
        return send_email(to_email, subject, body)
    except Exception as e:
        print(f"Failed to send email to {to_email}: {str(e)}")
        return {"status": "error", "email": to_email, "error": str(e)}
