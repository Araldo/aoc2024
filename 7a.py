from dataclasses import dataclass
import math
from utils.download import get_input
from utils.parse import parse_input_simple
from random import uniform
from enum import Enum, auto

DAY = 7

class Operation(Enum):
    MULTIPLY = auto()
    ADD = auto()

@dataclass
class Row():
    total: int
    elements: list[int]
    length: int

class Operations():
    def __init__(self, encoded, length) -> None:
        self.encoded = encoded
        self.operations = []
        for op in bin(encoded)[2:].zfill(length):
            if op == '1':
                self.operations.append(Operation.ADD)
            else:
                self.operations.append(Operation.MULTIPLY)

    def evaluate(self, elements) -> int:
        sum = elements[0]
        for element, operation in zip(elements[1:], self.operations):
            if operation == Operation.ADD:
                sum += element
            else:
                sum *= element
        return sum

get_input(DAY)
input = parse_input_simple(DAY)

rows = []
for row in input:
    total, elements = row.split(':')
    total = int(total)
    elements = [int(element) for element in elements.strip().split()]
    rows.append(Row(total = total, elements = elements, length=len(elements)))

# brute force approach
# a better way would be to start from the back: to allow the last operation to be '*', the total must have
# the element as a factor. E.g. 123 with elements [10, 2, 20, 3]: 123 % 3 == 0, which means the last operation can be both * and +.
# Working back from the tail, if the last operation was *, it leaves 41: 41 % 20 != 0, which means ?** is not possible. The other part of 
# the tree: if the last is '+': 120 % 20 == 0, so .*+ is possible. .++ is possible in any case, but it can also be pruned by checking if
# the max. value for the remaining part multiplied is sufficient to reach the value. Also when the intermediate sum already exceeds the 
# target value, that part of the tree can be pruned. 

sum = 0
for row in rows:
    valid_row = False
    for i in range(int(math.pow(2, row.length - 1))):
        op = Operations(i, row.length-1)
        if op.evaluate(row.elements) == row.total:
            valid_row = True
            break
    if valid_row:
        sum += row.total
        continue

print(sum)