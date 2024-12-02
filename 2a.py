from utils.download import get_input
from utils.parse import parse_input_simple

DAY = 2

get_input(DAY)
input = parse_input_simple(DAY)

safe_rows = 0

for row in input:
    is_safe = True
    if row[0] > row[1]:
        max = -1
        min = -3
    else:
        max = 3
        min = 1
    for this, next in zip(row[:-1], row[1:]):
        if not (min <= (next - this) <= max):
            is_safe = False  
            break
    safe_rows += is_safe

print(safe_rows)
