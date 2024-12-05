from utils.download import get_input
from utils.parse import parse_input_simple
from random import uniform

DAY = 5

get_input(DAY)
input = parse_input_simple(DAY)

pairs = []

for idx, line in enumerate(input):
    if not line:
        books = [pages.split(',') for pages in input[idx+1:]]
        break
    pairs.append(line.split('|'))

sum = 0
for book in books:
    book = {page: 0 for page in book}
    for pair in pairs:
        if pair[0] in book and pair[1] in book:
            book[pair[0]] += 1
    if list(book.values()) != sorted(list(book.values()), reverse=True):
        for page, count in book.items():
            if count == len(book) // 2:
                sum += int(page)

print(sum)