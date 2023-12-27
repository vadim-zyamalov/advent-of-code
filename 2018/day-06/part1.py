def inner(coords):
    result = []

    for x, y in coords:
        if (
            any(ax - x >= abs(ay - y) for ax, ay in coords if ax > x)
            and any(x - ax >= abs(ay - y) for ax, ay in coords if ax < x)
            and any(ay - y >= abs(ax - x) for ax, ay in coords if ay > y)
            and any(y - ay >= abs(ax - x) for ax, ay in coords if ay < y)
        ):
            result.append((x, y))
            continue

    return result


def closest(x, y, coords):
    dist = 1_000_000
    point = ()

    if (x, y) in coords:
        return 0, (x, y)

    for cx, cy in coords:
        dd = abs(cx - x) + abs(cy - y)
        if dist > dd:
            dist = dd
            point = (cx, cy)
        elif dist == dd:
            point = ()

    return dist, point


def part1(coords):
    lx, ly = 1_000_000, 1_000_000
    ux, uy = -1_000_000, -1_000_000
    for x, y in coords:
        lx, ly = min(x, lx), min(y, ly)
        ux, uy = max(x, ux), max(y, uy)

    inners = inner(coords)

    dists = {point: 0 for point in inners}

    for x in range(lx, ux + 1):
        for y in range(ly, uy + 1):
            _, point = closest(x, y, coords)
            if point in dists:
                dists[point] += 1

    return max(dists.values())


def part2(coords, limit=10_000):
    lx, ly = 1_000_000, 1_000_000
    ux, uy = -1_000_000, -1_000_000
    for x, y in coords:
        lx, ly = min(x, lx), min(y, ly)
        ux, uy = max(x, ux), max(y, uy)

    result = 0

    for x in range(lx, ux + 1):
        for y in range(ly, uy + 1):
            result += sum(abs(cx - x) + abs(cy - y) for cx, cy in coords) < limit

    return result


if __name__ == "__main__":
    with open("./_inputs/2018/day-06/input.txt", "r", encoding="utf8") as f:
        coords = [
            tuple(map(int, point.split(","))) for point in f.read().strip().split("\n")
        ]

        print(f"Part 1: {part1(coords)}")
        print(f"Part 2: {part2(coords)}")
