from typing import Any


def parse_input_simple(day: int) -> list[Any]:
    assert 1 <= day <= 25
    with open(f"{day}.txt", "r") as file:
        data = str(file.readlines()[0])[2:]
        data = data.split("\\n")[:-1]
        data = [[int(str(item)) for item in line.split()] for line in data]
    return data