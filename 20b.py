from utils.download import get_input
from utils.parse import parse_input_simple, make_grid

DAY = 20

DIRECTIONS = {
    ">": (1, 0),
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
}

get_input(DAY)
input = parse_input_simple(DAY)
grid, X, Y = make_grid(input)

START = (0,0)
END = (0,0)

for x in range(X):
    for y in range(Y):
        if grid[y][x] == "S":
            START = (x, y)
        if grid[y][x] == "E":
            END = (x, y)

dir_at_pos = {}

def get_count():
    pos_count = {}

    x, y = START
    last_direction = None
    count = 0
    while (x, y) != END:
        pos_count[(x, y)] = count
        for direction in DIRECTIONS.values():
            if last_direction == (-direction[0], -direction[1]):
                continue
            dx, dy = direction
            if (0 <= x < X) and (0 <= y < Y) and grid[dy+y][dx+x] in ('.', 'E'):
                count += 1
                last_direction = direction
                x, y = (dx+x, dy+y)
                break

    pos_count[END] = count

    pos_count_reverse = {}
    for a,b in pos_count.items():
        pos_count_reverse[b] = a

    return pos_count, pos_count_reverse


def get_shortcut_saving(step, direction, base, base_reverse):
    origin = base_reverse[step]
    target = (origin[0] + direction[0], origin[1] + direction[1])
    if target in base:
        return step - base[target] + abs(direction[0])+ abs(direction[1])

base, base_reverse = get_count()
max_count = max(base.values())
count = 0

directions = [(x,y) for x in range(-20, 21) for y in range(-20, 21) if 1 < (abs(x) + abs(y)) <= 20]
for step in range(max_count):
    for direction in directions:
        if (saving := get_shortcut_saving(step, direction, base, base_reverse)) and saving <= -100:
            count += 1

print(count)

