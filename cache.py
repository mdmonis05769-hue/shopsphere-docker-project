import redis

cache = redis.Redis(
    host="shopsphere-redis",
    port=6379,
    decode_responses=True
)
