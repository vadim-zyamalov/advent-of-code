def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    return int(abs(a) / gcd(a, b) * abs(b))


def lcmm(nums: list[int]) -> int:
    if not nums:
        return 1
    num = nums.pop(0)
    return lcm(num, lcmm(nums))


def part1(moves: dict, prog: str, beg="AAA", fin="ZZZ") -> int:
    N = len(prog)
    res = 0
    i = 0
    cur = beg

    while not cur.endswith(fin):
        cur = moves[cur][prog[i]]
        i = (i + 1) % N
        res += 1

    return res


def part2(moves: dict, prog: str, beg="A", fin="Z") -> int:
    beg = [el for el in moves.keys() if el.endswith(beg)]

    res = [part1(moves, prog, beg=el, fin=fin) for el in beg]

    return lcmm(res)


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
