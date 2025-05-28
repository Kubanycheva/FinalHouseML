import fastapi
from fastapi_limiter import FastAPILimiter

from api.endpoints import (users, house)
import redis.asyncio as redis
from fastapi import FastAPI
from contextlib import asynccontextmanager

import uvicorn
from house_app.admin.setup import setup_admin


async def init_redis():
    return redis.Redis.from_url('redis://localhost', encoding='utf-8',
                                decode_responses=True)


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = await init_redis()
    await FastAPILimiter.init(redis)
    yield
    await redis.close()


house_app = fastapi.FastAPI(title='House site', lifespan=lifespan)
setup_admin(house_app)



house_app.include_router(users.user_router, tags=['UserProfile'])
house_app.include_router(house.house_router, tags=['House'])

if __name__ == '__main__':
    uvicorn.run(house_app, host='127.0.0.1', port=8000)
