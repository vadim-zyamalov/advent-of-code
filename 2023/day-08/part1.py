from numpy import lcm, int64


def part1(moves: dict, prog: str) -> int:
    N = len(prog)
    res = 0
    i = 0
    cur = "AAA"

    while cur != "ZZZ":
        cur = moves[cur][prog[i]]
        i = (i + 1) % N
        res += 1

    return res


def part2_single(moves: dict, prog: str, beg="AAA") -> int:
    N = len(prog)
    res = 0
    i = 0
    cur = beg

    while not cur.endswith("Z"):
        cur = moves[cur][prog[i]]
        i = (i + 1) % N
        res += 1

    return res


def part2(moves: dict, prog: str) -> int:
    beg = [el for el in moves.keys() if el.endswith("A")]

    res = [part2_single(moves, prog, beg=el) for el in beg]

    return lcm.reduce(res, dtype=int64)


if __name__ == "__main__":
    moves = {}

    with open("_inputs/2023/day-08/input.txt", "r", encoding="utf8") as f:
        prog = f.readline().strip()
        f.readline()

        for line in f:
            if line.strip() == "":
                break

            cur, lr = line.split("=")
            cur = cur.strip()
            l, r = lr.strip().strip("()").split(",")

            moves[cur] = {"L": l.strip(), "R": r.strip()}

    res = part1(moves, prog)
    print(f"Part 1: {res}")

    res = part2(moves, prog)
    print(f"Part 2: {res}")
