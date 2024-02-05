DIR = {"u": -1, "d": 1, "l": -1j, "r": 1j}

TURNS = {
    "u": ("l", "r", "d"),
    "d": ("r", "l", "u"),
    "l": ("d", "u", "r"),
    "r": ("u", "d", "l"),
}

WEAK = set()
INFD = set()
FLAG = set()


def step(cur, dir):
    status = 0
    tl, tr, _ = TURNS[dir]
    if cur in INFD:
        ndir = tr
        INFD.remove(cur)
    else:
        ndir = tl
        INFD.add(cur)
        status = 1
    ncur = cur + DIR[ndir]
    return ncur, ndir, status


def evilstep(cur, dir):
    status = 0
    tl, tr, rv = TURNS[dir]
    if cur in WEAK:
        ndir = dir
        WEAK.remove(cur)
        INFD.add(cur)
        status = 1
    elif cur in INFD:
        ndir = tr
        INFD.remove(cur)
        FLAG.add(cur)
    elif cur in FLAG:
        ndir = rv
        FLAG.remove(cur)
    else:
        ndir = tl
        WEAK.add(cur)
    ncur = cur + DIR[ndir]
    return ncur, ndir, status


def part1(start, n=10_000):
    total = 0
    cur = start
    dir = "u"
    for _ in range(n):
        cur, dir, stat = step(cur, dir)
        total += stat
    print(f"Part 1: {total}")


def part2(start, n=10_000_000):
    total = 0
    cur = start
    dir = "u"
    for _ in range(n):
        cur, dir, stat = evilstep(cur, dir)
        total += stat
    print(f"Part 2: {total}")


if __name__ == "__main__":
    with open("_inputs/2017/day-22/input.txt", "r", encoding="utf8") as f:
        i, j = 0, 0
        for line in f:
            line = line.strip()
            j = 0
            for el in line:
                if el == "#":
                    INFD.add(complex(i, j))
                j += 1
            i += 1
        ni, nj = i, j
    cur = complex(ni // 2, nj // 2)

    INFD_bk = INFD.copy()

    part1(cur)

    INFD = INFD_bk

    part2(cur)
