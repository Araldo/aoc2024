from collections import defaultdict
from utils.download import get_input
from utils.parse import parse_input_simple
from itertools import combinations
import re

DAY = 24
NODE_PATTERN = r'([a-z0-9]{3})'

get_input(DAY)
input = parse_input_simple(DAY)

nodes = {}
skipped_lines = None

while skipped_lines != []:
    skipped_lines = []
    for line in input:
        if match := re.match(r'([a-z]\d\d): ([0-1])', line):
            nodes[match.groups()[0]] = int(match.groups()[1])
        elif match := re.match(f'{NODE_PATTERN} ((?:XOR|AND|OR)) {NODE_PATTERN} -> {NODE_PATTERN}', line):
            a = match.groups()[0]
            b = match.groups()[2]
            c = match.groups()[3]
            try:
                match match.groups()[1]:
                    case 'XOR': nodes[c] = nodes[a] ^ nodes[b]
                    case 'AND': nodes[c] = nodes[a] & nodes[b]
                    case 'OR': nodes[c] = nodes[a] | nodes[b]
            except:
                skipped_lines.append(line)

result = 0
for node, value in nodes.items():
    if value and re.match(r'z\d\d', node):
        result += 2**int(node[1:])

print(result)