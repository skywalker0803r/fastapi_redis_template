import redis
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
redis_client = redis.Redis.from_url(redis_url, decode_responses=True)

def set_key(key: str, value: str):
    redis_client.set(key, value)

def get_key(key: str) -> str:
    return redis_client.get(key)

def delete_key(key: str) -> bool:
    return redis_client.delete(key) > 0
