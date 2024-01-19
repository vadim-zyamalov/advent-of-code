DIRS = [
    (-1, 0, "|", "7", "F"),
    (0, -1, "-", "F", "L"),
    (1, 0, "|", "J", "L"),
    (0, 1, "-", "J", "7"),
]


def start(sketch: list[list[str]]) -> tuple[int, ...]:
    Nr, Nc = len(sketch), len(sketch[0])

    x, y = -1, -1
    for r, row in enumerate(sketch):
        for c, el in enumerate(row):
            if el == "S":
                x, y = r, c
                break
        if x != -1:
            break

    deltas = []
    for dx, dy, *tiles in DIRS:
        if (0 <= (nx := x + dx) < Nr) and (0 <= (ny := y + dy) < Nc):
            if sketch[nx][ny] in tiles:
                deltas.append(dx)
                deltas.append(dy)

    return x, y, *deltas


def next(
    d: int, x: int, y: int, dx: int, dy: int, sketch: list[list[str]]
) -> tuple[int, ...]:
    nx, ny = x + dx, y + dy
    match sketch[nx][ny]:
        case "L" | "7":
            return d + 1, nx, ny, dy, dx
        case "F" | "J":
            return d + 1, nx, ny, -dy, -dx

    return d + 1, nx, ny, dx, dy


def count(sketch: list[list[str]], loop: set) -> int:
    Nr, Nc = len(sketch), len(sketch[0])
    inside = False
    corner = ""
    res = 0

    xs, ys, dx1, dy1, dx2, dy2 = start(sketch)

    match (dx1, dy1, dx2, dy2):
        case (0, -1, 0, 1) | (0, 1, 0, -1):
            sketch[xs][ys] = "-"
        case (1, 0, -1, 0) | (-1, 0, 1, 0):
            sketch[xs][ys] = "|"
        case (0, -1, -1, 0) | (-1, 0, 0, -1):
            sketch[xs][ys] = "J"
        case (0, 1, -1, 0) | (-1, 0, 0, 1):
            sketch[xs][ys] = "L"
        case (0, 1, 1, 0) | (1, 0, 0, 1):
            sketch[xs][ys] = "F"
        case (0, -1, 1, 0) | (1, 0, 0, -1):
            sketch[xs][ys] = "7"

    for r in range(Nr):
        for c in range(Nc):
            if (r, c) not in loop and inside:
                res += 1
            if (r, c) in loop:
                tile = sketch[r][c]
                if tile in "LF":
                    corner = tile
                elif tile == "J":
                    if corner == "F":
                        inside = not inside
                    corner = ""
                elif tile == "7":
                    if corner == "L":
                        inside = not inside
                    corner = ""
                elif tile == "|":
                    inside = not inside

    return res


if __name__ == "__main__":
    with open("_inputs/2023/day-10/input.txt", "r", encoding="utf8") as f:
        sketch = []
        for line in f:
            line = line.strip()
            if line == "":
                break
            sketch.append(list(line))

    x1, y1, dx1, dy1, dx2, dy2 = start(sketch)
    x2, y2 = x1, y1
    d1, d2 = 0, 0
    loop = {(x1, y1)}
    while True:
        d1, x1, y1, dx1, dy1 = next(d1, x1, y1, dx1, dy1, sketch)
        d2, x2, y2, dx2, dy2 = next(d2, x2, y2, dx2, dy2, sketch)

        loop.add((x1, y1))
        loop.add((x2, y2))

        if (x1, y1) == (x2, y2):
            break

    print(f"Part 1: {d1}")

    res = count(sketch, loop)

    print(f"Part 2: {res}")
