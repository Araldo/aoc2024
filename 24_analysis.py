import networkx as nx
import matplotlib.pyplot as plt
from utils.download import get_input
from utils.parse import parse_input_simple
import re

G = nx.Graph()

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

for node in set(
    list(nodes.keys()) +
    list(node[0] for node in ops) +
    list(node[2] for node in ops) +
    list(node[3] for node in ops)
):
    G.add_node(node)

for edge in set(
    list((node[0], node[3],) for node in ops) + 
    list((node[2], node[3],) for node in ops)
):
    G.add_edge(*edge)

subax = plt.subplot(111)
nx.draw(G, with_labels=True, font_weight='bold', pos=nx.kamada_kawai_layout(G))
plt.show()
