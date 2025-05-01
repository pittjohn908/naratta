from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.routes.api_router import api_router
from app.config import get_config
from app.db.engine import run_migrations

app_config = get_config()


@asynccontextmanager
async def lifespan(app: FastAPI):
    run_migrations()
    yield


app = FastAPI(title="Narrata", lifespan=lifespan)
app.include_router(api_router)
