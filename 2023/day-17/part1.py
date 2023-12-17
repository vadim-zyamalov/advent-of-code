import heapq as hq


def isgood(pos: tuple[int, int], bounds: tuple[int, int]) -> bool:
    return (0 <= pos[0] < bounds[0]) and (0 <= pos[1] < bounds[1])


def next_pos(
    pos: tuple[int, int],
    direction: tuple[int, int],
    step: int,
    steps: tuple[int, int],
    bounds: tuple[int, int],
) -> list[tuple[int, ...]]:
    x, y = pos
    dx, dy = direction

    result = []
    if dx == dy:
        for ddx, ddy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if isgood((x + ddx, y + ddy), bounds):
                result.append((x + ddx, y + ddy, ddx, ddy, 0))
    else:
        if (step < steps[1]) and isgood((x + dx, y + dy), bounds):
            result.append((x + dx, y + dy, dx, dy, step + 1))
        if (steps[0] <= step < steps[1]) and isgood((x + dy, y + dx), bounds):
            result.append((x + dy, y + dx, dy, dx, 0))
        if (steps[0] <= step < steps[1]) and isgood((x - dy, y - dx), bounds):
            result.append((x - dy, y - dx, -dy, -dx, 0))

    return result


def dijkstra(
    heatmap: list[list[int]],
    beg: tuple[int, int],
    fin: tuple[int, int],
    steps: tuple[int, int],
) -> int:
    Nx, Ny = len(heatmap), len(heatmap[0])

    queue = [(0, *beg, 0, 0, 0)]

    visited = set()

    while queue:
        heat, x, y, dx, dy, step = hq.heappop(queue)

        if ((x, y) == fin) and (step >= steps[0]):
            return heat

        if (x, y, dx, dy, step) in visited:
            # if visited[(x, y, dx, dy, left)] < heat:
            continue

        visited.add((x, y, dx, dy, step))

        for nx, ny, ndx, ndy, nstep in next_pos(
            (x, y), (dx, dy), step, steps, (Nx, Ny)
        ):
            hq.heappush(queue, (heat + heatmap[nx][ny], nx, ny, ndx, ndy, nstep))

    return None


if __name__ == "__main__":
    with open("_inputs/2023/day-17/input.txt", "r", encoding="utf8") as f:
        heatmap = [[int(el) for el in row] for row in f.read().strip().split("\n")]

        Nx, Ny = len(heatmap), len(heatmap[0])

        res1 = dijkstra(heatmap, (0, 0), (Nx - 1, Ny - 1), (0, 3))
        print(f"Part 1: {res1}")

        res2 = dijkstra(heatmap, (0, 0), (Nx - 1, Ny - 1), (3, 10))
        print(f"Part 2: {res2}")
