import json
import os


def ensure_directory(directory: str) -> None:
    """Create a directory if it does not already exist."""

    os.makedirs(directory, exist_ok=True)


def save_json(data: dict, output_path: str) -> None:
    """Save dictionary data as a JSON file."""

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)