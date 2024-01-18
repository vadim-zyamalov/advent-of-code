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


def replace_start(dx1, dy1, dx2, dy2) -> str:
    match (dx1, dy1, dx2, dy2):
        case (0, -1, 0, 1) | (0, 1, 0, -1):
            return "-"
        case (1, 0, -1, 0) | (-1, 0, 1, 0):
            return "|"
        case (0, -1, -1, 0) | (-1, 0, 0, -1):
            return "J"
        case (0, 1, -1, 0) | (-1, 0, 0, 1):
            return "L"
        case (0, 1, 1, 0) | (1, 0, 0, 1):
            return "F"
        case (0, -1, 1, 0) | (1, 0, 0, -1):
            return "7"
    return ""


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


def expand(sketch: list[list[str]], loop: set) -> list[list[str]]:
    Nc = len(sketch[0])

    res = [["."] * (Nc * 2 + 1)]

    for x, row in enumerate(sketch):
        str1, str2 = ".", "."

        for y, el in enumerate(row):
            if (x, y) in loop:
                match el:
                    case "|":
                        str1 += "|."
                        str2 += "|."
                    case "-":
                        str1 += "--"
                        str2 += ".."
                    case "F":
                        str1 += "F-"
                        str2 += "|."
                    case "7":
                        str1 += "7."
                        str2 += "|."
                    case "L":
                        str1 += "L-"
                        str2 += ".."
                    case "J":
                        str1 += "J."
                        str2 += ".."
            else:
                str1 += ".."
                str2 += ".."

        res.append(list(str1))
        res.append(list(str2))

    return res


def flood(data: list[list[str]]) -> None:
    Nx, Ny = len(data), len(data[0])

    queue = [(Nx - 1, Ny - 1)]

    while queue:
        x, y = queue.pop()
        data[x][y] = "X"

        for dx, dy, *_ in DIRS:
            if (0 <= (nx := x + dx) < Nx) and (0 <= (ny := y + dy) < Ny):
                if data[nx][ny] == ".":
                    queue.append((nx, ny))


def count(sketch: list[list[str]], loop: set) -> int:
    Nr, Nc = len(sketch), len(sketch[0])

    xs, ys, dx1, dy1, dx2, dy2 = start(sketch)

    sketch[xs][ys] = replace_start(dx1, dy1, dx2, dy2)

    expanded = expand(sketch, loop)

    flood(expanded)

    res = 0

    for i in range(1, 2 * Nr + 1, 2):
        for j in range(1, 2 * Nc + 1, 2):
            if expanded[i][j] == ".":
                res += 1

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
