"""hana-script."""
import sys
from argparse import ArgumentParser
from logging import DEBUG, Formatter, StreamHandler, getLogger
from pathlib import Path

from hana_script.audio import extract_non_silent, load_audio
from hana_script.transcription import transcribe_audio

logger = getLogger(__name__)
logger.setLevel(DEBUG)
formatter = Formatter(
    "[%(levelname)s]%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
stream_handler = StreamHandler(sys.stdout)
stream_handler.setLevel(DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def main(audio_file_path_str: str) -> None:
    """Generate a transcription for an audio file.

    Args:
        audio_file_path_str (str): The path to the audio file.

    Returns:
        None
    """
    audio_file_path = Path(audio_file_path_str)
    audio = load_audio(audio_file_path)
    logger.info(f"Loaded {audio_file_path}")
    logger.info(f"Duration: {audio.duration_seconds} seconds")

    non_silent_chunks = extract_non_silent(audio)
    logger.info(f"Found {len(non_silent_chunks)} non-silent chunks")

    transcriptions = [
        transcribe_audio(chunk) for chunk, _ in non_silent_chunks
    ]
    transcription = "\n".join(transcriptions)
    logger.info(f"Transcription:\n{transcription}")

    output_file_path = audio_file_path.with_suffix(".txt")
    with output_file_path.open("w") as f:
        f.write(transcription)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--audio-file", type=Path, required=True)
    args = parser.parse_args()
    main(args.audio_file)
