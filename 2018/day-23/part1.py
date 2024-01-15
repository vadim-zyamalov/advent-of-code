class Bot:
    def __init__(self, pos, r):
        self.x, self.y, self.z = pos
        self.r = r

    def dist(self, other):
        return (
            abs(self.x - other.x)
            + abs(self.y - other.y)
            + abs(self.z - other.z)
        )


def part2(bots):
    queue = []
    start = Bot([0, 0, 0], 0)

    for bot in bots:
        dist = bot.dist(start)
        queue.append((max(0, dist - bot.r), 1))
        queue.append((dist + bot.r, -1))
    queue.sort()

    overlaps = 0
    max_overlaps = 0
    min_dist = 0
    while queue:
        dist, over = queue.pop(0)
        overlaps += over
        if overlaps > max_overlaps:
            max_overlaps = overlaps
            min_dist = dist

    return min_dist


if __name__ == "__main__":
    with open("_inputs/2018/day-23/input.txt", "r", encoding="utf8") as f:
        bots = []
        max_r = 0
        max_bot = Bot([0, 0, 0], 0)

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

            cur_bot = Bot(pos, r)

            if r > max_r:
                max_r = r
                max_bot = cur_bot

            bots.append(cur_bot)

    result = sum(max_bot.dist(el) <= max_r for el in bots)
    print(f"Part 1: {result}")

    result = part2(bots)
    print(f"Part 2: {result}")
