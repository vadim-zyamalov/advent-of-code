MOD31 = (1 << 31) - 1
MOD16 = (1 << 16) - 1


def generate(i, factor, mod=MOD31):
    return (i * factor) % mod


if __name__ == "__main__":
    with open("_inputs/2017/day-15/input.txt", "r", encoding="utf8") as f:
        inits = []
        for line in f:
            tmp = line.strip().split()
            inits.append(int(tmp[-1]))

    total = 0
    i1, i2 = inits

    for _ in range(40_000_000):
        if (i1 & MOD16) == (i2 & MOD16):
            total += 1
        i1, i2 = generate(i1, 16807), generate(i2, 48271)

    print(f"Part 1: {total}")

    total = 0
    i1, i2 = inits
    for _ in range(5_000_000):
        while (i1 := generate(i1, 16807)) % 4 != 0:
            pass
        while (i2 := generate(i2, 48271)) % 8 != 0:
            pass
        if (i1 & MOD16) == (i2 & MOD16):
            total += 1

    print(f"Part 2: {total}")
