from fastapi import APIRouter

router = APIRouter(prefix="/voices")


@router.get("/{voice_id}", response_model=[])
async def get_voices(voice_id: int) -> None:
    return {"Hello": "World"}


@router.post("/", response_model=[])
async def upload_voice() -> None:
    return {"Hello": "World"}
