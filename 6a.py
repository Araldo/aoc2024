from utils.download import get_input
from utils.parse import parse_input_simple
from random import uniform

DAY = 6

get_input(DAY)
input = parse_input_simple(DAY)

grid = [[char for char in line] for line in input]
X = len(grid[0])
Y = len(grid)
SYMBOLS = (".", "#", "X")
NEXT = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}


def get_start() -> tuple[int, int]:
    for x in range(X):
        for y in range(Y):
            if grid[y][x] not in SYMBOLS:
                return x, y
    raise ValueError


x, y = get_start()
direction = (0, -1)

while True:
    grid[y][x] = "X"
    next_y = y + direction[1]
    next_x = x + direction[0]
    if not (0 <= next_x < X and 0 <= next_y < Y):
        break
    if grid[next_y][next_x] == "#":
        direction = NEXT[direction]
    x += direction[0]
    y += direction[1]

count = 0
for x in range(X):
    for y in range(Y):
        if grid[y][x] == 'X':
            count+=1

print(count)