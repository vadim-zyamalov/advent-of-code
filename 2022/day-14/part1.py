def fill(line, grid: set):
    nodes = [
        (int(i), int(j))
        for l in line.split(" -> ")
        for (i, j) in [l.split(",")]
    ]
    for i in range(1, len(nodes)):
        if nodes[i][0] == nodes[i-1][0]:
            for j in range(min(nodes[i-1][1], nodes[i][1]),
                           max(nodes[i-1][1], nodes[i][1]) + 1):
                grid.add((nodes[i][0], j))
        else:
            for j in range(min(nodes[i-1][0], nodes[i][0]),
                           max(nodes[i-1][0], nodes[i][0]) + 1):
                grid.add((j, nodes[i][1]))


def max_grid(grid):
    res = 0
    for _, i in grid:
        res = max(res, i)
    return res


def fall(start, threshold, grid):
    coords = start
    while True:
        if (coords[0], coords[1] + 1) not in grid:
            coords = (coords[0], coords[1] + 1)
        elif (coords[0] - 1, coords[1] + 1) not in grid:
            coords = (coords[0] - 1, coords[1] + 1)
        elif (coords[0] + 1, coords[1] + 1) not in grid:
            coords = (coords[0] + 1, coords[1] + 1)
        else:
            grid.add(coords)
            return True
        if coords[1] >= threshold:
            return False


def fall_floor(start, threshold, grid):
    coords = start
    while True:
        if coords[1] + 1 == threshold + 2:
            grid.add(coords)
            return coords
        if (coords[0], coords[1] + 1) not in grid:
            coords = (coords[0], coords[1] + 1)
        elif (coords[0] - 1, coords[1] + 1) not in grid:
            coords = (coords[0] - 1, coords[1] + 1)
        elif (coords[0] + 1, coords[1] + 1) not in grid:
            coords = (coords[0] + 1, coords[1] + 1)
        else:
            grid.add(coords)
            return coords


TILES = set()

with open("../../_inputs/2022/day-14/input.txt", "r", encoding="utf8") as f:
    for line in f:
        fill(line.strip(), TILES)

max_level = max_grid(TILES)

TILES_BK = TILES.copy()

count = 0
while True:
    if not fall((500, 0), max_level, TILES):
        break
    count += 1

print(f"Part 1: {count}")

count = 0
while True:
    count += 1
    if fall_floor((500, 0), max_level, TILES_BK) == (500, 0):
        break

print(f"Part 2: {count}")
