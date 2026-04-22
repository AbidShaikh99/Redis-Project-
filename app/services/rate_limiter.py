from app.redis_client.redis import redis_client

RATE_LIMIT = 5
WINDOW = 60

def is_allowed(user_id: str):
    key =f"rate_limit:{user_id}"
    
    count = redis_client.get(key)
    
    if count is not None:
        if int(count) >= RATE_LIMIT:
            return False
        redis_client.incr(key)
    else:
        redis_client.set(key, 1, ex = WINDOW)
        
    return True

