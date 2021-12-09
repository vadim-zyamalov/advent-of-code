from itertools import permutations

route = {}


def collect_cities(rdict):
    res = set()
    for k in rdict:
        res.add(k)
        for kd in rdict[k]:
            res.add(kd)
    res = list(res)
    res.sort()
    return res


def collect_pair(c1, c2, rdict):
    if c1 in rdict and c2 in rdict[c1]:
        return rdict[c1][c2]
    elif c2 in rdict and c1 in rdict[c2]:
        return rdict[c2][c1]
    else:
        return None


def collect_map(rdict):
    cities = collect_cities(rdict)
    matrix = [[None for _ in cities] for _ in cities]

    for c1 in range(len(cities)):
        for c2 in range(len(cities)):
            if c1 == c2:
                continue
            matrix[c1][c2] = collect_pair(
                cities[c1], cities[c2],
                rdict
            )
            matrix[c2][c1] = matrix[c1][c2]
    return matrix


def distance(candidate, matrix):
    res = 0
    for i in range(1, len(candidate)):
        if matrix[candidate[i-1]][candidate[i]] is None:
            return None
        res += matrix[candidate[i-1]][candidate[i]]
    return res


with open("input.txt", "r") as f:
    res = []
    for line in f:
        city1, _, city2, _, dist = line.strip().split()
        if city1 not in route:
            route[city1] = {}
        route[city1][city2] = int(dist)

        cities = collect_cities(route)
        indices = [i for i in range(len(cities))]
        candidates = list(permutations(indices))
        matrix = collect_map(route)
        res = [distance(i, matrix) for i in candidates]

    print("Part 1: {}".format(min(res)))
    print("Part 2: {}".format(max(res)))
