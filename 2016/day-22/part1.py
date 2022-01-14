from itertools import product

NODES = {}

with open("./input.txt", "r", encoding="utf-8") as f:
    max_x = -1
    max_y = -1
    for line in f:
        if line.strip() == "":
            continue
        if not line.startswith("/dev/"):
            continue
        tmp = line.strip().split()
        tmp_node = tmp[0].split("/")[3].split("-")
        tmp_x = int(tmp_node[1][1:])
        tmp_y = int(tmp_node[2][1:])
        if tmp_x not in NODES:
            NODES[tmp_x] = {}
        NODES[tmp_x][tmp_y] = (int(tmp[1][:-1]),
                               int(tmp[2][:-1]),
                               int(tmp[3][:-1]))
        max_x = max(max_x, tmp_x)
        max_y = max(max_y, tmp_y)

GRID = tuple(tuple(el for _, el in row.items()) for _, row in NODES.items())

answer = 0
for x_0, y_0 in product(range(max_x+1), range(max_y+1)):
    for x_1, y_1 in product(range(max_x+1), range(max_y+1)):
        if (x_0 == x_1) and (y_0 == y_1):
            continue
        if GRID[x_0][y_0][1] == 0:
            continue
        if GRID[x_0][y_0][1] > GRID[x_1][y_1][2]:
            continue
        answer += 1

print(f"Part 1: {answer}")

for i, _ in enumerate(GRID):
    for j, _ in enumerate(GRID[i]):
        if (i, j) == (max_x, 0):
            print("G", sep="", end="")
        elif (i, j) == (0, 0):
            print("O", sep="", end="")
        elif GRID[i][j][0] > 100:
            print("#", sep="", end="")
        elif GRID[i][j][1] == 0:
            print("_", sep="", end="")
        else:
            print(".", sep="", end="")
    print()
print()
