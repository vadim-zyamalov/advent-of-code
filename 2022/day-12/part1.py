import time
import heapq as heap


def get_start_finish(grid):
    start, finish = None, None
    stop = False
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if not start and (grid[r][c] == "S"):
                start = (r, c)
                grid[r][c] = "a"
            if not finish and (grid[r][c] == "E"):
                finish = (r, c)
                grid[r][c] = "z"
            if start and finish:
                stop = True
                break
        if stop:
            break
    return start, finish


def possible_moves(r, c, grid):
    dimr, dimc = len(grid), len(grid[0])
    res = []
    if (r > 0) and (ord(grid[r][c]) >= ord(grid[r - 1][c]) - 1):
        res.append((-1, 0))
    if (r < dimr - 1) and (ord(grid[r][c]) >= ord(grid[r + 1][c]) - 1):
        res.append((1, 0))
    if (c > 0) and (ord(grid[r][c]) >= ord(grid[r][c - 1]) - 1):
        res.append((0, -1))
    if (c < dimc - 1) and (ord(grid[r][c]) >= ord(grid[r][c + 1]) - 1):
        res.append((0, 1))
    return res


def possible_moves_rev(r, c, grid):
    dimr, dimc = len(grid), len(grid[0])
    res = []
    if (r > 0) and (ord(grid[r][c]) <= ord(grid[r - 1][c]) + 1):
        res.append((-1, 0))
    if (r < dimr - 1) and (ord(grid[r][c]) <= ord(grid[r + 1][c]) + 1):
        res.append((1, 0))
    if (c > 0) and (ord(grid[r][c]) <= ord(grid[r][c - 1]) + 1):
        res.append((0, -1))
    if (c < dimc - 1) and (ord(grid[r][c]) <= ord(grid[r][c + 1]) + 1):
        res.append((0, 1))
    return res


def dijkstra(start, finish, grid):
    queue: list[tuple[tuple, int]] = [(0, start)]
    visited = {}

    while len(queue) > 0:
        q_path, q_state = heap.heappop(queue)
        if q_state == finish:
            return q_path
        if (q_state in visited) and (visited[q_state] <= q_path):
            continue
        visited[q_state] = q_path
        for dr, dc in possible_moves(q_state[0], q_state[1], grid):
            heap.heappush(queue, (q_path + 1, (q_state[0] + dr, q_state[1] + dc)))
    return float("inf")


def dijkstra_rev(finish, grid):
    dist = [[float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]
    queue = {}
    for r in range(len(MAP)):
        for c in range(len(MAP[0])):
            queue[r, c] = float("inf")
    queue[finish] = 0

    while len(queue) > 0:
        min_value = min(queue.values())
        min_k = [k for k in queue if queue[k] == min_value][0]
        q_state, q_path = min_k, queue[min_k]
        del queue[min_k]
        for dr, dc in possible_moves_rev(q_state[0], q_state[1], grid):
            if (q_state[0] + dr, q_state[1] + dc) in queue:
                tmp = q_path + 1
                if queue[q_state[0] + dr, q_state[1] + dc] > tmp:
                    queue[q_state[0] + dr, q_state[1] + dc] = tmp
                    dist[q_state[0] + dr][q_state[1] + dc] = tmp

    min_path = float("inf")
    for r in range(len(MAP)):
        for c in range(len(MAP[0])):
            if MAP[r][c] == "a":
                min_path = min(min_path, dist[r][c])
    return dist, min_path


MAP = []

with open("../../_inputs/2022/day-12/input.txt", "r", encoding="utf8") as f:
    for line in f:
        MAP.append(list(line.strip()))

s, f = get_start_finish(MAP)
t0 = time.time()
path = dijkstra(s, f, MAP)
t1 = time.time()
print(f"Part 1: {path}")
print(f"  Elapsed in {t1 - t0:3.2f} sec.")

path = float("inf")
t0 = time.time()
for r in range(len(MAP)):
    for c in range(len(MAP[0])):
        if MAP[r][c] == "a":
            path = min(path, dijkstra((r, c), f, MAP))
t1 = time.time()
print(f"Part 2: {path}")
print(f"  Elapsed in {t1 - t0:3.2f} sec.")

t0 = time.time()
dist, path = dijkstra_rev(f, MAP)
t1 = time.time()
print(f"Part 1: {dist[s[0]][s[1]]}")
print(f"Part 2: {path}")
print(f"  Elapsed in {t1 - t0:3.2f} sec.")
