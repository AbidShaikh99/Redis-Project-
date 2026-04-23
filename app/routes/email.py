from fastapi import APIRouter
from worker.tasks import send_email_task

router = APIRouter()

@router.post("/send/email")
def send_email_api(email: str):

    subject = "Welcome"
    body = "Hello! This is a real email sent using Celery."

    task = send_email_task.delay(email, subject, body)

    return {
        "status": True,
        "message": "Email is being sent",
        "task_id": task.id
    }
