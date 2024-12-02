import os
from pathlib import Path
import requests


def _get_input_cache_file(day: int, year: int = 2024) -> Path:
    dirpath = Path.home() / ".aoc_input_cache"
    if not dirpath.exists():
        dirpath.mkdir()

    return dirpath / f"{year}_{day}.txt"


def get_puzzle_input(day: int, year: int = 2024) -> str:
    cache_file = _get_input_cache_file(day, year)
    if cache_file.exists():
        return cache_file.read_text()

    cookies = {
            "session": os.getenv("AOC_SESSION_COOKIE")
    }

    response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input', cookies=cookies)
    response.raise_for_status()
    input_text = response.text
    cache_file.write_text(input_text)
    return input_text


if __name__ == "__main__":
    puzzle_input = get_puzzle_input(1)
    print(puzzle_input)
