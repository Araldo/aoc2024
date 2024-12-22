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

DAY = 22

DIRECTIONS = {
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
}

get_input(DAY)
input = parse_input_simple(DAY)
input = [value[0] for value in input]

def next(value):
    value = ((value * 64) ^ value) % (2 ** 24)
    value = ((value // 32) ^ value) % (2 ** 24)
    value = ((value * 2048) ^ value) % (2 ** 24)
    return value

sum = 0
for value in input:
    for n in range(2000):
        value = next(value)
    sum += value

print(sum)