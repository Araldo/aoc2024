# Run with pypy in ~1 hour. Regular python ~100 hours

from itertools import product

def parse_input_simple(day, type):
    assert 1 <= day <= 25
    with open(str(day) + ".txt", "r") as file:
        data = str(file.readlines()[0])[2:]
        data = data.split("\\n")[:-1]
        try:
            data = [[type(str(item)) for item in line.split()] for line in data]
        except ValueError:
            return data
    return data

DAY = 22

input = parse_input_simple(DAY, int)
input = [value[0] for value in input]

# @cache
def next(value):
    value = ((value * 64) ^ value) % (2 ** 24)
    value = ((value // 32) ^ value) % (2 ** 24)
    value = ((value * 2048) ^ value) % (2 ** 24)
    return value


best = 0

for sequence in list(product(list(range(-9,10)), repeat=4)):
    sum = 0
    print(best, sequence)

    # Really shouldn't be calculated in each loop, but cannot be bothered to optimize it.
    for value in input:
        values = [value]
        bananas = []
        changes = []
        for n in range(2000):
            values.append(next(values[-1]))
            try:
                bananas.append(values[-1] % 10)
                changes.append(bananas[-1] - bananas[-2])
                if changes[-4:] == list(sequence):
                    sum += bananas[-1]
                    break
            except IndexError:
                pass
    if sum > best:
        print(best)
        best = sum

print(best)