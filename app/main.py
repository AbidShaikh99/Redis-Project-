from fastapi import FastAPI, APIRouter
from app.routes import user, email
from app.db.database import engine
from app.db import models

models.Base.metadata.create_all(bind = engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(email.router)

