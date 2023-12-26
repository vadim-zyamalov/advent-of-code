def part1(xs, ys, claims, grid):
    result = 0
    Nx, Ny = len(xs), len(ys)

    for x0, y0, x1, y1 in claims.values():
        ix0, ix1 = xs.index(x0), xs.index(x1)
        iy0, iy1 = ys.index(y0), ys.index(y1)

        for ix in range(ix0, ix1):
            for iy in range(iy0, iy1):
                grid[ix][iy] += 1

    for ix in range(Nx - 1):
        for iy in range(Ny - 1):
            if grid[ix][iy] > 1:
                result += (xs[ix + 1] - xs[ix]) * (ys[iy + 1] - ys[iy])

    return result


def part2(xs, ys, claims, grid):
    for idx, (x0, y0, x1, y1) in claims.items():
        ix0, ix1 = xs.index(x0), xs.index(x1)
        iy0, iy1 = ys.index(y0), ys.index(y1)

        if all(grid[ix][iy] == 1 for ix in range(ix0, ix1) for iy in range(iy0, iy1)):
            return idx

    return None


if __name__ == "__main__":
    with open("_inputs/2018/day-03/input.txt", "r", encoding="utf8") as f:
        claims = {}
        xs = set()
        ys = set()

        for line in f:
            line = line.strip()
            if line == "":
                break

            idn, claim = line.split("@")
            idn = int(idn[1:].strip())
            tl, shape = claim.strip().split(":")
            x0, y0 = [int(el) for el in tl.strip().split(",")]
            wx, wy = [int(el) for el in shape.strip().split("x")]

            claims[idn] = (x0, y0, x0 + wx, y0 + wy)
            xs.add(x0)
            xs.add(x0 + wx)
            ys.add(y0)
            ys.add(y0 + wy)

        xs = sorted(xs)
        ys = sorted(ys)

        Nx, Ny = len(xs), len(ys)
        grid = [[0 for _ in range(Ny - 1)] for _ in range(Nx - 1)]

        print(f"Part 1: {part1(xs, ys, claims, grid)}")
        print(f"Part 2: {part2(xs, ys, claims, grid)}")
