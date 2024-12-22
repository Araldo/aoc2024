from collections import defaultdict
from utils.download import get_input
from utils.parse import parse_input_simple

DAY = 21

get_input(DAY)
input = parse_input_simple(DAY)

MAP_NUM = {
    '0A': '>A',
    '96': 'vA',
    '65': '<A',
    '5A': 'vv>A',
    '14': '^A',
    '43': 'v>>A',
    '3A': 'vA',
    '52': 'vA',
    'A6': '^^A',
    '28': '^^A',
    '8A': 'vvv>A',
    '70': '>vvvA',
    '67': '<<^A',
    '97': '<<A',
    '73': 'vv>>A',
    'A9': '^^^A',
    'A1': '^<<A',
    'A5': '<^^A'
}

MAP_CUR = {
    'A<': 'v<<A',
    'A>': 'vA',
    'A^': '<A',
    'Av': '<vA',
    '<<': 'A',
    '>>': 'A',
    '^^': 'A',
    'vv': 'A',
    '<>': '>>A',
    '<^': '>^A',
    '<v': '>A',
    'v<': '<A',
    'v^': '^A',
    'v>': '>A',
    '>v': '<A',
    '><': '<<A',
    '>^': '<^A',
    '^<': 'v<A',
    '^v': 'vA',
    '^>': 'v>A',
    '<A': '>>^A',
    'vA': '^>A',
    '^A': '>A',
    '>A': '^A',
    'AA': 'A'
}

sum = 0

for code in input:
    original_code = code
    code = 'A' + code
    new_code = []
    for n in range(1, len(code)):
        new_code.append(MAP_NUM[code[n-1:n+1]])
    
    hist = defaultdict(int)
    for c in new_code:
        hist[c] += 1

    for _ in range(25):
        new_hist = defaultdict(int)
        for pattern, count in hist.items():
            pattern = 'A' + pattern
            for a, b in zip(pattern[:-1], pattern[1:]):
                new_hist[MAP_CUR[a+b]] += count

        hist = new_hist

    for a,b in new_hist.items():
        sum += len(a)*b*int(original_code.replace('A', ''))

print(sum)
