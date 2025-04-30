import os

from fastapi import APIRouter
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

router = APIRouter(prefix="/voices")


@router.get("/{voice_id}", response_model=[])
async def get_voices(voice_id: int) -> None:
    return {"Hello": "World"}


@router.post("/", response_model=[])
async def upload_voice() -> None:
    return {"Hello": "World"}


@router.post("/sample", response_model=[])
async def sample_voice() -> None:
    os.environ["TORCH_FORCE_NO_WEIGHTS_ONLY_LOAD"] = "1"
    preload_models()

    text_prompt = """
        Hello, my name is Suno. And, uh — and I like pizza. [laughs]
        But I also have other interests such as playing tic tac toe.
    """

    audio_array = generate_audio(text_prompt)

    write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)

    return {"Hello": "World"}
