from server.lru_cache import LRUCache
from server.persistence import log_set, log_delete

class KeyValueStore:
    def __init__(self, capacity=100):
        self.cache = LRUCache(capacity)

    async def get(self, key):
        return self.cache.get(key)

    async def set(self, key, value):
        self.cache.put(key, value)
        log_set(key, value)

    async def delete(self, key):
        self.cache.delete(key)
        log_delete(key)
