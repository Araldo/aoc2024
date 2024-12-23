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

max_lan = 3
best_lan = []

i = 0

for src, dst in connections.items():
    options = [src] + dst
    for size in range(len(options), max_lan, -1):
        for lan in combinations(options, size):
            complete = True
            for duo in combinations(lan, 2):
                if duo[0] not in connections[duo[1]]:
                    complete = False
                    break
            if complete:
                max_lan = len(lan)
                best_lan = lan
                break
        if complete:
            break
                
best_lan = list(best_lan)
best_lan.sort()
print(','.join(best_lan))
