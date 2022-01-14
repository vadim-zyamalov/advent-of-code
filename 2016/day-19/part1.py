from math import log

INPUT = 3001330
# INPUT = 5


def JF1(n) -> int:
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * JF1(n // 2) - 1
    else:
        return 2 * JF1(n // 2) + 1


def JF2(n) -> int:
    if n == 1:
        return 1
    lower = int(log(n - 1) / log(3))
    if 3 ** lower < n <= 2 * 3 ** lower:
        return n - 3 ** lower
    else:
        return 2 * n - 3 * 3 ** lower


def circle_steal(elf, length, circle):
    idx = circle.index(elf)
    circle.remove(circle[(idx + length // 2) % length])


def next_elf(elf, length, circle):
    idx = circle.index(elf)
    return circle[(idx + 1) % length]


print(f"Part 1: {JF1(INPUT)}")

print(f"Part 2: {JF2(INPUT)}")
