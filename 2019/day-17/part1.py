import sys

sys.path.append(".\\")

from utils.intcode import Intcode
from utils.pos import Pos


def parse(data):
    lines = data.strip().split("\n")

    bot = Pos(-1, -1), ""
    tiles = set()

    for x, row in enumerate(lines):
        for y, el in enumerate(row):
            if el in "#^v<>":
                tiles.add(Pos(x, y))
                if el in "^v<>":
                    bot = Pos(x, y), el

    return bot, tiles


def alignment(tiles):
    result = 0

    for tile in tiles:
        if all(nbr in tiles for nbr in tile.near4):
            result += tile.x * tile.y

    return result


if __name__ == "__main__":
    with open("_inputs/2019/day-17/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    computer = Intcode(numbers, ascii=True)
    output = computer.start(inputs=[])
    bot, tiles = parse(output.ascii)

    print(f"Part 1: {alignment(tiles)}")

    computer.initials[0] = 2
    computer.start(inputs=[])

    inputs = [
        "C,A,C,B,A,C,A,B,B,A\n",
        "R,10,R,6,R,4,R,4\n",
        "R,6,L,12,L,12\n",
        "L,12,L,12,R,4\n",
        "n\n",
    ]

    for inp in inputs:
        output = computer.process(inputs=inp)

    print(f"Part 2: {output.rest[0]}")
