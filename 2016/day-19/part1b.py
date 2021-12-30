from math import log

INPUT = 3001330
# INPUT = 5


def JF(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * JF(n // 2) - 1
    if n % 2 == 1:
        return 2 * JF(n // 2) + 1


def JF2(n):
    n -= 1
    if n == 0:
        return 1
    lower = int(log(n) / log(3))
    if 3 ** lower <= n < 2 * 3 ** lower:
        return n - 3 ** lower + 1
    else:
        return 2 * (n - 3 ** lower + 1) - 3 ** lower


def circle_steal(elf, length, circle):
    idx = circle.index(elf)
    circle.remove(circle[(idx + length // 2) % length])


def next_elf(elf, length, circle):
    idx = circle.index(elf)
    return circle[(idx + 1) % length]


print(f"Part 1: {JF(INPUT)}")

print(f"Part 2: {JF2(INPUT)}")
