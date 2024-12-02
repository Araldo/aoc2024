from utils.download import get_input
from utils.parse import parse_input_simple

DAY = 2

get_input(DAY)
input = parse_input_simple(DAY)

safe_rows = 0

        
for row_org in input:
    # O(n*m), but the lines are not that long, so it doesn't matter 
    for remove_item in range(-1, len(row_org)):
        if remove_item > -1:
            row = row_org.copy()
            row.pop(remove_item)
        else:
            row = row_org
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
        if is_safe:
            safe_rows += 1
            break

print(safe_rows)
