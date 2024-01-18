def process(layout: list[str], start=(0, 0), direction=(0, 1)) -> int:
    Nr, Nc = len(layout), len(layout[0])

    visited = set()

    queue = [(*start, *direction)]

    while queue:
        x, y, dx, dy = queue.pop()

        while ((x, y, dx, dy) not in visited) and (0 <= x < Nr) and (0 <= y < Nc):
            visited.add((x, y, dx, dy))

            if (
                (layout[x][y] == ".")
                or ((layout[x][y] == "-") and (dx == 0))
                or ((layout[x][y] == "|") and (dy == 0))
            ):
                x, y = x + dx, y + dy
            elif ((layout[x][y] == "-") and (dx != 0)) or (
                (layout[x][y] == "|") and (dy != 0)
            ):
                queue.append((x - dy, y - dx, -dy, -dx))
                x, y, dx, dy = x + dy, y + dx, dy, dx
            elif layout[x][y] == "\\":
                x, y, dx, dy = x + dy, y + dx, dy, dx
            elif layout[x][y] == "/":
                x, y, dx, dy = x - dy, y - dx, -dy, -dx

    return len(set((x, y) for x, y, *_ in visited))


def process2(layout: list[str]) -> int:
    Nr, Nc = len(layout), len(layout[0])

    result = 0
    for x in range(Nr):
        result = max(
            result,
            process(layout, (x, 0), (0, 1)),
            process(layout, (x, Nc - 1), (0, -1)),
        )

    for y in range(Nc):
        result = max(
            result,
            process(layout, (0, y), (1, 0)),
            process(layout, (Nr - 1, y), (-1, 0)),
        )

    return result


if __name__ == "__main__":
    with open("./_inputs/2023/day-16/input.txt", "r", encoding="utf8") as f:
        layout = f.read().strip().split("\n")

        res1 = process(layout)
        print(f"Part 1: {res1}")

        res2 = process2(layout)
        print(f"Part 2: {res2}")
