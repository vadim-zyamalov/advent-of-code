mod16 = 2 ** 16
mod31 = 2 ** 31 - 1


def gen0(i1, i2, f1=16807, f2=48271, mod=mod31):
    return (i1 * f1) % mod, (i2 * f2) % mod


def gen1(i, f=16807, mod=mod31, crit=4):
    while True:
        if i % crit == 0:
            return i
        i = (i * f) % mod


if __name__ == "__main__":
    with open("../../_inputs/2017/day-15/input.txt", "r", encoding="utf8") as f:
        inits = []
        for line in f:
            tmp = line.strip().split()
            inits.append(int(tmp[-1]))

    total = 0
    i1, i2 = inits
    for _ in range(40_000_000):
        if (i1 % mod16) == (i2 % mod16):
            total += 1
        i1, i2 = gen0(i1, i2)

    print(f"Part 1: {total}")

    total = 0
    i1, i2 = inits
    for _ in range(5_000_000):
        i1, i2 = gen1(i1, f=16807, crit=4), gen1(i2, f=48271, crit=8)
        if (i1 % mod16) == (i2 % mod16):
            total += 1
        i1, i2 = gen0(i1, i2)

    print(f"Part 2: {total}")
