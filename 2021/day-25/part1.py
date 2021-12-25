grid = []


def dump(grid):
    print()
    for row in grid:
        print("".join(row))
    print


def move_east(grid):
    moves = []
    dimi, dimj = len(grid), len(grid[0])
    for i in range(dimi):
        for j in range(dimj):
            if grid[i][j] == ".":
                continue
            if grid[i][j] == "v":
                continue
            if grid[i][(j + 1) % dimj] != ".":
                continue
            moves.append((i, j))
    if moves == []:
        return False
    for i, j in moves:
        grid[i][j] = "."
        grid[i][(j + 1) % dimj] = ">"
    return True


def move_south(grid):
    moves = []
    dimi, dimj = len(grid), len(grid[0])
    for j in range(dimj):
        for i in range(dimi):
            if grid[i][j] == ".":
                continue
            if grid[i][j] == ">":
                continue
            if grid[(i + 1) % dimi][j] != ".":
                continue
            moves.append((i, j))
    if moves == []:
        return False
    for i, j in moves:
        grid[i][j] = "."
        grid[(i + 1) % dimi][j] = "v"
    return True


with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        grid.append(list(line.strip()))

step = 1
while True:
    res_east = move_east(grid)
    res_south = move_south(grid)
    if not res_east and not res_south:
        break
    step += 1

print(f"Part 1: {step}")
