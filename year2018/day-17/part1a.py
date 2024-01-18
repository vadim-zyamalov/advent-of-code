import sys
from typing import NamedTuple


sys.setrecursionlimit(10000)


class Pos(NamedTuple("Pos", [("x", int), ("y", int)])):
    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)


def fill(
    pos: Pos, clay: set[Pos], water: set[Pos], still: set[Pos], max_y: int
):
    water.add(pos)

    nxt = pos + Pos(0, 1)
    if nxt not in clay and nxt not in water and nxt.y <= max_y:
        fill(nxt, clay, water, still, max_y)
    if nxt not in clay and nxt not in still:
        return False

    nxt = pos + Pos(-1, 0)
    l_blocked = (nxt in clay) or (
        nxt not in water and fill(nxt, clay, water, filled, max_y)
    )
    nxt = pos + Pos(1, 0)
    r_blocked = (nxt in clay) or (
        nxt not in water and fill(nxt, clay, water, filled, max_y)
    )

    if l_blocked and r_blocked:
        still.add(pos)

        nxt = pos
        while nxt in water:
            still.add(nxt)
            nxt += Pos(-1, 0)

        nxt = pos
        while nxt in water:
            still.add(nxt)
            nxt += Pos(1, 0)

    return l_blocked or r_blocked


def dump(bounds, clay, drops):
    min_x, max_x, max_y = bounds
    for y in range(0, max_y + 1):
        for x in range(min_x, max_x + 1):
            if Pos(x, y) in clay:
                print("#", end="")
            elif Pos(x, y) in drops:
                print("~", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    spring = Pos(500, 0)

    drops = set()
    clay = set()
    min_y, max_y = 1_000_000, -1_000_000
    min_x, max_x = 1_000_000, -1_000_000

    with open("_inputs/2018/day-17/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break

            fst, snd = line.split(",")
            fst_ax, fst_coord = fst.strip().split("=")
            fst_coord = int(fst_coord)
            _, snd_coords = snd.strip().split("=")
            snd_coords = sorted(int(el) for el in snd_coords.split(".."))
            snd_coords[1] += 1

            for coord in range(*snd_coords):
                if fst_ax == "x":
                    clay.add(Pos(fst_coord, coord))
                    min_y = min(min_y, coord)
                    max_y = max(max_y, coord)
                    min_x = min(min_x, fst_coord)
                    max_x = max(min_x, fst_coord)
                else:
                    clay.add(Pos(coord, fst_coord))
                    min_y = min(min_y, fst_coord)
                    max_y = max(max_y, fst_coord)
                    min_x = min(min_x, coord)
                    max_x = max(min_x, coord)

    water = set()
    filled = set()
    fill(spring, clay, water, filled, max_y)
    print(
        f"Part 1: {len([pos for pos in (water | filled) if min_y <= pos.y <= max_y])}"
    )
    print(f"Part 2: {len(filled)}")
