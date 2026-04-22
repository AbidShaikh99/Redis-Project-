import json
from app.redis_client.redis import redis_client

CACHE_TTL  = 60


def get_user_cache(user_id):
    
    data = redis_client.get(f"cache:user:{user_id}")
    return json.loads(data) if data else None


def set_user_cache(user_id, data):
    redis_client.set(
        f"cache:user:{user_id}",
        json.dumps(data),
        ex= 60
        
    )