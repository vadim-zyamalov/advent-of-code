import sys

sys.path.append(".\\")

from utils.pos import Pos

DIRS = tuple(
    Pos(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if not ((dx == 0) and (dy == 0))
)


def neighbours(chairs, Nx, Ny):
    for pos in chairs:
        chairs[pos]["nbr"] = [nbr for nbr in pos.near8 if nbr in chairs]
        for d in DIRS:
            npos = pos
            while (0 <= npos.x < Nx) and (0 <= npos.y < Ny):
                npos += d
                if npos in chairs:
                    chairs[pos]["nbr2"].append(npos)
                    break


def step(chairs: dict[Pos, dict]):
    nbr_occupied = {
        k: sum(chairs[nbr]["occ"] for nbr in chairs[k]["nbr"]) for k in chairs
    }

    changed = False

    for pos in chairs:
        if chairs[pos]["occ"] == 0 and nbr_occupied[pos] == 0:
            chairs[pos]["occ"] = 1
            changed = True
        elif chairs[pos]["occ"] > 0 and nbr_occupied[pos] >= 4:
            chairs[pos]["occ"] = 0
            changed = True

    return changed


def step2(chairs: dict[Pos, dict]):
    nbr_occupied = {
        k: sum(chairs[nbr]["occ"] for nbr in chairs[k]["nbr2"]) for k in chairs
    }

    changed = False

    for pos in chairs:
        if chairs[pos]["occ"] == 0 and nbr_occupied[pos] == 0:
            chairs[pos]["occ"] = 1
            changed = True
        elif chairs[pos]["occ"] > 0 and nbr_occupied[pos] >= 5:
            chairs[pos]["occ"] = 0
            changed = True

    return changed


if __name__ == "__main__":
    with open("_inputs/2020/day-11/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n")

    chairs = {}
    Nx, Ny = len(lines), len(lines[0])

    for r, row in enumerate(lines):
        for c, el in enumerate(row):
            if el in "L#":
                chairs[Pos(r, c)] = {
                    "occ": 0 if el == "L" else 1,
                    "nbr": [],
                    "nbr2": [],
                }
    neighbours(chairs, Nx, Ny)

    while step(chairs):
        pass

    print(f"Part 1: {sum(v["occ"] for v in chairs.values())}")

    for k in chairs:
        chairs[k]["occ"] = 0

    while step2(chairs):
        pass

    print(f"Part 2: {sum(v["occ"] for v in chairs.values())}")
