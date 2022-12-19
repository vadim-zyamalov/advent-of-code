import parse


def next_pos(status, bp):
    robots, ores = status
    nx_pos = []

    for r in bp:
        if all(ores[i] >= bp[r][i] for i in range(len(ores))):
            nx_robots = robots[:r] + \
                (robots[r] + 1,) + \
                robots[(r+1):]
            nx_ores = tuple(ores[i] - bp[r][i] + robots[i] for i in range(len(ores)))
            nx_pos.append(
                (nx_robots,
                 nx_ores)
            )

    nx_ores = tuple(ores[i] + robots[i] for i in range(len(ores)))
    nx_pos.append(
        (robots,
         nx_ores)
    )

    return nx_pos



def dijkstra(bp, limit):
    queue = [((1, 0, 0, 0), (0, 0, 0, 0))]
    t = 0

    key = lambda s: [-v for i in range(3, -1, -1) for v in [s[0][i], s[1][i]]]
    while t < limit:
        nx_queue = []

        for st in queue:
            for nx_pos in next_pos(st, bp):
                nx_queue.append(nx_pos)

        queue = sorted(nx_queue, reverse=False, key=lambda s: key(s))[:10000]
        t += 1

    return max(v[1][3] for v in queue)


BLUEPRNT = {}

with open("./input.txt", "r", encoding="utf8") as f:
    for line in f:
        fst, snd = line.strip().split(": ")
        bp_id = int(fst.split()[1])
        BLUEPRNT[bp_id] = {}
        snd = snd.split(". ")
        for i in range(len(snd)):
            bp_ore = parse.search("{:d} ore", snd[i])
            bp_clay = parse.search("{:d} clay", snd[i])
            bp_obsidian = parse.search("{:d} obsidian", snd[i])
            bp_recipe = ()
            if bp_ore:
                bp_recipe = bp_recipe + (bp_ore.fixed[0],)
            else:
                bp_recipe = bp_recipe + (0,)
            if bp_clay:
                bp_recipe = bp_recipe + (bp_clay.fixed[0],)
            else:
                bp_recipe = bp_recipe + (0,)
            if bp_obsidian:
                bp_recipe = bp_recipe + (bp_obsidian.fixed[0],)
            else:
                bp_recipe = bp_recipe + (0,)
            bp_recipe = bp_recipe + (0,)
            BLUEPRNT[bp_id][i] = bp_recipe

res = 0
for bp in BLUEPRNT:
    res += bp * dijkstra(BLUEPRNT[bp], 24)

print(f"Part 1: {res}")

res = 1
for bp in [1,2,3]:
    res *= dijkstra(BLUEPRNT[bp], 32)

print(f"Part 2: {res}")
