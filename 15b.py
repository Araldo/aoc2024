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


X = len(grid[0])
Y = len(grid)
old_grid = grid
grid = []

for y in range(Y):
    grid.append([])
    for x in range(X):
        if old_grid[y][x] == ".":
            grid[-1].append(".")
            grid[-1].append(".")
        if old_grid[y][x] == "@":
            grid[-1].append("@")
            grid[-1].append(".")
        if old_grid[y][x] == "#":
            grid[-1].append("#")
            grid[-1].append("#")
        if old_grid[y][x] == "O":
            grid[-1].append("[")
            grid[-1].append("]")

X = len(grid[0])
Y = len(grid)
movements = "".join(movements)

for x in range(X):
    for y in range(Y):
        if grid[y][x] == "@":
            loc = (x, y)

for idx, movement in enumerate(movements):
    time.sleep(0.01)
    if movement in (">", "<"):
        can_move = False
        blocked = False
        next_x = loc[0]
        next_y = loc[1]
        count = 0

        while not blocked and not can_move:
            count += 1
            next_x += DIRECTIONS[movement][0]
            next_y += DIRECTIONS[movement][1]
            if grid[next_y][next_x] == "#":
                blocked = True
            elif grid[next_y][next_x] == ".":
                can_move = True

        if can_move:
            if movement == '>':
                fields = "@" + "[]" * ((count - 1) // 2)
            else:
                fields = "@" + "][" * ((count - 1) // 2)
            grid[loc[1]][loc[0]] = "."
            next_x = loc[0]
            next_y = loc[1]
            for i in range(count):
                next_x += DIRECTIONS[movement][0]
                next_y += DIRECTIONS[movement][1]
                grid[next_y][next_x] = fields[i]
                if i == 0:
                    loc = (next_x, next_y)
    else:
        can_move = False
        blocked = False
        front = [loc]

        affected = [(loc[0],loc[1],'@')]
        all_free = False

        while not all_free and not blocked:
            all_free = True
            new_front = []
            for field in front:
                y = field[1] + DIRECTIONS[movement][1]
                x = field[0] + DIRECTIONS[movement][0]
                if grid[y][x] == "#":
                    all_free = False
                    blocked = True
                if grid[y][x] == "[":
                    affected += [(x, y, "["), (x + 1, y, "]")]
                    all_free = False
                    new_front.append((x, y))
                    new_front.append((x + 1, y))
                if grid[y][x] == "]":
                    affected += [(x, y, "]"), (x - 1, y, "[")]
                    all_free = False
                    new_front.append((x, y))
                    new_front.append((x - 1, y))
            front = new_front

        if all_free:
            for affect in affected:
                grid[affect[1]][affect[0]] = "."
            for affect in affected:
                grid[affect[1] + DIRECTIONS[movement][1]][affect[0] + DIRECTIONS[movement][0]] = affect[2]
            loc = (affected[0][0]+DIRECTIONS[movement][0], affected[0][1]+DIRECTIONS[movement][1])

    for line in grid:
        print("".join(line))

sum = 0
for x in range(X):
    for y in range(Y):
        if grid[y][x] == "[":
            sum += y * 100 + x
print(sum)
