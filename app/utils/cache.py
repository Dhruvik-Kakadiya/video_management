import redis
import os

redis_host = os.getenv("REDIS_HOST")
redis_port = os.getenv("REDIS_PORT")

r = redis.Redis(host=redis_host, port=redis_port)


def is_blocked(video_id: int) -> bool:
    return r.sismember("blocked_videos", video_id)


def block_video_in_cache(video_id: int):
    r.sadd("blocked_videos", video_id)
