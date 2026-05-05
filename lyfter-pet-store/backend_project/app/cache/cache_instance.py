import os
from dotenv import load_dotenv
from app.cache.cache_manager import CacheManager

load_dotenv()

cache_manager = CacheManager(
  host=os.getenv("REDIS_HOST"),
  port=os.getenv("REDIS_PORT"),
  password=os.getenv("REDIS_PASSWORD"),
)