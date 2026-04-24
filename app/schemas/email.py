from pydantic import BaseModel
from typing import List


class EmailRequest(BaseModel):
    email: List[str]
    subject: str
    body: str