from collections import defaultdict
from dataclasses import dataclass
import math
from utils.download import get_input
from utils.parse import parse_input_simple, make_grid
from random import uniform
from enum import Enum, auto
from copy import deepcopy
from itertools import combinations, zip_longest, product
from functools import cache
import re
import time

DAY = 14


get_input(DAY)
input = parse_input_simple(DAY)

X = 101
Y = 103

r=[]

for row in input:
    if match := re.match(r'p=(\d+),(\d+)', row):
        x, y = [int(v) for v in match.groups(1)]
    if match := re.match(r'.*v=(\-?\d+),(\-?\d+)', row):
        vx, vy = [int(v) for v in match.groups(1)]
    r.append((x, y, vx, vy))

for itt in range(X*Y):
    grid = []
    for xg in range(Y):
        grid.append([])
        for xg in range(X):
            grid[-1].append('.')

    for r_ in r:
        x, y, vx, vy = r_ 
        x = (x + itt * vx) % X
        y = (y + itt * vy) % Y

        grid[y][x] = '*'

    n_in_a_row_max = 0
    n_in_a_row_count = 0

    for x in range(X):
        for y in range(Y):
            if grid[y][x] == '*':
                n_in_a_row_count += 1
                n_in_a_row_max = max(n_in_a_row_max, n_in_a_row_count)
            else:
                n_in_a_row_count = 0

    if n_in_a_row_max > 10:
        for row in grid:
            print(''.join(row))
        print(itt)
        break
 