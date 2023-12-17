import heapq as hq


def isgood(pos: tuple[int, int], bounds: tuple[int, int]) -> bool:
    return (0 <= pos[0] < bounds[0]) and (0 <= pos[1] < bounds[1])


def dijkstra(
    heatmap: list[list[int]],
    beg: tuple[int, int],
    fin: tuple[int, int],
    steps: tuple[int, int],
) -> int:
    Nx, Ny = len(heatmap), len(heatmap[0])

    queue = [(0, *beg, 0, 0)]

    visited = set()

    while queue:
        heat, x, y, dx, dy = hq.heappop(queue)

        if (x, y) == fin:
            return heat

        if (x, y, dx, dy) in visited:
            continue

        visited.add((x, y, dx, dy))

        directions = {(0, 1), (0, -1), (1, 0), (-1, 0)} - {(dx, dy), (-dx, -dy)}

        for ndx, ndy in directions:
            nx, ny, nheat = x, y, heat
            for i in range(1, steps[1] + 1):
                nx += ndx
                ny += ndy
                if not isgood((nx, ny), (Nx, Ny)):
                    break
                nheat += heatmap[nx][ny]
                if i >= steps[0]:
                    hq.heappush(queue, (nheat, nx, ny, ndx, ndy))

    return -1


if __name__ == "__main__":
    with open("_inputs/2023/day-17/input.txt", "r", encoding="utf8") as f:
        heatmap = [[int(el) for el in row] for row in f.read().strip().split("\n")]

        Nx, Ny = len(heatmap), len(heatmap[0])

        res1 = dijkstra(heatmap, (0, 0), (Nx - 1, Ny - 1), (1, 3))
        print(f"Part 1: {res1}")

        res2 = dijkstra(heatmap, (0, 0), (Nx - 1, Ny - 1), (4, 10))
        print(f"Part 2: {res2}")
