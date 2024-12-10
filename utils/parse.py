from typing import Any


def parse_input_simple(day: int, type=int) -> list[Any]:
    assert 1 <= day <= 25
    with open(f"{day}.txt", "r") as file:
        data = str(file.readlines()[0])[2:]
        data = data.split("\\n")[:-1]
        try:
            data = [[type(str(item)) for item in line.split()] for line in data]
        except ValueError:
            return data
    return data

def make_grid(input):
    grid = [[char for char in line] for line in input]
    X = len(grid[0])
    Y = len(grid)
    return grid, X, Y