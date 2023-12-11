def dist(g1: tuple[int, int], g2: tuple[int, int]) -> int:
    x1, y1 = g1
    x2, y2 = g2
    return abs(x1 - x2) + abs(y1 - y2)


def exdist(
    g1: tuple[int, int],
    g2: tuple[int, int],
    exrows: list[int] = [],
    excols: list[int] = [],
    exnum=2,
) -> int:
    x1, y1 = min(g1[0], g2[0]), min(g1[1], g2[1])
    x2, y2 = max(g1[0], g2[0]), max(g1[1], g2[1])

    res = dist(g1, g2)
    extra = 0
    if (s := sum(1 for r in exrows if x1 < r < x2)) > 0:
        extra += s * (exnum - 1)
    if (s := sum(1 for c in excols if y1 < c < y2)) > 0:
        extra += s * (exnum - 1)

    return res + extra


def parse(image: list[str]) -> tuple[list[tuple[int, int]], list[int], list[int]]:
    Nr, Nc = len(image), len(image[0])
    galaxies = []
    rows = []
    cols = list(range(Nc))

    for r in range(Nr):
        if all(el == "." for el in image[r]):
            rows.append(r)
        else:
            for c in range(Nc):
                if image[r][c] != ".":
                    if c in cols:
                        cols.remove(c)
                    galaxies.append((r, c))

    return galaxies, rows, cols


if __name__ == "__main__":
    image = []
    with open("_inputs/2023/day-11/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            image.append(line)

    galaxies, rows, cols = parse(image)

    res1 = 0
    res2 = 0
    Ngal = len(galaxies)
    for g1 in range(Ngal - 1):
        for g2 in range(g1 + 1, Ngal):
            res1 += exdist(galaxies[g1], galaxies[g2], rows, cols)
            res2 += exdist(galaxies[g1], galaxies[g2], rows, cols, 1_000_000)

    print(f"Part 1: {res1}")
    print(f"Part 2: {res2}")
