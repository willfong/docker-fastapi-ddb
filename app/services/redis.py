import os
import redis
import json
from ..services import util

r = redis.Redis(host=os.environ.get('REDIS_ENDPOINT_URL'))

def put(key, value, ttl):
    util.logger.warning(f"Key: {key}")
    if r.set(key, json.dumps(value), ex=ttl):
        return True
    return False

def get(k):
    results = r.get(k)
    if results:
        return json.loads(results)
    return False