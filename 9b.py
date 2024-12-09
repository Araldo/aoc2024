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
layout_length = 0
empty_blocks = []
file_blocks = []

for idx, (file, empty) in enumerate(zip_longest(disk[::2], disk[1::2])):
    file_blocks.append((layout_length, int(file)))
    layout_length += int(file)
    if empty:
        empty_blocks.append((layout_length, int(empty)))
        layout_length += int(empty)

pointer = len(file_blocks) -1

while pointer > 0:
    file = file_blocks[pointer]
    for idx, empty_block in enumerate(empty_blocks):
        if file[0] <= empty_block[0]:
            break
        if empty_block[1] >= file[1]:
            empty_blocks[idx] = (empty_block[0]+file[1], empty_block[1]-file[1])
            file_blocks[pointer] = (empty_block[0], file[1])
            break
    pointer -= 1

sum = 0
file_id = 0
for file in file_blocks:
    for idx in range(file[0], file[1] + file[0]):
        sum += idx * file_id
    file_id += 1

print(sum)
