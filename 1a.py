from utils.download import get_input
from utils.parse import parse_input_simple

DAY = 1

get_input(DAY)
input = parse_input_simple(DAY)

list1 = []
list2 = []

for row in input:
    list1.append(row[0])
    list2.append(row[1])

list1.sort()
list2.sort()

sum = 0
for a, b in zip(list1, list2):
    sum += abs(a - b)

print(sum)
