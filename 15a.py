from collections import defaultdict
from dataclasses import dataclass
import math
import time
from utils.download import get_input
from utils.parse import parse_input_simple, make_grid
from random import uniform
from enum import Enum, auto
from copy import deepcopy
from itertools import combinations, zip_longest, product
from functools import cache
import re

DAY = 15


DIRECTIONS = {
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
}

get_input(DAY)
input = parse_input_simple(DAY)

grid = []
movements = []
end_of_grid = False

for line in input:
    if line:
        if end_of_grid:
            movements.append(line)
        else:
            grid.append(line)
    else:
        end_of_grid = True

grid = [[c for c in line] for line in grid]
X = len(grid[0])
Y = len(grid)
movements = "".join(movements)

for x in range(X):
    for y in range(Y):
        if grid[y][x] == "@":
            loc = (x, y)

for idx, movement in enumerate(movements):
    can_move = False
    blocked = False
    next_x = loc[0]
    next_y = loc[1]
    count = 0
        
    while not blocked and not can_move:
        count += 1
        next_x += DIRECTIONS[movement][0]
        next_y += DIRECTIONS[movement][1]
        if grid[next_y][next_x] == '#':
            blocked = True
        elif grid[next_y][next_x] == '.':
            can_move = True

    if can_move:
        fields = '@' + 'O'*(count-1)
        grid[loc[1]][loc[0]] = '.'
        next_x = loc[0]
        next_y = loc[1]
        for i in range(count):
            next_x += DIRECTIONS[movement][0]
            next_y += DIRECTIONS[movement][1]
            grid[next_y][next_x] = fields[i]
            if i == 0:
                loc = (next_x, next_y)
        for line in grid:
            print(''.join(line))

sum = 0
for x in range(X):
    for y in range(Y):
        if grid[y][x] == 'O':
            sum += y*100+x
print(sum)