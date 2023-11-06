h = 0

b = 79
c = b

b = 107900
c = 124900

while b <= c:
    f = 1

    for d in range(2, b // 2):
        if b % d == 0:
            f = 0
            break

    if f == 0:
        h += 1

    b += 17

print(f"Part 2: {h}")
