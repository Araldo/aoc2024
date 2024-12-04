from utils.download import get_input
from utils.parse import parse_input_simple

DAY = 4

get_input(DAY)
input = parse_input_simple(DAY)
# input + border
grid = [['-'] + [char for char in line] + ['-'] for line in ['-' * len(input[0])] + input + ['-' * len(input[0])]]

string = "AMSMS"
directions=[]

for i in range(-1, 2, 2):
    for j in range(-1, 2, 2):
        directions.append(
            [(0,0), (i, i), (-i, -i), (j, -j), (-j, j)],
        )

result = 0

for x, line in enumerate(grid):
    for y, cell in enumerate(line):
        for direction in directions:
            s = ""
            for idx, step_ in enumerate(direction):
                if string[idx] != grid[x + step_[0]][y + step_[1]]:
                    break
                if idx==len(direction) -1:
                    result += 1
            
print(result)
