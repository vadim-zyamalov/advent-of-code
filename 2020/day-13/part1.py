from math import prod


def part1(t0, ids):
    minw = max(ids)
    bus = 0

    for period in ids:
        wait = -t0 % period
        if wait < minw:
            minw = wait
            bus = period

    return bus * minw


def part2_CRT(ids, rs):
    M = prod(ids)
    x = 0

    for ri, a in zip(rs, ids):
        x += (-ri % a) * (M // a) * pow(M // a, a - 2, a)

    return x % M


if __name__ == "__main__":
    with open("_inputs/2020/day-13/input.txt", "r", encoding="utf8") as f:
        t0 = int(f.readline())
        idx = []
        ids = []
        for i, el in enumerate(f.readline().strip().split(",")):
            if el == "x":
                continue
            idx.append(i)
            ids.append(int(el))

    print(f"Part 1: {part1(t0, ids)}")
    print(f"Part 2: {part2_CRT(ids, idx)}")
