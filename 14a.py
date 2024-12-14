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

DAY = 14


get_input(DAY)
input = parse_input_simple(DAY)

X = 101
Y = 103

q = [0,0,0,0]

for row in input:
    if match := re.match(r'p=(\d+),(\d+)', row):
        x, y = [int(v) for v in match.groups(1)]
    if match := re.match(r'.*v=(\-?\d+),(\-?\d+)', row):
        vx, vy = [int(v) for v in match.groups(1)]

    x = (x + 100 * vx) % X
    y = (y + 100 * vy) % Y
    
    if x < (X // 2):
        if y < (Y // 2):
            q[0] += 1
        elif y > (Y // 2):
            q[2] += 1
    elif x > (X // 2):
        if y < (Y // 2):
            q[1] += 1
        elif y > (Y // 2):
            q[3] += 1

q_mult = 1
for q in q:
    q_mult *= q

print(q_mult)