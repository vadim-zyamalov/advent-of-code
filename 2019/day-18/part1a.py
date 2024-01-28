import sys

sys.path.append(".\\")

from utils.pos import Pos
from collections import deque, defaultdict
from typing import Deque
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


def reachable_keys(pos: Pos, keys: frozenset, tiles: defaultdict):
    queue: Deque[tuple[Pos, int]] = deque([(pos, 0)])
    seen = set()

    while queue:
        pp, dd = queue.popleft()
        tile = tiles[pp]
        if tile.islower() and tile not in keys:
            yield pp, dd, tiles[pp]
            continue
        for nxt in pp.near4:
            if nxt in seen:
                continue
            seen.add(nxt)
            tile = tiles[nxt]
            if tile != "#" and (not tile.isupper() or tile.lower() in keys):
                queue.append((nxt, dd + 1))


def path(tiles, keys, start):
    seen = set()
    queue: list[tuple[int, Pos, frozenset]] = [(0, start, frozenset())]

    while queue:
        dd, pos, fkeys = hq.heappop(queue)
        if fkeys == keys:
            return dd
        if (pos, fkeys) in seen:
            continue
        seen.add((pos, fkeys))
        for nxt, ll, key in reachable_keys(pos, fkeys, tiles):
            hq.heappush(queue, (dd + ll, nxt, fkeys | {key}))


def path4(tiles, keys, starts):
    seen = set()
    queue: list[tuple[int, tuple[Pos], frozenset]] = [(0, starts, frozenset())]

    while queue:
        dd, poss, fkeys = hq.heappop(queue)
        if fkeys == keys:
            return dd
        if (poss, fkeys) in seen:
            continue
        seen.add((poss, fkeys))
        for i, pos in enumerate(poss):
            for nxt, ll, key in reachable_keys(pos, fkeys, tiles):
                _pos = poss[0:i] + (nxt,) + poss[i + 1 :]
                hq.heappush(queue, (dd + ll, _pos, fkeys | {key}))


def split(tiles: defaultdict, start):
    starts = ()
    for nxt in start.near8:
        if nxt.dist(start) == 2:
            starts += (nxt,)
        else:
            tiles[nxt] = "#"
    tiles[start] = "#"
    return starts


if __name__ == "__main__":
    with open("_inputs/2019/day-18/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n")

    tiles, keys, start = parse(lines)

    print(f"Part 1: {path(tiles, keys, start)}")

    starts = split(tiles, start)

    print(f"Part 2: {path4(tiles, keys, starts)}")
