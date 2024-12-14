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
import re

DAY = 13


get_input(DAY)
input = parse_input_simple(DAY)
input.append('')

class Solve():
    def __init__(self, data) -> None:
        for line, label in zip(data, ('Button A', 'Button B', 'Prize')):
            if match := re.match(rf'{label}: X.(\d+), Y.(\d+)', line):
                x = int(match.group(1))
                y = int(match.group(2))
                if label == 'Button A':
                    ax, ay = x, y
                elif label == 'Button B':
                    bx, by = x, y
                else:
                    px, py = x + 10000000000000, y + 10000000000000

        self.result = self.solve(ax, ay, bx, by, px, py)
                    
    def solve(self, ax, ay, bx, by, px, py):
        a = -((by*px)-(bx*py))/((ay*bx)-(ax*by))
        b = -((ax*py)-(ay*px))/((ay*bx)-(ax*by))
        
        if not (a % 1) and not (b % 1):
            return 3 * a + b 
        else:
            return 0

buffer = []
sum = 0

for line in input:
    if line:
        buffer.append(line)
    else:
        eq = Solve(buffer)
        sum += eq.result
        buffer = []

print(int(sum))