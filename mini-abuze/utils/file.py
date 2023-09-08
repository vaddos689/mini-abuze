import json
from pathlib import Path
from typing import Iterable


def load_json(filepath: Path | str) -> dict:
    with open(filepath, "r") as file:
        return json.load(file)


def write_json(filepath: Path | str, data):
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


def load_txt(filepath: Path | str) -> list:
    with open(filepath, "r") as file:
        return file.read().split('\n')


def write_lines_txt(filepath: Path | str, lines: Iterable[str]):
    with open(filepath, "w") as file:
        file.write("\n".join(lines))
