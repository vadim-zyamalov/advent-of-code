vents1 = {}
vents2 = {}


def counter(line, vents, nodiag=False):
    start, _, end = line.partition('->')
    x1, y1 = [int(i) for i in start.strip().split(',')]
    x2, y2 = [int(i) for i in end.strip().split(',')]
    if nodiag and (x1 != x2) and (y1 != y2):
        return vents
    xstep = 1 if x1 < x2 else -1 if x1 > x2 else 0
    ystep = 1 if y1 < y2 else -1 if y1 > y2 else 0
    x, y = x1, y1
    for _ in range(
            max(abs(x1 - x2),
                abs(y1 - y2)) + 1):
        if (x, y) in vents:
            vents[(x, y)] += 1
        else:
            vents[(x, y)] = 1
        x += xstep
        y += ystep
    return vents


with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        vents1 = counter(line, vents1, True)
        vents2 = counter(line, vents2, False)

answer = 0
for key, val in vents1.items():
    if val > 1:
        answer += 1

print(f"Part 1: {answer}")

answer = 0
for key, val in vents2.items():
    if val > 1:
        answer += 1

print(f"Part 2: {answer}")
