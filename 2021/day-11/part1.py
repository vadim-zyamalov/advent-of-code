grid = []
steps = 100


def deepcopy(original):
    return [[el for el in row] for row in original]


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
    if (i >= 0) and (i <= len(grid) - 1) and \
            (j >= 0) and (j <= len(grid[i]) - 1):
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


with open('input.txt', 'r') as f:
    for line in f:
        grid.append([int(i) for i in line.strip()])

result = 0
for i in range(steps):
    grid = step(grid)
    flashed = [[0 for _ in row] for row in grid]
    repeat = True
    while repeat:
        grid, flashed, repeat = flash(grid, flashed)
    result += sum(v for row in flashed for v in row)

print("Part 1: {}".format(result))
