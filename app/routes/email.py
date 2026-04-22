from fastapi import APIRouter
from app.services.email_service import send_email_async

router = APIRouter()

@router.post("/send/email")
def send_email(email: str):
    send_email_async(email)
    return{
        "message": "Email Queeed"
    }