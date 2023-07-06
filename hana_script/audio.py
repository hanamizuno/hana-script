"""Audio processing."""
from pathlib import Path
from typing import cast

from pydub import AudioSegment
from pydub.silence import detect_nonsilent


def load_audio(audio_path: Path) -> AudioSegment:
    """Load audio file."""
    return AudioSegment.from_file(audio_path)


def extract_non_silent(audio: AudioSegment) -> list[tuple[AudioSegment, int]]:
    """Extract non-silent chunks from audio."""
    non_silence_sections = detect_nonsilent(
        audio, min_silence_len=5000, silence_thresh=-48,
    )
    non_silence_sections = cast(list[list[int]], non_silence_sections)
    print(non_silence_sections)
    non_silent_chunks = [
        (audio[start:end], start) for start, end in non_silence_sections
    ]

    return non_silent_chunks
