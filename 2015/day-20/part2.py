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


elves = {}
i = 0
while True:
    i += 1

    result = 0

    if 1 not in elves:
        elves[1] = 0
    if elves[1] < 50:
        result += 11
        elves[1] += 1

    factors = []
    for f in factor(i):
        factors.append(f)

    steps = int(2 ** (len(factors)) - 1)

    visited = []
    for step in range(1, steps + 1):
        tmp = 1
        for shift in range(len(factors)):
            if 1 & (step >> shift):
                tmp *= factors[len(factors) - 1 - shift]
        if tmp not in visited:
            if tmp not in elves:
                elves[tmp] = 0
            if elves[tmp] < 50:
                result += 11 * tmp
                elves[tmp] += 1
            visited.append(tmp)

    if result >= goal:
        print(result)
        break

print("Part 2: {}".format(i))
