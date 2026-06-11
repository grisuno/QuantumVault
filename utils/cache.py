# /home/grisun0/src/postcuantum/v1/utils/cache.py
from typing import Optional, Any
import redis
import json

class Cache:
    """Redis-based caching layer."""
    def __init__(self):
        self.client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    def get(self, key: str) -> Optional[Any]:
        """Retrieve a value from the cache."""
        value = self.client.get(key)
        return json.loads(value) if value else None

    def set(self, key: str, value: Any, ttl: int = 3600) -> None:
        """Store a value in the cache with an optional TTL (seconds)."""
        self.client.setex(key, ttl, json.dumps(value))

    def delete(self, key: str) -> None:
        """Delete a key from the cache."""
        self.client.delete(key)
