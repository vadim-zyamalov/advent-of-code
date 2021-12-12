from math import sqrt

with open("input.txt", "r") as f:
    goal = int(f.readline().strip())


def factor(x):
    j = 2
    while x > 1:
        for i in range(j, int(sqrt(x + 0.05)) + 1):
            if x % i == 0:
                x /= i
                j = i
                yield int(i)
                break
        else:
            if x > 1:
                yield int(x)
                break


i = 0
while True:
    i += 1

    result = 10

    factors = []
    for f in factor(i):
        factors.append(f)

    steps = int(2 ** (len(factors)) - 1)

    visited = []
    for step in range(1, steps + 1):
        tmp = 1
        for shift in range(len(factors)):
            if 1 & (step>>shift):
                tmp *= factors[len(factors) - 1 - shift]
        if tmp not in visited:
            result += 10 * tmp
            visited.append(tmp)

    if i < 10:
        print(result)
    if result >= goal:
        print(result)
        break

print("Part 1: {}".format(i))
