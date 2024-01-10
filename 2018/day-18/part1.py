from collections import Counter

ITERS = 1_000_000_000


class Pos(tuple):
    def __new__(cls, *x):
        return super().__new__(cls, tuple(x))

    def __add__(self, other):
        return Pos(self[0] + other[0], self[1] + other[1])

    def near(self, limit=(50, 50)):
        return [
            self + Pos(dx, dy)
            for dx in [-1, 0, 1]
            for dy in [-1, 0, 1]
            if ((dx != 0) or (dy != 0))
            and (0 <= self[0] + dx < limit[0])
            and (0 <= self[1] + dy < limit[1])
        ]


def update(area, limits):
    result = {}
    for pos, val in area.items():
        elems = Counter([area[p] for p in pos.near(limits)])
        match val:
            case 0:
                result[pos] = 1 if elems[1] >= 3 else 0
            case 1:
                result[pos] = 2 if elems[2] >= 3 else 1
            case _:
                result[pos] = 2 if (elems[1] >= 1) and (elems[2] >= 1) else 0
    return result


def _hash(area, limits):
    res = 0
    for x in range(limits[0]):
        for y in range(limits[1]):
            res = res * 3 + area[Pos(x, y)]
    return res


def count(area):
    elems = Counter([v for v in area.values()])
    return elems[1] * elems[2]


def dump(area, limits):
    for x in range(limits[0]):
        for y in range(limits[1]):
            match area[Pos(x, y)]:
                case 0:
                    print(".", end="")
                case 1:
                    print("|", end="")
                case 2:
                    print("#", end="")
        print()


if __name__ == "__main__":
    with open("_inputs/2018/day-18/input.txt", "r", encoding="utf8") as f:
        area = {}
        lines = f.read().strip("\n").split("\n")

        for x, row in enumerate(lines):
            for y, el in enumerate(row):
                pos = Pos(x, y)
                match el:
                    case "#":
                        area[pos] = 2
                    case "|":
                        area[pos] = 1
                    case _:
                        area[pos] = 0

    limits = max(area) + Pos(1, 1)

    cache = {}
    cycle_beg = -1
    cycle_len = 0

    for i in range(ITERS):
        area = update(area, limits)
        value = count(area)
        if i == 9:
            print(f"Part 1: {value}")
        hvalue = _hash(area, limits)
        if hvalue not in cache:
            cache[hvalue] = (i, value)
        else:
            cycle_beg, _ = cache[hvalue]
            cycle_len = i - cycle_beg
            break

    idx = (ITERS - cycle_beg) % cycle_len + (cycle_beg - 1)

    for i, v in cache.values():
        if i == idx:
            print(f"Part 2: {v}")
            break
