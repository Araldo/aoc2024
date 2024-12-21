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

DAY = 20

DIRECTIONS = {
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
}

get_input(DAY)
input = parse_input_simple(DAY)

# input = """###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############""".split('\n')

grid, X, Y = make_grid(input)
print(grid)


START = (0,0)
END = (0,0)

for x in range(X):
    for y in range(Y):
        if grid[y][x] == "S":
            START = (x, y)
        if grid[y][x] == "E":
            END = (x, y)


dir_at_pos = {}


def get_count(cheat= None, cheat_direction = None):
    global dir_at_pos
    global grid

    last_direction = (0,0)
    count = 0
    pos = START

    grid_ = deepcopy(grid)

    while pos != END:
        x, y = pos
        found = False
        if count == cheat and cheat_direction:
            dx, dy = cheat_direction
            found = True
            x += dx * 2
            y += dy * 2
            count += 2
            pos = (x,y)
            if x < 0 or x >= X or y < 0 or y >= Y or grid[y][x] == '#':
                return None, grid_
            grid_[y-2*dy][x-2*dx] = '1'
            grid_[y-dy][x-dx] = '2'
            if pos != END:
                last_direction = dir_at_pos[pos]
            continue
        for direction in DIRECTIONS.values():
            try:
                if dir_at_pos[pos] != direction:
                    continue
            except KeyError:
                pass
            dx, dy = direction
            if direction == (-last_direction[0], -last_direction[1]):
                continue
            if grid[y+dy][x+dx] in ('.', 'E'):
                found = True
                grid_[y][x] = '■'
                if cheat is None:
                    dir_at_pos[pos] = direction
                count += 1
                pos = (x+dx, y+dy)
                last_direction = direction
                break
        if not found:
            # for line in grid_:
            #     print(''.join(line))
            # print(pos)
            return None, grid_
    return count, grid_

base, _ = get_count()
cheats_saving_100ps = 0

hist = defaultdict(int)

for n in range(base):
    for direction in DIRECTIONS.values():
        count, grid_ = get_count(n, direction)
        # if count and count < base:
        #     hist[base-count] += 1
        #     for line in grid_:
        #         print(''.join(line))
        #     print(n, count - base)
        if count and count <= base - 100:
            cheats_saving_100ps += 1
            for line in grid_:
                print(''.join(line))
    print(n, count, cheats_saving_100ps)

print(hist)