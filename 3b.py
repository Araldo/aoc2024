from utils.download import get_input
from utils.parse import parse_input_simple
import re

DAY = 3

get_input(DAY)
input = parse_input_simple(DAY)
input = 'do()' + ''.join(input) + 'don\'t()'
matches = re.findall(r"do\(\).*?don't\(\)", input)
input = ''.join(matches)

matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)
sum = 0
for match in matches:
    sum += int(match[0])*int(match[1])

print(sum)
