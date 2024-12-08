from collections import defaultdict
from dataclasses import dataclass
import math
from utils.download import get_input
from utils.parse import parse_input_simple, make_grid
from random import uniform
from enum import Enum, auto
from copy import deepcopy
from itertools import combinations

DAY = 8

get_input(DAY)
input = parse_input_simple(DAY)

grid, X, Y = make_grid(input)

antenna_groups = defaultdict(list)

for x in range(X):
    for y in range(Y):
        if (freq := grid[y][x]) != '.':
            antenna_groups[freq].append((x, y))

anti_nodes = []

for locs in antenna_groups.values():
    for comb in combinations(locs, 2):
        a, b = comb
        for n in range(-50, 50):
            new_x = a[0] + n*(a[0] - b[0])
            new_y = a[1] + n*(a[1] - b[1])
            anti_nodes.append((new_x, new_y))

anti_nodes = [node for node in anti_nodes if 0 <= node[0] < X and 0 <= node[1] < Y]
anti_nodes = set(anti_nodes)

print(len(anti_nodes))