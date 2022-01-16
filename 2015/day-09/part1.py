from itertools import permutations

route = {}


def collect_cities(rdict):
    result = set()
    for k in rdict:
        result.add(k)
        for kd in rdict[k]:
            result.add(kd)
    result = list(result)
    result.sort()
    return result


def collect_pair(c1, c2, rdict):
    if c1 in rdict and c2 in rdict[c1]:
        return rdict[c1][c2]
    if c2 in rdict and c1 in rdict[c2]:
        return rdict[c2][c1]
    return None


def collect_map(rdict):
    cities = collect_cities(rdict)
    matrix = [[None for _ in cities] for _ in cities]

    for c1, city1 in enumerate(cities):
        for c2, city2 in enumerate(cities):
            if c1 == c2:
                continue
            matrix[c1][c2] = collect_pair(
                city1, city2,
                rdict
            )
            matrix[c2][c1] = matrix[c1][c2]
    return matrix


def distance(candidate, matrix):
    result = 0
    for i in range(1, len(candidate)):
        if matrix[candidate[i-1]][candidate[i]] is None:
            return -1
        result += matrix[candidate[i-1]][candidate[i]]
    return result


with open("input.txt", "r") as f:
    result = []
    for line in f:
        city1, _, city2, _, dist = line.strip().split()
        if city1 not in route:
            route[city1] = {}
        route[city1][city2] = int(dist)

        cities = collect_cities(route)
        indices = [i for i in range(len(cities))]
        matrix = collect_map(route)

        candidates = permutations(indices)
        result = [distance(i, matrix) for i in candidates]

    print(f"Part 1: {min(result)}")
    print(f"Part 2: {max(result)}")
