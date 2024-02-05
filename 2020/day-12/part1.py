import sys

sys.path.append(".\\")

from utils.pos import Pos

ROT = {0: "E", 1: "N", 2: "W", 3: "S"}
WPROT = {"L": lambda pos: Pos(pos.y, -pos.x), "R": lambda pos: Pos(-pos.y, pos.x)}

DIR = {"E": Pos(0, 1), "N": Pos(1, 0), "W": Pos(0, -1), "S": Pos(-1, 0)}


def move(pos: Pos, face: int, op: str, num: int) -> tuple[Pos, int]:
    match op:
        case "N" | "E" | "S" | "W":
            return pos + num * DIR[op], face
        case "L" | "R":
            d_ang = num // 90
            return pos, (face + d_ang * (1 if op == "L" else -1)) % 4
        case "F":
            return pos + num * DIR[ROT[face]], face
        case _:
            assert False, "whong operation"


def movewp(pos: Pos, wp: Pos, op: str, num: int) -> tuple[Pos, Pos]:
    match op:
        case "N" | "E" | "S" | "W":
            return (
                pos,
                wp + num * DIR[op],
            )
        case "L" | "R":
            d_ang = num // 90
            for _ in range(d_ang):
                wp = WPROT[op](wp)
            return pos, wp
        case "F":
            return pos + num * wp, wp
        case _:
            assert False, "whong operation"


if __name__ == "__main__":
    with open("_inputs/2020/day-12/input.txt", "r", encoding="utf8") as f:
        commands = [(line[0], int(line[1:])) for line in f.read().strip().split("\n")]

    beg = Pos(0, 0)
    cur = beg
    face = 0

    for op, num in commands:
        cur, face = move(cur, face, op, num)

    print(f"Part 1: {cur.dist(beg)}")

    cur = beg
    wp = Pos(1, 10)

    for op, num in commands:
        cur, wp = movewp(cur, wp, op, num)

    print(f"Part 2: {cur.dist(beg)}")
