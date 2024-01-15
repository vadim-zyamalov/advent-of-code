import heapq as hq


def dist(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2])


def part2_incorrect(bots):
    queue = []
    start = (0, 0, 0)

    for bot in bots:
        d = dist(bot, start)
        queue.append((max(0, d - bot[3]), 1))
        queue.append((d + bot[3], -1))
    queue.sort()

    overlaps = 0
    max_overlaps = 0
    min_dist = 0
    while queue:
        d, over = queue.pop(0)
        overlaps += over
        if overlaps > max_overlaps:
            max_overlaps = overlaps
            min_dist = d

    return min_dist


def intersect_with_box(bot, box):
    d = 0
    for i in (0, 1, 2):
        box_lower, box_upper = box[0][i], box[1][i] - 1
        d += abs(bot[i] - box_lower) + abs(bot[i] - box_upper)
        d -= box_upper - box_lower
        # d == 0 если бот внутри
        # d > 0 если бот вне куба
    d //= 2
    # если бот вне куба, то d считается дважды
    return d <= bot[3]


def intersections_with_box(bots, box):
    return sum(intersect_with_box(bot, box) for bot in bots)


def part2_correct(bots, start=(0, 0, 0)):
    max_c = max(max(bot[i] + bot[3] for bot in bots) for i in (0, 1, 2))
    box_size = 1
    while box_size <= max_c:
        box_size *= 2

    init_box = (
        (-box_size, -box_size, -box_size),
        (box_size, box_size, box_size),
    )

    queue = [(-len(bots), -2 * box_size, 3 * box_size, init_box)]

    while queue:
        _, size, dd, box = hq.heappop(queue)
        if size == -1:
            return dd
        new_size = size // -2
        for octant in [
            (0, 0, 0),
            (0, 0, 1),
            (0, 1, 0),
            (0, 1, 1),
            (1, 0, 0),
            (1, 0, 1),
            (1, 1, 0),
            (1, 1, 1),
        ]:
            new_box0 = tuple(
                box[0][i] + new_size * octant[i] for i in (0, 1, 2)
            )
            new_box1 = tuple(new_box0[i] + new_size for i in (0, 1, 2))
            new_box = (new_box0, new_box1)
            new_inters = intersections_with_box(bots, new_box)
            new_dist = dist(start, new_box0)
            hq.heappush(queue, (-new_inters, -new_size, new_dist, new_box))


if __name__ == "__main__":
    with open("_inputs/2018/day-23/input.txt", "r", encoding="utf8") as f:
        bots = []
        max_r = 0
        max_bot = (0, 0, 0)

        for line in f:
            line = line.strip()
            if line == "":
                break
            *pos, r = tuple(
                int(el)
                for el in line.replace("pos=<", "")
                .replace(" r=", "")
                .replace(">", "")
                .split(",")
            )

            cur_bot = (*pos, r)

            if r > max_r:
                max_r = r
                max_bot = cur_bot

            bots.append(cur_bot)

    result = sum(dist(max_bot, el) <= max_r for el in bots)
    print(f"Part 1: {result}")

    result = part2_incorrect(bots)
    print(f"Part 2: {result}")

    result = part2_correct(bots)
    print(f"Part 2: {result}")
