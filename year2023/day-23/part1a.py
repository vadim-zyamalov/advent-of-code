import heapq

DIRS = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def nodes(forest):
    result = set()

    for tile in forest:
        if sum(tile + dt in forest for dt in [1, -1, 1j, -1j]) > 2:
            result.add(tile)
    return result


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
    if fin not in nodes:
        nodes.add(fin)

    seen = set()
    result = {beg: {}}

    queue = [(beg, beg, True)]

    while queue:
        x, prx, direction = queue.pop()
        start = prx

        dist = 0 if start != beg else -1

        while x not in nodes:
            seen.add(x)
            next_tile = [
                x + dx
                for dx in [1, -1, 1j, -1j]
                if x + dx in forest and x + dx != prx
            ]
            x, prx, dist = next_tile[0], x, dist + 1

        finish = x

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
            x + dx
            for dx in [1, -1, 1j, -1]
            if x + dx in forest and x + dx not in seen
        ]

        for nx in next_tile:
            match forest[nx]:
                case "v":
                    nd = nx - x == 1
                case "^":
                    nd = nx - x == -1
                case ">":
                    nd = nx - x == 1j
                case "<":
                    nd = nx - x == -1j
            queue.append((nx, x, nd))

    return result


def part1(graph, beg, fin):
    queue = [(0, beg, ())]
    result = 0
    visited = {}

    while queue:
        dist, cur, path = queue.pop()

        if cur in path:
            continue

        visited[cur] = max(visited.get(cur, 0), dist)

        for nxt in graph.get(cur, []):
            queue.append(
                (dist + graph[cur][nxt], nxt, path + (cur,)),
            )

    return visited[fin]


if __name__ == "__main__":
    with open("_inputs/2023/day-23/input.txt", "r", encoding="utf8") as f:
        forest = f.read().strip().split("\n")
        forest = {
            x + y * 1j: el
            for x, row in enumerate(forest)
            for y, el in enumerate(row.strip())
            if el != "#"
        }

        start, finish = [*forest][0], [*forest][-1]

        nodes_f = nodes(forest)
        graph_f1 = graph(forest, nodes(forest), start, finish)
        graph_f2 = non_slippery(graph_f1)
        res1 = part1(graph_f1, start, finish)
        print(f"Part 1: {res1}")
        res2 = part1(graph_f2, start, finish)
        print(f"Part 2: {res2}")
