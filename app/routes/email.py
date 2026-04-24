from fastapi import APIRouter
from worker.tasks import send_email_task
from app.schemas.email import EmailRequest

router = APIRouter()



@router.post("/send/email")
def send_email_api(request: EmailRequest):
    
    for email in request.email:
        send_email_task.delay(
            email,
            request.subject,
            request.body
        )

    return {
        "status": True,
        "message": "Email is being sent"
    }
