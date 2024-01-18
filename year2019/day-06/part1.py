from collections import defaultdict


def parse(lines):
    graph = defaultdict(set)

    for line in lines:
        cb, ob = line.split(")")
        graph[cb].add(ob)

    return graph


def count(graph, head="COM", n=0):
    if not graph[head]:
        return n
    return n + sum(count(graph, el, n + 1) for el in graph[head])


def dfs(graph, node, fin, path, visited):
    visited.add(node)
    path.append(node)

    if node == fin:
        return True

    if not graph[node] or not any(
        dfs(graph, nxt, fin, path, visited) for nxt in graph[node] if nxt not in visited
    ):
        path.pop()
        return False

    return True


def intersect(path0, path1):
    i = 0

    while (i < len(path0)) and (i < len(path1)) and (path0[i] == path1[i]):
        i += 1

    if path0[i - 1] != path1[i - 1]:
        return None
    return i - 1


def jumps(graph, beg="YOU", fin="SAN"):
    path0, path1 = [], []

    visited = set()
    dfs(graph, "COM", beg, path0, visited)

    visited = set()
    dfs(graph, "COM", fin, path1, visited)

    i = intersect(path0, path1)

    if i:
        return len(path0) + len(path1) - 2 * i - 4
    return None


if __name__ == "__main__":
    with open("./_inputs/2019/day-06/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n")

    graph = parse(lines)
    print(f"Part 1: {count(graph)}")
    print(f"Part 2: {jumps(graph, 'YOU', 'SAN')}")
