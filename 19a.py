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

DAY = 19

get_input(DAY)
input = parse_input_simple(DAY)

towels = []
designs = []

towels = input[0].replace(' ','').split(',')
towels.sort()
towels = tuple(towels)
designs = input[2:]

@cache
def is_design_possible(design) -> bool:
    if design in towels:
        return True
    
    possible_towels = []
    for towel in towels:
        if design.startswith(towel):
            possible_towels.append(towel)
    
    return any(is_design_possible(design[len(towel):]) for towel in possible_towels)

print(sum(is_design_possible(design) for design in designs))
