from utils.download import get_input
from utils.parse import parse_input_simple
from copy import deepcopy

DAY = 6

get_input(DAY)
input = parse_input_simple(DAY)

grid_org = [[char for char in line] for line in input]
X = len(grid_org[0])
Y = len(grid_org)
SYMBOLS = (".", "#", "X")
NEXT = {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)}

def get_start() -> tuple[int, int]:
    for x in range(X):
        for y in range(Y):
            if grid_org[y][x] not in SYMBOLS:
                return x, y
    raise ValueError

# Brute force, finishes in reasonable time, a few minutes
# Improvement: only place extra object in the path of the original route
count = 0

x, y = get_start()
for obj_x in range(X):
    for obj_y in range(Y):
        x, y = get_start()
        direction = (0, -1)
        grid = deepcopy(grid_org)
        if grid[obj_y][obj_x] == '#' or grid[obj_y][obj_x] == '^':
            continue
        grid[obj_y][obj_x] = '#'
        for i in range(X*Y):
            grid[y][x] = "X"
            next_y = y + direction[1]
            next_x = x + direction[0]
            if not (0 <= next_x < X and 0 <= next_y < Y):
                break
            if grid[next_y][next_x] == "#":
                direction = NEXT[direction]
            next_y = y + direction[1]
            next_x = x + direction[0]
            if grid[next_y][next_x] == "#":
                direction = NEXT[direction]
            x += direction[0]
            y += direction[1]
        if i == X*Y-1:
            count+=1
            grid[obj_y][obj_x] = 'O'
print(count)