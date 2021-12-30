INPUT = 3001330
# INPUT = 5

def JF(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2 * JF(n // 2) - 1
    if n % 2 == 1:
        return 2 * JF(n // 2) + 1


def circle_steal(elf, length, circle):
    idx = circle.index(elf)
    circle.remove(circle[(idx + length // 2) % length])


def next_elf(elf, length, circle):
    idx = circle.index(elf)
    return circle[(idx + 1) % length]


print(f"Part 1: {JF(INPUT)}")

CIRCLE = [i for i in range(1, INPUT + 1)]
circle_len = INPUT
current = 1

while circle_len > 1:
    circle_steal(current, circle_len, CIRCLE)
    circle_len -= 1
    current = next_elf(current, circle_len, CIRCLE)

print(f"Part 2: {CIRCLE[0]}")
