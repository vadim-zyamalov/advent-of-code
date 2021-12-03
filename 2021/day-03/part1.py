from operator import add

total = 0
count = []

with open("input.txt", "r") as f:
    for line in f:
        total += 1
        tmp = []
        for digit in line.strip():
            if digit == '0':
                tmp.append(0)
            else:
                tmp.append(1)
        if not count:
            count = tmp
        else:
            count = list(map(add, count, tmp))

gamma = int(
    '0b' + ''.join(['1' if i >= total / 2 else '0' for i in count]),
    2)
epsilon = int(
    '0b' + ''.join(['1' if i < total / 2 else '0' for i in count]),
    2)

print(gamma * epsilon)
