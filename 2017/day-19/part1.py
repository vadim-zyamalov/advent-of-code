DIR = {
    "u": (-1, 0, "lr"),
    "d": (1, 0, "lr"),
    "l": (0, -1, "ud"),
    "r": (0, 1, "ud"),
}


def next(cur: tuple[int, int], dir: str, plan: list[list], shape: tuple[int, int]):
    lx, ly = shape
    x, y = cur
    dx, dy, alts = DIR[dir]
    nx, ny = x + dx, y + dy

    if (-1 < nx < lx) and (-1 < nx < ly) and (plan[nx][ny] != " "):
        return (nx, ny), dir
    else:
        for k in alts:
            dx, dy, _ = DIR[k]
            nnx, nny = x + dx, y + dy
            if (-1 < nnx < lx) and (-1 < nny < ly) and (plan[nnx][nny] != " "):
                return (nnx, nny), k
    return (-1, -1), ""


def process(plan: list[list]):
    visited = ""
    steps = 0

    LX, LY = len(plan), len(plan[0])
    dir = "d"
    cur = 0, plan[0].index("|")

    while cur != (-1, -1):
        steps += 1
        x, y = cur
        if plan[x][y] not in ("|", "-", "+"):
            visited += plan[x][y]
        cur, dir = next(cur, dir, plan, (LX, LY))

    return visited, steps


if __name__ == "__main__":
    MAP = []
    with open("../../_inputs/2017/day-19/input.txt", "r", encoding="utf8") as f:
        for line in f:
            if line.strip("\n") == "":
                break
            MAP.append(list(line.strip("\n")))

    res, steps = process(MAP)
    print(f"Part 1: {res}")
    print(f"Part 2: {steps}")
