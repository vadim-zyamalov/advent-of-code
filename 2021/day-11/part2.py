grid = []
STEPS = 100


def deepcopy(original):
    return [list(row) for row in original]


def dump(grid):
    for i in grid:
        for j in i:
            print(f"{j} ", end='')
        print()
    print()


def step(grid):
    return [[
        grid[i][j] + 1 for j in range(len(grid[i]))
    ] for i in range(len(grid))]


def charge(i, j, grid, flashed):
    if (0 <= i <= len(grid) - 1) and \
            (0 <= j <= len(grid[i]) - 1):
        if flashed[i][j] == 0:
            grid[i][j] += 1


def flash(grid, flashed):
    dimi, dimj = len(grid), len(grid[0])
    new_grid = deepcopy(grid)
    new_flashed = deepcopy(flashed)
    for i in range(dimi):
        for j in range(dimj):
            if (new_grid[i][j] > 9) and (new_flashed[i][j] == 0):
                new_grid[i][j] = 0
                new_flashed[i][j] = 1

                charge(i - 1, j, new_grid, new_flashed)
                charge(i + 1, j, new_grid, new_flashed)
                charge(i, j - 1, new_grid, new_flashed)
                charge(i, j + 1, new_grid, new_flashed)
                charge(i - 1, j - 1, new_grid, new_flashed)
                charge(i + 1, j - 1, new_grid, new_flashed)
                charge(i - 1, j + 1, new_grid, new_flashed)
                charge(i + 1, j + 1, new_grid, new_flashed)
    return new_grid, new_flashed, new_flashed != flashed


with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        grid.append([int(i) for i in line.strip()])

total = sum(1 for row in grid for _ in row)

i = 0
while True:
    i += 1
    grid = step(grid)
    flashed = [[0 for _ in row] for row in grid]
    repeat = True
    while repeat:
        grid, flashed, repeat = flash(grid, flashed)
    result = sum(v for row in flashed for v in row)
    if result == total:
        break

print(f"Part 2: {i}")
