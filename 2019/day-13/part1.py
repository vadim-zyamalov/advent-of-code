import sys

sys.path.append(".\\")

from utils.intcode import Intcode
from collections import defaultdict

TILES = {1: "#", 2: "@", 3: "_", 4: "O", 0: " "}


def parse(data, tiles):
    oi = iter(data)
    scores = []
    ball = None
    bat = None

    for x, y, t in zip(oi, oi, oi):
        if (x, y) == (-1, 0):
            scores.append(t)
        else:
            if t == 4:
                ball = (x, y)
            elif t == 3:
                bat = (x, y)
            tiles[x, y] = t
    return scores, ball, bat


def bricks(tiles):
    return sum(v == 2 for v in tiles.values())


def dump(tiles):
    coords = sorted(tiles.keys())
    min_x, min_y, max_x, max_y = *coords[0], *coords[-1]

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print(TILES[tiles[x, y]], end="")
        print()


if __name__ == "__main__":
    with open("_inputs/2019/day-13/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    tiles = defaultdict(int)
    computer = Intcode(numbers)
    output, _ = computer.process(inputs=[])
    _ = parse(output, tiles)
    print(f"Part 1: {sum(v == 2 for v in tiles.values())}")

    tiles = defaultdict(int)
    computer.reset()
    computer._regs[0] = 2
    output, _ = computer.process(inputs=[])

    scores, ball, bat = parse(output, tiles)
    assert ball is not None
    assert bat is not None

    dump(tiles)

    while bricks(tiles) > 0:
        i = -1 if ball[1] < bat[1] else 1 if ball[1] > bat[1] else 0
        output, finished = computer.process(inputs=[i], resume=True)

        _scores, _ball, _bat = parse(output, tiles)

        if _ball is not None:
            ball = _ball
        if _bat is not None:
            bat = _bat
        if scores != []:
            scores.extend(_scores)

    dump(tiles)
    print(f"Part 2: {scores[-1]}")
