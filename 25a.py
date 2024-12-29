from collections import defaultdict
from copy import deepcopy
from functools import cache
from utils.download import get_input
from utils.parse import parse_input_simple
from itertools import combinations
import re

DAY = 25

get_input(DAY)
input = parse_input_simple(DAY)

# print(input)

patterns = [[]]
keys = []
locks = []

for line in input:
    if line:
        patterns[-1].append(line)
    else:
        patterns.append([])

for pattern in patterns:
    heights = [0]*5
    if pattern[0] == '#####':
        for line in pattern[1:]:
            for idx, c in enumerate(line):
                if c == '#':
                    heights[idx] += 1
        locks.append(heights)
    else:
        for line in pattern[-2::-1]:
            for idx, c in enumerate(line):
                if c == '#':
                    heights[idx] += 1
        keys.append(heights)

result = 0
for key in keys:
    for lock in locks:
        if all(kh + lh <= 5 for kh, lh in zip(key, lock)):
            result += 1
    
print(result)