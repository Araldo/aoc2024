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

get_input(DAY)
input = parse_input_simple(DAY)
input = [value[0] for value in input]

@cache
def next(value):
    value = ((value * 64) ^ value) % (2 ** 24)
    value = ((value // 32) ^ value) % (2 ** 24)
    value = ((value * 2048) ^ value) % (2 ** 24)
    return value

@cache
def get_values(value):
    values = [value]
    bananas = []
    changes = []
    for _ in range(2000):
        values.append(next(values[-1]))
        try:
            bananas.append(values[-1] % 10)
            changes.append(bananas[-1] - bananas[-2])
        except IndexError:
            pass
    return bananas, changes

from itertools import product 
from tqdm import tqdm

best = 0

for sequence in tqdm(list(product(list(range(-9,10)), repeat=4))):
    sum = 0
    print(best, sequence)
    for value in input:
        bananas, changes = get_values(value)
        for n in range(len(changes)-4):
            if changes[n:n+4] == sequence:
                sum += bananas[n+4]
                break
    if sum > best:
        print(best)
        best = sum
print(best)