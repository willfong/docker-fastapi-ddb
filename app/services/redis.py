import os
import redis
import json
from ..services import util, statsd

r = redis.Redis(host=os.environ.get('REDIS_ENDPOINT_URL'))

@statsd.statsd_root_stats
def put(key, value, ttl):
    if r.set(key, json.dumps(value), ex=ttl):
        return True
    return False

@statsd.statsd_root_stats
def get(k):
    results = r.get(k)
    if results:
        return json.loads(results)
    return False

def incr(k):
    if r.incr(k):
        return True
    return False

# TODO: scan shouldn't be used. Needs to be upgraded
def scan():
    return r.scan()
