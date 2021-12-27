import numpy as np

X = []
Y = []
Z = []
RANGES = []


class Cube:
    def __init__(self,
                 on=0,
                 xs=(0, 0),
                 ys=(0, 0),
                 zs=(0, 0)) -> None:
        self.on = on
        self.x_0 = xs[0]
        self.x_0 = xs[1]
        self.y_0 = ys[0]
        self.y_0 = ys[1]
        self.z_0 = zs[0]
        self.z_0 = zs[1]

    def set_on(self, on):
        self.on = on

    def set_coords(self, cs, coord):
        if coord == 'x':
            self.x_0 = cs[0]
            self.x_1 = cs[1]
        if coord == 'y':
            self.y_0 = cs[0]
            self.y_1 = cs[1]
        if coord == 'z':
            self.z_0 = cs[0]
            self.z_1 = cs[1]


with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        range_current = Cube()
        status, rest = line.strip().split()
        range_current.set_on(int(status == "on"))
        tmp = rest.split(",")
        for r in tmp:
            coord, rest = r.split("=")
            r_low, r_high = (int(i) for i in rest.split(".."))
            r_high += 1
            range_current.set_coords((r_low, r_high), coord)
            if coord == 'x':
                X.append(r_low)
                X.append(r_high)
            if coord == 'y':
                Y.append(r_low)
                Y.append(r_high)
            if coord == 'z':
                Z.append(r_low)
                Z.append(r_high)
        RANGES.append(range_current)

X = list(set(X))
X.sort()
Y = list(set(Y))
Y.sort()
Z = list(set(Z))
Z.sort()

grid = [[[0 for _ in Z] for _ in Y] for _ in X]

for r in RANGES:
    for x in range(X.index(r.x_0), X.index(r.x_1)):
        for y in range(Y.index(r.y_0), Y.index(r.y_1)):
            for z in range(Z.index(r.z_0), Z.index(r.z_1)):
                grid[x][y][z] = r.on

answer = 0
for x in range(len(X) - 1):
    for y in range(len(Y) - 1):
        for z in range(len(Z) - 1):
            if grid[x][y][z] > 0:
                answer += (X[x + 1] - X[x]) * \
                    (Y[y + 1] - Y[y]) * \
                    (Z[z + 1] - Z[z])

print(f"Part 2: {answer}")
