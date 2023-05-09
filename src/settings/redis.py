import os

import aioredis
import redis

AUTH_REDIS_URL = os.getenv("AUTH_REDIS_URL")
ADMIN_REDIS_URL = os.getenv("ADMIN_REDIS_URL")
auth_redis = redis.from_url(AUTH_REDIS_URL, decode_responses=True)
admin_redis = aioredis.from_url(ADMIN_REDIS_URL, decode_responses=True)
