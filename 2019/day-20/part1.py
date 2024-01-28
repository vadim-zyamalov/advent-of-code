import sys

sys.path.append(".\\")

from utils.pos import Pos
from collections import defaultdict, deque
import heapq as hq

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def nodes(tiles):
    result = set()

    for tile in tiles:
        if sum(nxt in tiles for nxt in tile.near4) > 2:
            result.add(tile)

    return result


def portals(tiles, lines):
    _tiles = sorted(tiles, key=lambda t: t.x)
    min_x, max_x = _tiles[0].x, _tiles[-1].x
    _tiles = sorted(tiles, key=lambda t: t.y)
    min_y, max_y = _tiles[0].y, _tiles[-1].y

    tmp = defaultdict(list)

    for tile in tiles:
        x, y = tile.x, tile.y
        for nbr in tile.near4:
            nx, ny = nbr.x, nbr.y
            dx, dy = nx - x, ny - y
            if lines[nx][ny] in LETTERS:
                if (dx > 0) or (dy > 0):
                    tag = lines[nx][ny] + lines[nx + dx][ny + dy]
                else:
                    tag = lines[nx + dx][ny + dy] + lines[nx][ny]
                tmp[tag].append(tile)
                break

    outer = {}
    inner = {}
    [start], [finish] = tmp["AA"], tmp["ZZ"]

    for pp in tmp:
        if pp in ["AA", "ZZ"]:
            continue
        p0, p1 = tmp[pp]
        if p0.x in [min_x, max_x] or p0.y in [min_y, max_y]:
            outer[p0] = p1
            inner[p1] = p0
        else:
            inner[p0] = p1
            outer[p1] = p0

    return outer, inner, start, finish


def graph(tiles, nodes, portals_outer, portals_inner, beg: Pos, fin: Pos):
    if fin not in nodes:
        nodes.add(fin)

    seen = set()
    result = {beg: {}}

    queue = deque([(beg, beg)])

    while queue:
        x, prev_x = queue.popleft()
        start = prev_x
        dist = 0
        ch_lev = 0
        min_ch, max_ch = 1_000_000, 0
        next_step = False

        while x not in nodes:
            seen.add(x)
            if x in portals_outer and prev_x not in portals_inner:
                next_tile = [portals_outer[x]]
                ch_lev -= 1
                min_ch = min(min_ch, ch_lev)
                max_ch = max(max_ch, ch_lev)
            elif x in portals_inner and prev_x not in portals_outer:
                next_tile = [portals_inner[x]]
                ch_lev += 1
                min_ch = min(min_ch, ch_lev)
                max_ch = max(max_ch, ch_lev)
            else:
                next_tile = [
                    nxt for nxt in x.near4 if nxt in tiles and nxt != prev_x
                ]
            if not next_tile:
                next_step = True
                break
            x, prev_x, dist = next_tile[0], x, dist + 1
        seen.add(x)

        if next_step:
            continue

        finish = x

        if start not in result:
            result[start] = {}
        if finish not in result[start]:
            result[start][finish] = []

        if finish not in result:
            result[finish] = {}
        if start not in result[finish]:
            result[finish][start] = []

        result[start][finish].append(
            (dist + (1 if start != beg else 0), ch_lev, min_ch)
        )
        result[finish][start].append(
            (dist + (1 if start != beg else 0), -ch_lev, -max_ch)
        )

        next_tile = [nxt for nxt in x.near4 if nxt in tiles and nxt not in seen]

        for nx in next_tile:
            queue.append((nx, x))

    return result


def part1(graph, beg, fin):
    seen = set()
    queue = [(0, beg)]

    while queue:
        dd, pos = hq.heappop(queue)

        if pos == fin:
            return dd

        if pos in seen:
            continue
        seen.add(pos)

        for nxt, variants in graph[pos].items():
            for l, _, _ in variants:
                hq.heappush(queue, (dd + l, nxt))


def part2(graph, beg, fin):
    seen = set()
    queue = [(0, beg, 0)]

    while queue:
        dd, pos, level = hq.heappop(queue)

        if (pos, level) == (fin, 0):
            return dd

        if (pos == beg) and (level > 0):
            continue

        if (pos == fin) and (level > 0):
            continue

        if level < 0:
            continue

        if (pos, level) in seen:
            continue
        seen.add((pos, level))

        for nxt, variants in graph[pos].items():
            for lng, ch_lev, min_ch in variants:
                if level + min_ch < 0:
                    continue
                hq.heappush(queue, (dd + lng, nxt, level + ch_lev))


if __name__ == "__main__":
    with open("_inputs/2019/day-20/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip("\n").split("\n")
        tiles = set(
            Pos(x, y)
            for x, row in enumerate(lines)
            for y, el in enumerate(row)
            if el == "."
        )

    nodes_set = nodes(tiles)
    portals_outer, portals_inner, start, finish = portals(tiles, lines)
    G = graph(tiles, nodes_set, portals_outer, portals_inner, start, finish)
    print(f"Part 1: {part1(G, start, finish)}")
    print(f"Part 2: {part2(G, start, finish)}")
