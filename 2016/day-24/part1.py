import time
import heapq as hp


def init(grid):
    start = (-1, -1)
    points = []
    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            if el == "0":
                start = (i, j)
            elif (el != "#") and \
                 (el != ".") and \
                 (el != "0"):
                points.append(el)
    points.sort()
    return start, points


def tsorted(data):
    return tuple(sorted(data))


def possible_moves(pos, grid):
    result = []
    x, y = pos
    for dx, dy in [(-1, 0),
                   (1, 0),
                   (0, -1),
                   (0, 1)]:
        if grid[x + dx][y + dy] == "#":
            continue
        result.append((x + dx, y + dy))
    return result


GRID = []
with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        GRID.append(list(line.strip()))

START, VENTS = init(GRID)

queue = [(0, (START, ()))]
visited = {}

t_0 = time.time()
while queue:
    cur_steps, (cur_pos, cur_visit) = hp.heappop(queue)
    if len(cur_visit) == len(VENTS):
        print(f"Part 1: {cur_steps}")
        print(f"  elapsed in {time.time() - t_0:.2f} seconds")
        break
    if (cur_pos, cur_visit) in visited and \
       visited[(cur_pos, cur_visit)] <= cur_steps:
        continue
    visited[(cur_pos, cur_visit)] = cur_steps
    for next_x, next_y in possible_moves(cur_pos, GRID):
        if GRID[next_x][next_y] in VENTS and \
           GRID[next_x][next_y] not in cur_visit:
            hp.heappush(
                queue,
                (cur_steps + 1,
                 ((next_x, next_y),
                  tsorted(
                      (GRID[next_x][next_y],) + cur_visit
                  ))))
        else:
            hp.heappush(
                queue,
                (cur_steps + 1, ((next_x, next_y), cur_visit))
            )

queue = [(0, (START, ()))]
visited = {}

t_0 = time.time()
while queue:
    cur_steps, (cur_pos, cur_visit) = hp.heappop(queue)
    if (len(cur_visit) == len(VENTS)) and \
       cur_pos == START:
        print(f"Part 2: {cur_steps}")
        print(f"  elapsed in {time.time() - t_0:.2f} seconds")
        break
    if (cur_pos, cur_visit) in visited and \
       visited[(cur_pos, cur_visit)] <= cur_steps:
        continue
    visited[(cur_pos, cur_visit)] = cur_steps
    for next_x, next_y in possible_moves(cur_pos, GRID):
        if GRID[next_x][next_y] in VENTS and \
           GRID[next_x][next_y] not in cur_visit:
            hp.heappush(
                queue,
                (cur_steps + 1,
                 ((next_x, next_y),
                  tsorted(
                      (GRID[next_x][next_y],) + cur_visit
                  ))))
        else:
            hp.heappush(
                queue,
                (cur_steps + 1, ((next_x, next_y), cur_visit))
            )
