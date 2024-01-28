import sys

sys.path.append(".\\")

from utils.pos import Pos
from collections import deque, defaultdict
import heapq as hq

DOORS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEYS = "abcdefghijklmnopqrstuvwxyz"


def parse(lines):
    tiles = defaultdict(lambda: "#")
    keys = frozenset()
    start = Pos(-1, -1)

    for x, row in enumerate(lines):
        for y, tile in enumerate(row):
            pos = Pos(x, y)
            tiles[pos] = tile
            if tile == "@":
                start = pos
            elif tile in KEYS:
                keys |= {tile}

    return tiles, keys, start


def path(tiles, keys, start):
    seen = set()
    queue = [(0, start, frozenset())]

    while queue:
        dd, pos, fkeys = hq.heappop(queue)
        if fkeys == keys:
            return dd
        if (pos, fkeys) in seen:
            continue
        seen.add((pos, fkeys))
        for nxt in pos.near4:
            tile = tiles[nxt]
            if tile == "#":
                continue
            if tile.isupper() and tile.lower() not in fkeys:
                continue
            if tile.islower() and tile not in fkeys:
                _fkeys = fkeys | {tiles[nxt]}
            else:
                _fkeys = fkeys
            hq.heappush(queue, (dd + 1, nxt, _fkeys))


def path4(tiles, doors, keys, starts):
    fin_keys = tuple(sorted(keys.values()))

    seen = set()
    queue = [(0, starts, ())]

    while queue:
        dd, poss, fkeys = hq.heappop(queue)
        if fkeys == fin_keys:
            return dd
        if (poss, fkeys) in seen:
            continue
        seen.add((poss, fkeys))
        for i, pos in enumerate(poss):
            for nxt in pos.near4:
                if nxt not in tiles:
                    continue
                if nxt in doors and doors[nxt].lower() not in fkeys:
                    continue
                if nxt in keys and keys[nxt] not in fkeys:
                    _fkeys = tuple(sorted(fkeys + (keys[nxt],)))
                else:
                    _fkeys = fkeys
                _pos = tuple(poss[j] if j != i else nxt for j in range(4))
                hq.heappush(queue, (dd + 1, _pos, _fkeys))


def split(tiles: set, start):
    starts = ()
    for nxt in start.near8:
        if nxt.dist(start) == 2:
            starts += (nxt,)
        else:
            tiles.remove(nxt)
    tiles.remove(start)
    return starts


if __name__ == "__main__":
    with open("_inputs/2019/day-18/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n")

    tiles, keys, start = parse(lines)

    print(f"Part 1: {path(tiles, keys, start)}")

    # starts = split(tiles, start)

    # print(f"Part 2: {path4(tiles, doors, keys, starts)}")
