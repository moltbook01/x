from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import router
from app.db import init_db
from app.scheduler import Scheduler

scheduler = Scheduler()


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    await scheduler.start()
    try:
        yield
    finally:
        await scheduler.stop()


app = FastAPI(lifespan=lifespan, title="I-Only Debate System")
app.include_router(router)
