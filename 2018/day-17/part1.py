from typing import NamedTuple


class Pos(NamedTuple("Pos", [("x", int), ("y", int)])):
    def __add__(self, other):
        return type(self)(self.x + other.x, self.y + other.y)


def go_down(pos: Pos, clay: set[Pos], drops: set[Pos], bottom: int):
    while (pos.y < bottom) and pos + Pos(0, 1) not in (clay | drops):
        pos += Pos(0, 1)
    # print(f"Go down: {pos}")
    return pos


def go_side(pos: Pos, clay: set[Pos], drops: set[Pos], bounds, left=True):
    min_x, max_x = bounds
    dx = -1 if left else 1
    cur = pos
    while (
        (min_x < pos.x < max_x)
        and cur + Pos(dx, 0) not in (clay | drops)
        and cur + Pos(0, 1) in (clay | drops)
    ):
        cur += Pos(dx, 0)
    if cur + Pos(dx, 0) in (clay | drops):
        # print(f"Go {'left' if left else 'right'}: {cur}")
        return cur, True
    if cur + Pos(-dx, 1) in clay:
        return cur, True
    if cur + Pos(-2 * dx, 1) in clay:
        return cur + Pos(-dx, 0), True
    # print(f"Go {'left' if left else 'right'}: {pos}")
    return pos, False


def drop(
    spring: Pos, bounds: tuple[int, ...], clay: set[Pos], drops: set[Pos]
) -> bool:
    pos = spring
    moved = True

    min_x, max_x, max_y = bounds

    while moved:
        moved = False
        nxt = go_down(pos, clay, drops, max_y)
        if nxt != pos:
            moved = True
            pos = nxt
        else:
            break

        nxt_l, valid_l = go_side(pos, clay, drops, (min_x, max_x))
        nxt_r, valid_r = go_side(pos, clay, drops, (min_x, max_x), False)
        if valid_l and valid_r:
            if nxt_l < pos:
                moved = True
                pos = nxt_l
            elif nxt_r > pos:
                moved = True
                pos = nxt_r

    if pos != spring:
        # print(pos)
        drops.add(pos)
        return True

    return False


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
    max_y = 0
    min_x, max_x = 1_000_000, -1_000_000

    with open("_inputs/2018/day-17/sample.txt", "r", encoding="utf8") as f:
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
                    max_y = max(max_y, coord)
                    min_x = min(min_x, fst_coord)
                    max_x = max(min_x, fst_coord)
                else:
                    clay.add(Pos(coord, fst_coord))
                    max_y = max(max_y, fst_coord)
                    min_x = min(min_x, coord)
                    max_x = max(min_x, coord)

    while drop(spring, (min_x - 1, max_x + 1, max_y), clay, drops):
        pass

    # dump((min_x - 1, max_x + 1, max_y), clay, drops)
    print(f"Part 1: {len(drops)}")
