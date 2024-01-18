STEP = 369

if __name__ == "__main__":
    spinlock = [0]
    pos = 0

    for i in range(1, 2017 + 1):
        pos = (pos + STEP) % i
        spinlock = spinlock[: (pos + 1)] + [i] + spinlock[(pos + 1) :]
        pos = (pos + 1) % (i + 1)

    print(f"Part 1: {spinlock[(pos + 1) % (2017 + 1)]}")

    pos = 0
    res = 0

    for i in range(1, 50_000_001):
        pos = (pos + STEP) % i
        if pos == 0:
            res = i
        pos = (pos + 1) % (i + 1)

    print(f"Part 2: {res}")
