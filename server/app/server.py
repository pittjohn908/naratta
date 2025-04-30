from fastapi import FastAPI

from app.routes.api_router import api_router

app = FastAPI(title="Narrata")
app.include_router(api_router)
