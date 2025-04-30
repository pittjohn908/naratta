from fastapi import FastAPI

from app.routes.routes import api_router

app = FastAPI(title="Narrata")
app.include_router(api_router)
