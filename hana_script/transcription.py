"""Transcribe audio."""
import os
from pathlib import Path

import openai
from dotenv import load_dotenv

AUDIO_SUFFIXES = [
    "mp3",
    "mp4",
    "mpeg",
    "mpga",
    "m4a",
    "wav",
    "webm",
]


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def transcribe_audio_file(audio_file_path: Path) -> str:
    """Transcribe audio file using OpenAI Audio API."""
    if audio_file_path.suffix in AUDIO_SUFFIXES:
        raise ValueError("File type not supported.")
    with open(audio_file_path, "rb") as f:
        response = openai.Audio.transcribe("whisper-1", file=f, language="ja")

    return response.text
