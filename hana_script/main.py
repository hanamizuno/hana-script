"""hana-script"""
from argparse import ArgumentParser
from pathlib import Path

from hana_script.transcription import transcribe_audio_file


def main(audio_file_path_str: str) -> None:
    """Main function."""
    audio_file_path = Path(audio_file_path_str)
    transcription = transcribe_audio_file(audio_file_path)
    print(transcription)

    output_file_path = audio_file_path.with_suffix(".txt")
    with open(output_file_path, "w") as f:
        f.write(transcription)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--audio-file", type=Path, required=True)
    args = parser.parse_args()
    main(args.audio_file)
