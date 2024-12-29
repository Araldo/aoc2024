from utils.download import get_input
from utils.parse import parse_input_simple
import re

DAY = 24
NODE_PATTERN = r"([a-z0-9]{3})"

get_input(DAY)
input = parse_input_simple(DAY)
ops = []
nodes = {}

for line in input:
    if match := re.match(
        f"{NODE_PATTERN} ((?:XOR|AND|OR)) {NODE_PATTERN} -> {NODE_PATTERN}", line
    ):
        ops.append(list(match.groups()))

stages = []
for _ in range(46):
    stages.append(set())

for op in ops:
    if op[0].startswith('x') or op[0].startswith('y'):
        idx = int(op[0][1:])
        stages[idx].add(tuple(op))
        for op2 in ops:
            if op[3] == op2[0] or op[3] == op2[2]:
                stages[idx].add(tuple(op2))
    if op[3].startswith('z'):
        idx = int(op[3][1:])
        stages[idx].add(tuple(op))

errors = []

for stage in stages[1:-2]:
    for op in stage:
        if op[3].startswith('z') and op[1] != 'XOR':
            errors.append(op[3])
            for op in stage:
                if op[1] == 'XOR' and not (op[0].startswith('x') or op[0].startswith('y')):
                    errors.append(op[3])
        elif op[1] == 'XOR' and (op[0].startswith('x') or op[0].startswith('y')):
            node = op[3]
            for op in stage:
                if op[1] == 'XOR' and not (op[0].startswith('x') or op[0].startswith('y')) and node != op[0] and node != op[2]:
                    errors.append(node)
        elif op[1] == 'AND' and (op[0].startswith('x') or op[0].startswith('y')):
            node = op[3]
            for op in stage:
                if op[1] == 'XOR' and not (op[0].startswith('x') or op[0].startswith('y')) and (node == op[0] or node == op[2]):
                    errors.append(node)

errors.sort()
print(','.join(errors))
