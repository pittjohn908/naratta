from fastapi import APIRouter

from . import files
from . import novels
from . import voices

api_router = APIRouter()
api_router.include_router(files.router, prefix="/v1")
api_router.include_router(novels.router, prefix="/v1")
api_router.include_router(voices.router, prefix="/v1")
