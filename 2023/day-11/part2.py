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
    extra = sum(1 for r in exrows if x1 < r < x2)
    extra += sum(1 for c in excols if y1 < c < y2)
    extra *= exnum - 1

    return res + extra


if __name__ == "__main__":
    rows = []
    cols = []
    galaxies = []
    row = -1
    Ncols = -1
    with open("_inputs/2023/day-11/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            row += 1
            if Ncols == -1:
                Ncols = len(line)
                cols = list(range(Ncols))
            if all(el == "." for el in line):
                rows.append(row)
            else:
                for col in range(Ncols):
                    if line[col] == "#":
                        if col in cols:
                            cols.remove(col)
                        galaxies.append((row, col))

    res1 = 0
    res2 = 0
    Ngal = len(galaxies)
    for g1 in range(Ngal - 1):
        for g2 in range(g1 + 1, Ngal):
            res1 += exdist(galaxies[g1], galaxies[g2], rows, cols)
            res2 += exdist(galaxies[g1], galaxies[g2], rows, cols, 1_000_000)

    print(f"Part 1: {res1}")
    print(f"Part 2: {res2}")
