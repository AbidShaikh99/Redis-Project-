from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
import json
from app.services.rate_limiter import is_allowed
from app.db.database import get_db
from app.db import models
from fastapi.responses import JSONResponse
from app.redis_client.redis import redis_client   
router = APIRouter()

@router.get("/limited")
def limited(request: Request):
    ip = request.client.host
    
    if not is_allowed(ip):
        return JSONResponse(status_code=429,
                           content={
                               "status":False,
                               "message":"Rate limited exceeded"
                           })
    return{
        "message":"success"
    }

@router.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):

    cached = redis_client.get(f"cache:user:{user_id}")

    if cached:
        return {
            "source": "cache",
            "data": json.loads(cached)
        }

    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    data = {
        "id": user.id,
        "name": user.name
    }

    redis_client.set(
        f"cache:user:{user_id}",
        json.dumps(data),
        ex=60
    )

    return {
        "source": "db",
        "data": data
    }