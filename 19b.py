from utils.download import get_input
from utils.parse import parse_input_simple
from functools import cache

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
def number_of_designs_possible(design) -> int:
    if not design:
        return 1
    possible_towels = []
    for towel in towels:
        if design.startswith(towel):
            possible_towels.append(towel)

    sum = 0
    for towel in possible_towels:
        sum += number_of_designs_possible(design[len(towel):])
    return sum

print(sum(number_of_designs_possible(design) for design in designs))
