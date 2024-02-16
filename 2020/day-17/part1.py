import sys

sys.path.append(".\\")

from utils.pos import Pos3D, Pos4D


def active(points):
    return [k for k, v in points.items() if v]


def step(points):
    nxt_points = {}
    seen = set()

    for p in points:
        for np in p.near_all:
            if np in seen:
                continue
            seen.add(np)
            if np not in points or not points[np]:
                nxt_points[np] = (
                    sum(points[nnp] for nnp in np.near_all if nnp in points) == 3
                )
            elif points[np]:
                nxt_points[np] = sum(
                    points[nnp] for nnp in np.near_all if nnp in points
                ) in [2, 3]

    return nxt_points


if __name__ == "__main__":
    with open("_inputs/2020/day-17/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip("\n").split("\n")

    points = {}

    for x, row in enumerate(lines):
        for y, el in enumerate(row):
            points[Pos3D(x, y, 0)] = el == "#"

    for _ in range(6):
        points = step(points)

    print(f"Part 1: {len(active(points))}")

    points = {}

    for x, row in enumerate(lines):
        for y, el in enumerate(row):
            points[Pos4D(x, y, 0, 0)] = el == "#"

    for _ in range(6):
        points = step(points)

    print(f"Part 2: {len(active(points))}")
