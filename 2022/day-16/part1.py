import heapq as hp

raw_dists = {}
rates = {}
dists = {}


def dijkstra(s, f, valves):
    visited = {}
    queue = [(0, s)]
    while queue:
        d, v = hp.heappop(queue)
        if v == f:
            return d
        if (v in visited) and (visited[v] < d):
            continue
        visited[v] = d
        for nv in valves[v]["tunnels"]:
            hp.heappush(queue, (d + 1, nv))


def dijkstra_valves(rates, dists, limit):
    pressures = []
    paths = []

    queue = [(0, 0, ["AA"])]

    while queue:
        p, sc, path = hp.heappop(queue)
        cur = path[-1]
        if p > limit:
            continue
        next_step = []
        for nx, d in dists[cur].items():
            if nx in path:
                continue
            if d > limit - p - 1:
                continue
            np = p + d + 1
            nsc = sc + rates[nx] * (limit - np)
            next_step.append((np, nsc, path + [nx]))
        if next_step:
            for i in next_step:
                hp.heappush(queue, i)
        else:
            pressures.append(sc)
            paths.append(path[1:])
    return pressures, paths


with open("../../_inputs/2022/day-16/input.txt", "r", encoding="utf8") as f:
    for line in f:
        fst, snd = line.strip().split(";")
        fst = fst.split()
        snd=snd.split()

        tmp_valve = fst[1]
        tmp_rate = int(fst[4].split("=")[1])
        if tmp_rate > 0:
            rates[tmp_valve] = tmp_rate

        raw_dists[tmp_valve] = {
            "tunnels": [l.strip(",") for l in snd[4:]]
        }

dists["AA"] = {}
for i in rates:
    dists["AA"][i] = dijkstra("AA", i, raw_dists)
    if i not in dists:
        dists[i] = {}
    for j in rates:
        if i == j:
            continue
        if j not in dists:
            dists[j] = {}
        dists[i][j] = dijkstra(i, j, raw_dists)
        dists[j][i] = dists[i][j]

ps, _ = dijkstra_valves(rates, dists, 30)
print(f"Part 1: {max(ps)}")

results = zip(*dijkstra_valves(rates, dists, 26))
ps, paths = zip(*sorted(results, reverse=True))

i, j = 0, 1
while any(x in paths[i] for x in paths[j]):
    j += 1

limit = j

res = ps[i] + ps[j]
for i in range(limit):
    for j in range(i+1, limit + 1):
        if any(x in paths[i] for x in paths[j]):
            continue
        res = max(res, ps[i] + ps[j])
print(f"Part 2: {res}")
