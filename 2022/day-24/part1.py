import functools
import math


@functools.cache
def move_blizzards(blizzards, time, dimx, dimy):
    res = set()
    for x, y, dx, dy in blizzards:
        res.add(((x + dx * time) % dimx,
                 (y + dy * time) % dimy))
    return res


def move_pos(pos, blizzards, walls):
    res = []
    x, y = pos
    for dx, dy in [(1, 0), (0, 1), (0, -1), (-1, 0), (0, 0)]:
        nx_x, nx_y = x + dx, y + dy
        if ((nx_x, nx_y) not in blizzards) and ((nx_x, nx_y) not in walls):
            res.append((nx_x, nx_y))
    return res


def bfs(start, finish, start_time, blizzards, walls, dimx, dimy):
    queue = [(start_time, start)]
    visited = set()

    while queue:
        t, pos = queue.pop(0)
        t += 1
        for nx_pos in move_pos(pos,
                               move_blizzards(blizzards,
                                              t % math.lcm(dimx, dimy),
                                              dimx, dimy),
                               walls):
            if (t, nx_pos) not in visited:
                if nx_pos == finish:
                    return t
                visited.add((t, nx_pos))
                queue.append((t, nx_pos))


BLIZZARDS = ()
WALLS = ()

with open("./input.txt", "r", encoding="utf8") as f:
    row = -1
    for line in f:
        line = line.strip()
        row += 1
        for col in range(len(line)):
            match line[col]:
                case "^":
                    BLIZZARDS += ((row - 1, col - 1, -1, 0),)
                case "v":
                    BLIZZARDS += ((row - 1, col - 1, 1, 0),)
                case "<":
                    BLIZZARDS += ((row - 1, col - 1, 0, -1),)
                case ">":
                    BLIZZARDS += ((row - 1, col - 1, 0, 1),)
                case "#":
                    WALLS += ((row - 1, col - 1), )
                case _:
                    pass
    dimx, dimy = max(el for el in WALLS)

WALLS += ((-2, 0),)
WALLS += ((dimx + 1, dimy - 1),)

# print(sorted(WALLS))
res = bfs((-1, 0), (dimx, dimy - 1), 0, BLIZZARDS, WALLS, dimx, dimy)
print(f"Part 1: {res}")

res = bfs((-1, 0), (dimx, dimy - 1),
          bfs((dimx, dimy - 1), (-1, 0), res, BLIZZARDS, WALLS, dimx, dimy)
          , BLIZZARDS, WALLS, dimx, dimy)
print(f"Part 2: {res}")

