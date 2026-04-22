from worker.worker import send_email_task

def send_email_async(email: str):
    send_email_task.delay(email)