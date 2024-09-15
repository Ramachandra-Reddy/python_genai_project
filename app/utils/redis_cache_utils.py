from redis import asyncio as aioredis
from resources import CONFIG

host = CONFIG["redis_db"]["host"]
username = CONFIG["redis_db"]["username"]


class ChatCache:
    def __init__(self, host, port):
        pass