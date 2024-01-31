import sys

sys.path.append(".\\")

from utils.intcode import Intcode
from utils.pos import Pos

TURNS = [lambda p: Pos(-p.y, p.x), lambda p: Pos(p.y, -p.x)]


def paint(white):
    points = list(white)

    points.sort(key=lambda p: p.x)
    min_x, max_x = min(points).x, max(points).x

    points.sort(key=lambda p: p.y)
    min_y, max_y = min(points).y, max(points).y

    points.sort()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if Pos(x, y) in points:
                print("#", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    with open("_inputs/2019/day-11/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    pos = Pos(0, 0)
    dpos = Pos(-1, 0)

    white = set()
    painted = set()

    computer = Intcode(numbers)
    computer.start(inputs=[])

    halted = False

    while not halted:
        output = computer.resume(inputs=[1 if pos in white else 0])
        if output.list[0] == 0:
            white -= {pos}
        elif output.list[0] == 1:
            white |= {pos}
        painted.add(pos)

        dpos = TURNS[output.list[1]](dpos)
        pos += dpos

        halted = output.status

    print(f"Part 1: {len(painted)}")

    pos = Pos(0, 0)
    dpos = Pos(-1, 0)

    white = set()
    white.add(pos)

    computer.start(inputs=[])

    halted = False

    while not halted:
        output = computer.resume(inputs=[1 if pos in white else 0])
        if output.list[0] == 0:
            white -= {pos}
        elif output.list[0] == 1:
            white |= {pos}

        dpos = TURNS[output.list[1]](dpos)
        pos += dpos

        halted = output.status

    print("Part 2:")
    paint(white)
