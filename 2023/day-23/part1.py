import heapq
from collections import defaultdict

DIRS = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def inside(x, y, Nx, Ny):
    return (0 <= x < Nx) and (0 <= y < Ny)


def next_pos(x, y, forest, fsize):
    Nx, Ny = fsize
    result = []
    for dx, dy in DIRS:
        if inside(x + dx, y + dy, Nx, Ny):
            if forest[x + dx][y + dy] != "#":
                result.append((x + dx, y + dy))
    return result


def nodes(forest):
    Nx, Ny = len(forest), len(forest[0])

    result = set()

    for x in range(1, Nx - 1):
        for y in range(1, Ny - 1):
            if forest[x][y] != "#":
                n_ways = sum(forest[x + dx][y + dy] != "#" for dx, dy in DIRS)
                if n_ways > 2:
                    result.add((x, y))
    return sorted(result)


def non_slippery(graph):
    result = {}
    for k in graph:
        for vk in graph[k]:
            if k not in result:
                result[k] = {}
            if vk not in result:
                result[vk] = {}
            result[k][vk] = graph[k][vk]
            result[vk][k] = graph[k][vk]
    return result


def graph(forest, nodes, beg, fin):
    Nx, Ny = len(forest), len(forest[0])

    if fin not in nodes:
        nodes.append(fin)

    seen = set()
    result = {beg: {}}

    queue = [(*beg, *beg, True)]

    while queue:
        x, y, prx, pry, direction = queue.pop()

        start = (prx, pry)
        dist = 0 if start != beg else -1

        while (x, y) not in nodes:
            seen.add((x, y))

            next_tile = [
                (nx, ny)
                for nx, ny in next_pos(x, y, forest, (Nx, Ny))
                if (nx, ny) != (prx, pry)
            ]
            prx, pry = x, y
            x, y = next_tile[0]

            dist += 1

        finish = (x, y)

        if start == beg:
            result[beg][finish] = dist + 1
        else:
            if direction:
                if start not in result:
                    result[start] = {}
                result[start][finish] = dist + 1
            else:
                if finish not in result:
                    result[finish] = {}
                result[finish][start] = dist + 1

        next_tile = [
            (nx, ny)
            for nx, ny in next_pos(x, y, forest, (Nx, Ny))
            if (nx, ny) not in seen
        ]

        for nx, ny in next_tile:
            match forest[nx][ny]:
                case "v":
                    nd = nx - x == 1
                case "^":
                    nd = nx - x == -1
                case ">":
                    nd = ny - y == 1
                case "<":
                    nd = ny - y == -1
            if (nx, ny, x, y, nd) not in queue and (x, y) in nodes:
                queue.append((nx, ny, x, y, nd))

    return result


def heuristic(p0, p1):
    return abs(p0[0] - p1[0]) + abs(p0[1] - p1[1])


def part1(graph, beg, fin):
    queue = [(0, beg, ())]
    result = 0

    while queue:
        dist, cur, path = heapq.heappop(queue)
        if cur == fin:
            result = max(result, abs(dist))
            continue

        if cur in path:
            continue

        for nxt in graph[cur]:
            heapq.heappush(
                queue,
                (dist - graph[cur][nxt], nxt, path + (cur,)),
            )

    return result


if __name__ == "__main__":
    with open("_inputs/2023/day-23/input.txt", "r", encoding="utf8") as f:
        forest = f.read().strip().split("\n")

        start = (0, forest[0].index("."))
        finish = (len(forest) - 1, forest[-1].index("."))

        nodes_f = nodes(forest)
        graph_f1 = graph(forest, nodes(forest), start, finish)
        graph_f2 = non_slippery(graph_f1)
        res1 = part1(graph_f1, start, finish)
        print(f"Part 1: {res1}")
        res2 = part1(graph_f2, start, finish)
        print(f"Part 2: {res2}")
