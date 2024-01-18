def intersect(brick1, brick2):
    x0, y0, _, x1, y1, _ = brick1
    a0, b0, _, a1, b1, _ = brick2
    return ((a0 <= x0 <= a1) and (y0 <= b0 <= y1)) or (
        (x0 <= a0 <= x1) and (b0 <= y0 <= b1)
    )


def drop(fig, fig_no, bricks):
    x0, y0, z0, x1, y1, z1 = fig

    mz = 0
    for brick in bricks.values():
        if intersect(fig, brick):
            mz = max(mz, brick[-1])

    bricks[fig_no] = (x0, y0, mz + 1, x1, y1, mz + (z1 - z0) + 1)


def adjacent(fig_no, bricks, below=True):
    result = []
    cur_brick = bricks[fig_no]

    if below and (cur_brick[-1] == 1):
        return result

    dz = -1 if below else 1
    cur_z = 2 if below else -1
    i_z = -1 if below else 2

    for i_no, i_brick in bricks.items():
        if intersect(cur_brick, i_brick) and (cur_brick[cur_z] + dz == i_brick[i_z]):
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


def part2(remove, removed, lower_bricks, upper_bricks):
    upper = []

    for r_brick in remove:
        upper += upper_bricks[r_brick]

    upper = [el for el in list(set(upper)) if el not in removed]

    next_bricks = []

    for adj_brick in upper:
        lower = lower_bricks[adj_brick]
        if all(el in remove + removed for el in lower):
            next_bricks.append(adj_brick)

    if next_bricks:
        return part2(next_bricks, removed + next_bricks, lower_bricks, upper_bricks)

    return len(removed)


if __name__ == "__main__":
    with open("_inputs/2023/day-22/input.txt", "r", encoding="utf8") as f:
        bricks = {}

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
            drop(fig, i, bricks)

        below_bricks = {brick: adjacent(brick, bricks, True) for brick in bricks}
        above_bricks = {brick: adjacent(brick, bricks, False) for brick in bricks}

        res1, removable = part1(below_bricks, above_bricks)
        print(f"Part 1: {res1}")

        res2 = 0
        for brick in bricks:
            if brick in removable:
                continue
            res2 += part2([brick], [], below_bricks, above_bricks)
        print(f"Part 2: {res2}")
