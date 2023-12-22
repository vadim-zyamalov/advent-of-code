def drop(fig, fig_no, bricks, cubes):
    x0, y0, z0, x1, y1, z1 = fig

    bricks[fig_no] = []

    while True:
        if (x0 == x1) and (y0 == y1) and ((z0 - 1 == 0) or (x0, y0, z0 - 1) in cubes):
            for z in range(z0, z1 + 1):
                cubes[(x0, y0, z)] = fig_no
                bricks[fig_no].append((x0, y0, z))
            break
        elif (x0 == x1) and (
            (z0 - 1 == 0) or any((x0, ny, z0 - 1) in cubes for ny in range(y0, y1 + 1))
        ):
            for y in range(y0, y1 + 1):
                cubes[(x0, y, z0)] = fig_no
                bricks[fig_no].append((x0, y, z0))
            break
        elif (y0 == y1) and (
            (z0 - 1 == 0) or any((nx, y0, z0 - 1) in cubes for nx in range(x0, x1 + 1))
        ):
            for x in range(x0, x1 + 1):
                cubes[(x, y0, z0)] = fig_no
                bricks[fig_no].append((x, y0, z0))
            break

        z0 -= 1
        z1 -= 1


def adjacent(fig_no, bricks, below=True):
    result = []
    cur_brick = bricks[fig_no]

    if below and any(z == 1 for _, _, z in cur_brick):
        return result

    dz = -1 if below else 1

    for i_no, i_cubes in bricks.items():
        if i_no == fig_no:
            continue
        if any((x, y, z - dz) in cur_brick for x, y, z in i_cubes):
            result.append(i_no)

    return result


def part1(lower_bricks, upper_bricks):
    result = []

    for brick in lower_bricks:
        if upper_bricks[brick] == []:
            result.append(brick)
            continue

        removable = True
        for adj_brick in upper_bricks[brick]:
            if len(lower_bricks[adj_brick]) == 1:
                removable = False
                break
        if removable:
            result.append(brick)

    return len(result), result


def part2(removed, lower_bricks, upper_bricks):
    upper = []

    for r_brick in removed:
        upper += upper_bricks[r_brick]

    upper = [el for el in list(set(upper)) if el not in removed]

    next_bricks = []

    for adj_brick in upper:
        lower = lower_bricks[adj_brick]
        if all(el in removed for el in lower):
            next_bricks.append(adj_brick)

    if next_bricks:
        removed.extend(next_bricks)
        return part2(removed, lower_bricks, upper_bricks)
    return len(removed) - 1


if __name__ == "__main__":
    with open("_inputs/2023/day-22/input.txt", "r", encoding="utf8") as f:
        bricks = {}
        cubes = {}

        data = []
        for line in f:
            line = line.strip()
            if line == "":
                break
            p1, p2 = line.split("~")
            p1 = tuple(int(el) for el in p1.split(","))
            p2 = tuple(int(el) for el in p2.split(","))

            p1, p2 = min(p1, p2), max(p1, p2)

            data.append((*p1, *p2))

        data = sorted(data, key=lambda x: x[2])

        for i, fig in enumerate(data):
            drop(fig, i, bricks, cubes)

        below_bricks = {brick: adjacent(brick, bricks, True) for brick in bricks}
        above_bricks = {brick: adjacent(brick, bricks, False) for brick in bricks}

        res1, removable = part1(below_bricks, above_bricks)
        print(f"Part 1: {res1}")

        res2 = 0
        for brick in bricks:
            if brick in removable:
                continue
            res2 += part2([brick], below_bricks, above_bricks)
        print(f"Part 2: {res2}")
