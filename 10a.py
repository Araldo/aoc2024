from collections import defaultdict
from dataclasses import dataclass
import math
from utils.download import get_input
from utils.parse import parse_input_simple, make_grid
from random import uniform
from enum import Enum, auto
from copy import deepcopy
from itertools import combinations, zip_longest

DAY = 10

get_input(DAY)
input = parse_input_simple(DAY, str)
input = [row[0] for row in input]
grid, X, Y = make_grid(input)


def climb(grid, locations):
    result = []
    for location in locations:
        x, y = location
        height = grid[y][x]
        for direction in ((0,1), (0,-1), (1,0),(-1,0)):
            x_new = x+direction[0]
            y_new = y+direction[1]
            if 0<= x_new < X and 0 <= y_new < Y and grid[y_new][x_new] == height+1:
                result.append((x_new,y_new))
    result = list(set(result))
    if height == 8:
        return len(result)
    else:
        return climb(grid, result)

heads = []
for x in range(X):
    for y in range(Y):
        grid[y][x] = int(grid[y][x])
        if grid[y][x] == 0:
            heads.append((x, y))

sum = 0
for head in heads:
    sum += climb(grid, [head])

print(sum)