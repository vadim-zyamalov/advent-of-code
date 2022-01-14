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
    for dx, dy in [(-1, 0),
                   (1, 0),
                   (0, -1),
                   (0, 1)]:
        variant_pos = (pos[0] + dx, pos[1] + dy)
        if grid[variant_pos[0]][variant_pos[1]] == "#":
            continue
        result.append(variant_pos)
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
    for next_pos in possible_moves(cur_pos, GRID):
        if GRID[next_pos[0]][next_pos[1]] in VENTS and \
           GRID[next_pos[0]][next_pos[1]] not in cur_visit:
            hp.heappush(
                queue,
                (cur_steps + 1,
                 (next_pos,
                  tsorted(
                      (GRID[next_pos[0]][next_pos[1]],) + cur_visit
                  ))))
        else:
            hp.heappush(
                queue,
                (cur_steps + 1, (next_pos, cur_visit))
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
    for next_pos in possible_moves(cur_pos, GRID):
        if GRID[next_pos[0]][next_pos[1]] in VENTS and \
           GRID[next_pos[0]][next_pos[1]] not in cur_visit:
            hp.heappush(
                queue,
                (cur_steps + 1,
                 (next_pos,
                  tsorted(
                      (GRID[next_pos[0]][next_pos[1]],) + cur_visit
                  ))))
        else:
            hp.heappush(
                queue,
                (cur_steps + 1, (next_pos, cur_visit))
            )
