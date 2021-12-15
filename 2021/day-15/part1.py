grid = []

moves = [(-1, 0),
         (0, -1)]


def dump(grid):
    for row in grid:
        for digit in row:
            print(digit, end=" ")
        print()
    print()


def neighbours(i, j, grid):
    dimi, dimj = len(grid), len(grid[0])
    return [(i + di, j + dj)
            for (di, dj) in [(-1, 0),
                             (0, -1),
                             (1, 0),
                             (0, 1)]
            if (0 <= i + di < dimi) and (0 <= j + dj < dimj)]


def deep_copy(grid):
    return [[el for el in raw] for raw in grid]


def increment(grid):
    return [[1 if el == 9 else el + 1 for el in row] for row in grid]


def append_right(grid, new_grid):
    return [[el for el in grid[row] + new_grid[row]] for row in range(len(grid))]


def append_below(grid, new_grid):
    return [[el for el in row] for row in grid + new_grid]

def process(grid):
    dimi, dimj = len(grid), len(grid[0])
    inner_grid = deep_copy(grid)
    for step in range(dimi):
        for s in range(step, dimi):
            tmpr = []
            tmpc = []
            for di, dj in moves:
                if (0 <= step + di < dimi) and \
                   (0 <= s + dj < dimj):
                    tmpr.append(inner_grid[step + di][s + dj])
                if (0 <= s + di < dimi) and \
                   (0 <= step + dj < dimj):
                    tmpc.append(inner_grid[s + di][step + dj])
            if tmpr:
                inner_grid[step][s] += min(tmpr)
            if tmpc and (step != s):
                inner_grid[s][step] += min(tmpc)
    return inner_grid


def process_dijkstra(grid):
    dimi, dimj = len(grid), len(grid[0])
    cost = {}
    points = []
    for i in range(dimi):
        for j in range(dimj):
            cost[i, j] = 10 * dimi * dimj
            points.append((i, j))
    cost[0, 0] = 0
    
    while len(points) > 0:
        min_cost = min([cost[k] for k in cost if k in points])
        pi, pj = [p for p in points if cost[p] == min_cost][0]
    
        points.remove((pi, pj))

        for (ni, nj) in neighbours(pi, pj, grid):
            if (ni, nj) in points and (cost[ni, nj] > cost[pi, pj] + grid[ni][nj]):
                cost[ni, nj] = cost[pi, pj] + grid[ni][nj]
    return cost[dimi - 1, dimj - 1]


def process_dijkstra_add(grid):
    dimi, dimj = len(grid), len(grid[0])
    cost = {(int(0), int(0)): 0}
    points = [(0, 0)]
    
    for (pi, pj) in points:
        for (ni, nj) in neighbours(pi, pj, grid):
            if (ni, nj) in cost and (cost[ni, nj] <= cost[pi, pj] + grid[ni][nj]):
                continue
            cost[ni, nj] = cost[pi, pj] + grid[ni][nj]
            points.append((ni, nj))
    return cost[dimi - 1, dimj - 1]


with open("input.txt", "r") as f:
    for line in f:
        if line.strip() == "":
            continue
        grid.append([int(digit) for digit in line.strip()])

result = process_dijkstra_add(grid)
print("Part 1: {}".format(result))

new_grid = deep_copy(grid)
inc_grid = deep_copy(grid)
for i in range(4):
    inc_grid = increment(inc_grid)
    new_grid = append_right(new_grid, inc_grid)

inc_grid = deep_copy(new_grid)
for i in range(4):
    inc_grid = increment(inc_grid)
    new_grid = append_below(new_grid, inc_grid)

result = process_dijkstra_add(new_grid)
print("Part 2: {}".format(result))
