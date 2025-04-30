from typing import Annotated

from fastapi import APIRouter, File, UploadFile

from app.services.epub.epub import EBook

router = APIRouter(prefix="/files")


# @router.post("/create")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}


@router.post("/upload")
async def create_upload_file(file: UploadFile):
    ebook = EBook.from_upload_file(file)
    return {"filename": file.filename, "content": ebook.content}
