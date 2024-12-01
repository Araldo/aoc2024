from utils.download import get_input
from utils.parse import parse_input_simple
from collections import Counter

DAY = 1

get_input(DAY)
input = parse_input_simple(DAY)

sum = 0

list1 = []
list2 = []

for row in input:
    list1.append(row[0])
    list2.append(row[1])

list2_count = Counter(list2)

for item in list1:
    sum += list2_count[item] * item

print(sum)
