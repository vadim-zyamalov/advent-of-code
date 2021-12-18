grid = []
steps = 100


def status(i, j, grid):
    dimi, dimj = len(grid), len(grid[0])
    number = 0
    if (i > 0) and (grid[i-1][j] == 1):
        number += 1
    if (i > 0) and (j > 0) and (grid[i-1][j-1] == 1):
        number += 1
    if (j > 0) and (grid[i][j-1] == 1):
        number += 1
    if (i < dimi - 1) and (j > 0) and (grid[i+1][j-1] == 1):
        number += 1
    if (i < dimi - 1) and (grid[i+1][j] == 1):
        number += 1
    if (i < dimi - 1) and (j < dimj - 1) and (grid[i+1][j+1] == 1):
        number += 1
    if (j < dimj - 1) and (grid[i][j+1] == 1):
        number += 1
    if (i > 0) and (j < dimj - 1) and (grid[i-1][j+1] == 1):
        number += 1
    if (number == 3) and (grid[i][j] == 0):
        return 1
    if (number not in [2, 3]) and (grid[i][j] == 1):
        return -1
    return 0


def stuck(grid):
    dimi, dimj = len(grid), len(grid[0])
    grid[0][0] = 1
    grid[0][dimj-1] = 1
    grid[dimi-1][0] = 1
    grid[dimi-1][dimj-1] = 1


def dump(grid):
    for i in grid:
        for j in i:
            print('.' if j == 0 else '#', end='')
        print()


with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() != '':
            grid.append([0 if c == '.' else 1 for c in line.strip()])

for step in range(steps):
    new_grid = [[
        grid[i][j] + status(i, j, grid) for j in range(len(grid[i]))
    ] for i in range(len(grid))]
    grid = new_grid.copy()

print(f"Part 1: {sum(v for row in grid for v in row)}")

grid = []

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() != '':
            grid.append([0 if c == '.' else 1 for c in line.strip()])
    stuck(grid)

for step in range(steps):
    new_grid = [[
        grid[i][j] + status(i, j, grid) for j in range(len(grid[i]))
    ] for i in range(len(grid))]
    stuck(new_grid)
    grid = new_grid.copy()

print(f"Part 2: {sum(v for row in grid for v in row)}")
