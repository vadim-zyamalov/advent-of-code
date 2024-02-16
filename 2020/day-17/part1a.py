import sys

sys.path.append(".\\")

from utils.pos import Pos3D, Pos4D


def step(points):
    new_points = set()

    neigbours = {}

    for pos in points:
        for nbr in pos.near_all:
            neigbours[nbr] = neigbours.get(nbr, 0) + 1

    for pos, val in neigbours.items():
        if (pos in points and val == 2) or (val == 3):
            new_points.add(pos)

    return new_points


if __name__ == "__main__":
    with open("_inputs/2020/day-17/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip("\n").split("\n")

    points = set()

    for x, row in enumerate(lines):
        for y, el in enumerate(row):
            if el == "#":
                points.add(Pos3D(x, y, 0))

    for _ in range(6):
        points = step(points)

    print(f"Part 1: {len(points)}")

    points = set()

    for x, row in enumerate(lines):
        for y, el in enumerate(row):
            if el == "#":
                points.add(Pos4D(x, y, 0, 0))

    for _ in range(6):
        points = step(points)

    print(f"Part 2: {len(points)}")
