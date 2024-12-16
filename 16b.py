from collections import defaultdict
from dataclasses import dataclass
import math
import time
from utils.download import get_input
from utils.parse import parse_input_simple, make_grid
from random import uniform
from enum import Enum, auto
from copy import copy, deepcopy
from itertools import combinations, zip_longest, product
from functools import cache
import re

DAY = 16


DIRECTIONS = {
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
}

get_input(DAY)
input = parse_input_simple(DAY)
grid, X, Y = make_grid(input)
best = {}
lowest = 999999999999999

for x in range(X):
    for y in range(Y):
        for dir in DIRECTIONS:
            if grid[y][x] == 'S' and dir == '>':
                best[(x, y, dir)] = (0, set())
            elif grid[y][x] in ('.', 'E', 'S'):
                best[(x, y, dir)] = (lowest, set())


for i in range(250):
    for pos, data in best.items():
        x, y, d = pos
        score, route = data
        for symbol, delta in DIRECTIONS.items():
            new_route = copy(route)
            new_pos = (x+delta[0], y+delta[1])
            new_route.add(new_pos)
            if symbol == d:
                new_score = score + 1
            else:
                new_score = score + 1001
            if grid[new_pos[1]][new_pos[0]] == '#':
                continue
            if grid[new_pos[1]][new_pos[0]] == 'E':
                if new_score <= lowest:
                    lowest = new_score
            new_dir = symbol
            key = (new_pos[0], new_pos[1], new_dir)
            if new_score == best[key][0]:
                best[key] = (new_score, new_route | best[key][1])
            if new_score < best[key][0]:
                best[key] = (new_score, new_route)


count = 1  # S is not counted below
for pos, data in best.items():
    x, y, d = pos
    score, route = data
    if score == lowest:
        for pos in route:
            grid[pos[1]][pos[0]] = 'O'
            count += 1

print(count)