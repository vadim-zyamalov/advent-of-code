DIRS = {(-1, 0), (1, 0), (0, -1), (0, 1)}


def next_pos(
    x: int, y: int, dx: int, dy: int, layout: list[str], Nr, Nc
) -> tuple[tuple[int, ...], ...]:
    if (
        (layout[x][y] == ".")
        or ((layout[x][y] == "-") and (dx == 0))
        or ((layout[x][y] == "|") and (dy == 0))
    ):
        if (0 <= (nx := x + dx) < Nr) and (0 <= (ny := y + dy) < Nc):
            return ((nx, ny, dx, dy),)
    if ((layout[x][y] == "-") and (dx != 0)) or ((layout[x][y] == "|") and (dy != 0)):
        res = ()
        if (0 <= (nx := x - dy) < Nr) and (0 <= (ny := y - dx) < Nc):
            res += ((nx, ny, -dy, -dx),)
        if (0 <= (nx := x + dy) < Nr) and (0 <= (ny := y + dx) < Nc):
            res += ((nx, ny, dy, dx),)
        return res
    if (
        (layout[x][y] == "\\")
        and (0 <= (nx := x + dy) < Nr)
        and (0 <= (ny := y + dx) < Nc)
    ):
        return ((nx, ny, dy, dx),)
    if (
        (layout[x][y] == "/")
        and (0 <= (nx := x - dy) < Nr)
        and (0 <= (ny := y - dx) < Nc)
    ):
        return ((nx, ny, -dy, -dx),)
    return ()


def process(layout: list[str], start=(0, 0), direction=(0, 1)) -> int:
    Nr, Nc = len(layout), len(layout[0])
    visited = []
    result = []

    queue = [(*start, *direction)]

    while queue:
        x, y, dx, dy = queue.pop()

        if (x, y, dx, dy) in visited:
            continue
        if (x, y) not in result:
            result.append((x, y))

        visited.append((x, y, dx, dy))
        next_tiles = next_pos(x, y, dx, dy, layout, Nr, Nc)
        for next_tile in next_tiles:
            if next_tile not in result:
                queue.append(next_tile)

    return len(result)


def process2(layout: list[str]) -> int:
    Nr, Nc = len(layout), len(layout[0])

    result = 0
    for x in range(Nr):
        if x % 5 == 0:
            print(f"{x}", end=", ")
        result = max(
            result,
            process(layout, (x, 0), (0, 1)),
            process(layout, (x, Nc - 1), (0, -1)),
        )
    print()

    for y in range(Nc):
        if y % 5 == 0:
            print(f"{y}", end=", ")
        result = max(
            result,
            process(layout, (0, y), (1, 0)),
            process(layout, (Nr - 1, y), (-1, 0)),
        )
    print()

    return result


if __name__ == "__main__":
    with open("./_inputs/2023/day-16/input.txt", "r", encoding="utf8") as f:
        layout = f.read().strip().split("\n")

        res1 = process(layout)
        print(f"Part 1: {res1}")

        res2 = process2(layout)
        print(f"Part 2: {res2}")
