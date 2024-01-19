from functools import cache
import heapq as hq
import time


class Pos(tuple):
    def __new__(cls, *x):
        return super().__new__(cls, tuple(x))

    def __add__(self, other):
        return Pos(self[0] + other[0], self[1] + other[1])

    @property
    def near(self):
        tmp = [self + d for d in [Pos(-1, 0), Pos(1, 0), Pos(0, -1), Pos(0, 1)]]
        return [p for p in tmp if (p[0] >= 0) and (p[1] >= 0)]


@cache
def ero_level(pos: Pos, tgt: Pos, depth: int):
    if (pos == Pos(0, 0)) or (pos == tgt):
        return (0 + depth) % 20183
    if pos[1] == 0:
        return (pos[0] * 16807 + depth) % 20183
    if pos[0] == 0:
        return (pos[1] * 48271 + depth) % 20183
    return (
        ero_level(pos + Pos(-1, 0), tgt, depth)
        * ero_level(pos + Pos(0, -1), tgt, depth)
        + depth
    ) % 20183


def part1(tgt, depth):
    result = 0
    for x in range(tgt[0] + 1):
        for y in range(tgt[1] + 1):
            result += ero_level(Pos(x, y), tgt, depth) % 3
    return result


def part2(tgt: Pos, depth: int):
    eqs = [0, 1, 2]

    def env(c):
        return ero_level(c, tgt, depth) % 3

    def heur(c):
        return abs(c[0] - tgt[0]) + abs(c[1] - tgt[1])

    queue: list[tuple[int, int, Pos, int]] = [
        (heur(Pos(0, 0)), 0, Pos(0, 0), 1)
    ]
    visited = set()

    while queue:
        _, dist, pos, eq = hq.heappop(queue)
        pos_type = env(pos)

        if pos == tgt:
            if eq == 1:
                return dist
            else:
                hq.heappush(queue, (dist + 7, dist + 7, pos, 1))

        if (pos, eq) in visited:
            continue
        visited.add((pos, eq))

        for nxt in pos.near:
            nxt_type = env(nxt)
            for nxt_eq in eqs:
                # Мы не можем перейти в следующую
                # клетку или находиться в текущей
                # с данным снаряжением.
                if (nxt_eq == nxt_type) or (nxt_eq == pos_type):
                    continue
                if nxt_eq == eq:
                    hq.heappush(
                        queue, (dist + 1 + heur(nxt), dist + 1, nxt, eq)
                    )
                else:
                    hq.heappush(
                        queue, (dist + 8 + heur(nxt), dist + 8, nxt, nxt_eq)
                    )


if __name__ == "__main__":
    with open("_inputs/2018/day-22/input.txt", "r", encoding="utf8") as f:
        depth = int(f.readline().strip().split()[1])
        tgt = Pos(*[int(i) for i in f.readline().strip().split()[1].split(",")])

    t0 = time.time()
    print(f"Part 1: {part1(tgt, depth)}")
    print(f"    took {time.time() - t0:.2f} secs")

    t0 = time.time()
    print(f"Part 2: {part2(tgt, depth)}")
    print(f"    took {time.time() - t0:.2f} secs")
