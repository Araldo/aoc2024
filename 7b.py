from dataclasses import dataclass
import math
from utils.download import get_input
from utils.parse import parse_input_simple
from random import uniform
from enum import Enum, auto
from numpy import base_repr

DAY = 7

class Operation(Enum):
    MULTIPLY = auto()
    ADD = auto()
    CONCAT = auto()

@dataclass
class Row():
    total: int
    elements: list[int]
    length: int

class Operations():
    def __init__(self, encoded, length) -> None:
        self.encoded = encoded
        self.operations = []
        for op in base_repr(encoded, base=3).zfill(length):
            match op:
                case '0': self.operations.append(Operation.ADD)
                case '1': self.operations.append(Operation.MULTIPLY)
                case '2': self.operations.append(Operation.CONCAT)

    def evaluate(self, elements) -> int:
        sum = elements[0]
        for element, operation in zip(elements[1:], self.operations):
            match operation:
                case Operation.ADD: sum += element
                case Operation.MULTIPLY: sum *= element
                case Operation.CONCAT: sum = int(str(sum) + str(element))
        return sum

get_input(DAY)
input = parse_input_simple(DAY)

rows = []
for row in input:
    total, elements = row.split(':')
    total = int(total)
    elements = [int(element) for element in elements.strip().split()]
    rows.append(Row(total = total, elements = elements, length=len(elements)))

sum = 0
for row in rows:
    valid_row = False
    for i in range(int(math.pow(3, row.length - 1))):
        op = Operations(i, row.length-1)
        if op.evaluate(row.elements) == row.total:
            valid_row = True
            break
    if valid_row:
        sum += row.total
        continue

print(sum)