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

DAY = 11

get_input(DAY)
input = tuple(parse_input_simple(DAY)[0])

@cache
def new_stones(stones: tuple[int]) -> tuple[int]:
    result = []
    for stone in stones:
        if stone == 0:
            result += [1]
        elif len(str(stone)) % 2 == 0:
            str_repr = str(stone)
            half = len(str_repr) // 2
            result += [int(str_repr[:half]), int(str_repr[half:])]
        else:
            result += [stone * 2024]
    return tuple(result)

for i in range(25):
    input = new_stones(input)

print(len(input))