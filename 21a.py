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
    new_code = ''
    for n in range(1, len(code)):
        new_code += MAP_NUM[code[n-1:n+1]]
    
    for _ in range(2):
        code = 'A' + new_code
        new_code = ''
        for n in range(1, len(code)):
            new_code += MAP_CUR[code[n-1:n+1]]
            
    sum += len(new_code) * int(original_code.replace('A', ''))

print(sum)