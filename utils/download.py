from typing import Any
import requests
import os
from enum import Enum


class Puzzle(Enum):
    A = (0,)
    B = 1


def get_input(day: int, puzzle: Puzzle = Puzzle.A) -> None:
    assert 1 <= day <= 25
    filename = f"{day}.txt"
    if os.path.exists(filename):
        return
    response = requests.get(
        f"https://adventofcode.com/2024/day/{day}/input",
        cookies={"session": os.environ["AOC_SESSION"]},
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
        },
    )
    with open(filename, "w+") as file:
        file.write(str(response.content))
