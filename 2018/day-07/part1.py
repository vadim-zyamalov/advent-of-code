import heapq as hq


def get_start(graph):
    result = []
    for node, val in graph.items():
        if val["fr"] == []:
            result.append(node)
    return sorted(result)


def part1(graph):
    result = []
    queue = get_start(graph)

    while queue:
        node = queue.pop(0)
        result.append(node)
        for nxt in graph[node]["to"]:
            if all(prev in result for prev in graph[nxt]["fr"]):
                queue.append(nxt)
                queue.sort()

    return "".join(result)


def part2(graph, nwork=5, add=60):
    t = 0
    finished = []
    workers = []

    queue = get_start(graph)

    while queue or workers:
        if (len(workers) == nwork) or (not queue and workers):
            ft, wnode = hq.heappop(workers)
            t = max(ft, t)
            finished.append(wnode)
            queue.extend(graph[wnode]["to"])
            queue = sorted(set(queue))
        while workers and workers[0][0] <= t:
            _, wnode = hq.heappop(workers)
            finished.append(wnode)
            queue.extend(graph[wnode]["to"])
            queue = sorted(set(queue))
        for node in list(queue):
            if (
                (graph[node]["fr"] == [])
                or all(prev in finished for prev in graph[node]["fr"])
                or (finished == [])
            ):
                if len(workers) < nwork:
                    hq.heappush(workers, (t + add + ord(node) - ord("A") + 1, node))
                    queue.remove(node)
                else:
                    break
        else:
            if workers:
                t = workers[0][0]

    return t


if __name__ == "__main__":
    graph = {}

    with open("./_inputs/2018/day-07/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            words = line.split()
            fr, to = words[1], words[7]

            if fr not in graph:
                graph[fr] = {"fr": [], "to": []}
            if to not in graph:
                graph[to] = {"fr": [], "to": []}

            graph[fr]["to"].append(to)
            graph[to]["fr"].append(fr)

    for node in graph:
        graph[node]["fr"].sort()
        graph[node]["to"].sort()

    print(f"Part 1: {part1(graph)}")
    print(f"Part 2: {part2(graph)}")
