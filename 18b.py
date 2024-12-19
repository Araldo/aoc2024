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

DAY = 18


DIRECTIONS = {
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
}

get_input(DAY)
input = parse_input_simple(DAY)


for n in range(2950,len(input)):
    grid = []
    X, Y = 73,73

    for y in range(Y):
        grid.append([])
        for x in range(X):
            if (x == 0 or x == X-1) or (y==0 or y == Y-1):
                grid[y].append('#')
            else:
                grid[y].append('.')

    for idx, line in enumerate(input):
        if idx == n:
            break
        x, y = line.split(',')
        x = int(x)+1
        y = int(y)+1
        grid[y][x] = '#'

    grid[Y-2][X-2] = 'E'

    lowest = 999999999999999
    grid[0]

    best = {}
    for x in range(X):
        for y in range(Y):
            if grid[y][x] in ('.', 'E'):
                best[(x, y)] = lowest
    best[(1,1)] = 0

    for i in range(1250):
        if best[X-2,Y-2] < 99999999999:
            break
        for pos, score in best.items():
            x, y = pos
            for symbol, delta in DIRECTIONS.items():
                new_score = score + 1
                new_pos = (x+delta[0], y+delta[1])
                if grid[new_pos[1]][new_pos[0]] == '#':
                    continue
                if grid[new_pos[1]][new_pos[0]] == 'E':
                    if new_score < lowest:
                        lowest = new_score
                key = (new_pos[0], new_pos[1])
                if new_score < best[key]:
                    best[key] = new_score
    print(n, lowest, input[n-1])
    if lowest > 99999999:
        break

