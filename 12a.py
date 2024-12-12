from collections import defaultdict
from dataclasses import dataclass
import math
from utils.download import get_input
from utils.parse import parse_input_simple, make_grid
from random import uniform
from enum import Enum, auto
from copy import deepcopy
from itertools import combinations, zip_longest
from functools import cache

DAY = 12

DIRECTIONS = [(1,0), (-1,0), (0,1),(0,-1)]

get_input(DAY)
input = parse_input_simple(DAY)

grid, X, Y = make_grid(input, border=True)

@dataclass
class Field():
    code: str
    group: int | None
    perimeter: int
    x: int
    y: int

    def set_group(self, grid, group, code=None):
        if self.code == '-' or self.group:
            return grid
        if code==self.code or code is None:
            self.group = group
            for direction in DIRECTIONS:
                dx = direction[0]
                dy = direction[1]
                grid = grid[self.y+dy][self.x+dx].set_group(grid, group, self.code)

        return grid

    def set_perimeter(self, grid):
        if self.code == '-':
            return grid
        for direction in DIRECTIONS:
            dx = direction[0]
            dy = direction[1]
            if grid[y+dy][x+dx].code != self.code:
                self.perimeter += 1
        return grid

    def __repr__(self) -> str:
        return f"{self.code} {self.group} {self.perimeter} {self.x} {self.y}"

for x in range(0, X):
    for y in range(0, Y):
        code = grid[y][x]
        grid[y][x] = Field(code, None, 0, x, y)

group = 0
for x in range(1, X-1):
    for y in range(1, Y-1):
        group += 1
        grid = grid[y][x].set_group(grid, group)
        grid = grid[y][x].set_perimeter(grid)

group_sizes = defaultdict(int)
for x in range(1, X-1):
    for y in range(1, Y-1):
        group_sizes[grid[y][x].group] += 1

sum = 0
for x in range(1, X-1):
    for y in range(1, Y-1):
        sum += grid[y][x].perimeter * group_sizes[grid[y][x].group]

print(sum)
