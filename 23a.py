from collections import defaultdict
from utils.download import get_input
from utils.parse import parse_input_simple
from itertools import combinations

DAY = 23

get_input(DAY)
input = parse_input_simple(DAY)
input.sort()
connections = defaultdict(list)

for line in input:
    connections[line[:2]].append(line[-2:])
    connections[line[-2:]].append(line[:2])

tripples = set()

for src, dst in connections.items():
    for comb in  combinations(dst, 2):
        if comb[0] in connections[comb[1]]:
            tri = [src, comb[0], comb[1]]
            tri.sort()
            for c  in tri:
                if c.startswith('t'):
                    tripples.add(tuple(tri))
                    break

print(len(tripples))
            