from collections import defaultdict
import time

DIRS = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}


class Cart:
    def __init__(self, pos, dpos):
        self.x, self.y = pos
        self.dx, self.dy = dpos
        self.dead = False
        self.cross = 0

    def turn(self, tile):
        match tile:
            case "\\":
                self.dx, self.dy = self.dy, self.dx
            case "/":
                self.dx, self.dy = -self.dy, -self.dx
            case "+":
                if self.cross == 0:
                    self.dx, self.dy = -self.dy, self.dx
                elif self.cross == 2:
                    self.dx, self.dy = self.dy, -self.dx
                self.cross = (self.cross + 1) % 3
            case _:
                pass

    def move(self, turns):
        if (self.x, self.y) == (0, 117):
            print(turns[(self.x, self.y)])
        self.turn(turns[(self.x, self.y)])
        self.x += self.dx
        self.y += self.dy

    def __repr__(self):
        return f"{int(self.x)},{int(self.y)}:{self.dx},{self.dy}"

    def __str__(self):
        return f"{int(self.x)},{int(self.y)}:{self.dx},{self.dy}"


if __name__ == "__main__":
    turns = defaultdict(str)
    carts = []

    with open("./_inputs/2018/day-13/input.txt", "r", encoding="utf8") as f:
        for r, row in enumerate(f.read().strip("\n").split("\n")):
            for c, el in enumerate(row):
                if el in "\\/+":
                    turns[(r, c)] = el
                elif el in "<>^v":
                    carts.append(Cart((r, c), DIRS[el]))

    t0 = time.time()
    part1 = True
    N = len(carts)

    while N > 1:
        carts.sort(key=lambda c: (c.x, c.y))
        for i in range(N):
            if carts[i].dead:
                continue

            carts[i].move(turns)

            for ci in range(N):
                if (i == ci) or carts[ci].dead:
                    continue
                if (carts[i].x, carts[i].y) == (carts[ci].x, carts[ci].y):
                    if part1:
                        print(f"Part 1: {int(carts[i].y)},{int(carts[i].x)}")
                        print(f"    took {time.time() - t0:.2f} secs")
                        part1 = False
                    carts[i].dead = True
                    carts[ci].dead = True
                    break

        carts = [c for c in carts if not c.dead]
        N = len(carts)

    print(f"Part 2: {int(carts[0].y)},{int(carts[0].x)}")
    print(f"    took {time.time() - t0:.2f} secs")
