import smtplib
from email.mime.text import MIMEText
from app.utils.config import EMAIL, APP_PASSWORD

def send_email(to_email: str, subject: str, body: str):
    """Send an email synchronously; Celery wraps this in a background task."""
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = to_email
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, APP_PASSWORD)
            server.send_message(msg)
        
        print(f"Email sent successfully to {to_email}")
        return {"status": "success", "email": to_email}
    except Exception as e:
        print(f"Failed to send email to {to_email}: {str(e)}")
        return {"status": "error", "email": to_email, "error": str(e)}

# import smtplib
# from email.mime.text import MIMEText
# from utils.config import EMAIL, APP_PASSWORD

# def send_email(to_email: str, subject: str, body: str):

#     msg = MIMEText(body)
#     msg["Subject"] = subject
#     msg["From"] = EMAIL
#     msg["To"] = to_email

#     try:
#         server = smtplib.SMTP("smtp.gmail.com", 587)
#         server.starttls()
#         server.login(EMAIL, APP_PASSWORD)

#         server.send_message(msg)
#         server.quit()

#         print("Email sent successfully!")

#     except Exception as e:
#         print(" Email error:", e)
