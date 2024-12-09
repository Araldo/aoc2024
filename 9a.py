from collections import defaultdict
from dataclasses import dataclass
import math
from utils.download import get_input
from utils.parse import parse_input_simple, make_grid
from random import uniform
from enum import Enum, auto
from copy import deepcopy
from itertools import combinations, zip_longest

DAY = 9

get_input(DAY)
input = parse_input_simple(DAY)
grid, X, Y = make_grid(input)
disk = grid[0]
layout = []

for idx, (file, empty) in enumerate(zip_longest(disk[::2], disk[1::2])):
    layout += [idx]*int(file)
    if empty:
        layout += ['.']*int(empty)

head = 0
tail = len(layout) - 1

while head < tail:
    if layout[head] == '.':
        if layout[tail] != '.':
            layout[head] = layout[tail]
            layout[tail] = '.'
            head += 1
            tail -= 1
        else:
            tail -= 1
    else:
        head += 1

sum = 0
for idx, element in enumerate(layout):
    if element == '.':
        break
    else:
        sum += idx * element

print(sum)