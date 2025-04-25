from fastapi import APIRouter

router = APIRouter(prefix="novels")


@router.post("/", response_model=[])
async def upload_novel() -> None:
    return {"Hello": "World"}


@router.get("/{novel_id}", response_model=[])
async def get_novel(novel_id: int) -> None:
    return {"Hello": "World"}


@router.post("/{novel_id}", response_model=[])
async def generate_audiobook(novel_id: int) -> None:
    return {"Hello": "World"}
