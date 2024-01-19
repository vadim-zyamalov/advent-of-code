from collections import defaultdict
import math as m


def angdist(p0, p1):
    d0, d1 = p1[0] - p0[0], p1[1] - p0[1]
    ang = m.atan2(d0, d1)
    _ang = m.atan2(-d0, -d1)
    dist = abs(d0) + abs(d1)
    return ang, _ang, dist


def angdists(asteroids):
    N = len(asteroids)
    result = defaultdict(list)
    for i in range(N - 1):
        ai = asteroids[i]
        for j in range(i + 1, N):
            aj = asteroids[j]
            ang, _ang, dist = angdist(ai, aj)
            result[ai].append((ang, dist, aj))
            result[aj].append((_ang, dist, ai))
    return result


def queues(data):
    queues = defaultdict(list)
    for ang, dist, aster in data:
        queues[ang].append((dist, aster))
    for ang in queues:
        queues[ang].sort()
    return queues


def part1(asteroids):
    angles = {}
    max_num = 0
    max_asteroid = None
    asternet = angdists(asteroids)
    for aster, data in asternet.items():
        angles[aster] = set(ang for ang, _, _ in data)
        if len(angles[aster]) > max_num:
            max_num = len(angles[aster])
            max_asteroid = aster
    return max_num, max_asteroid, asternet[max_asteroid]


def part2(data, aim=200):
    lists = queues(data)
    angles = sorted(lists.keys(), reverse=True)

    N = len(angles)

    idx = 0
    killed = 0
    last = None

    while killed < aim:
        while len(lists[angles[idx]]) == 0:
            idx = (idx + 1) % N
        _, last = lists[angles[idx]].pop(0)
        killed += 1
        idx = (idx + 1) % N

    return 100 * last[0] + last[1]


if __name__ == "__main__":
    with open("_inputs/2019/day-10/input.txt", "r", encoding="utf8") as f:
        asteroids = [
            (x, y)
            for y, row in enumerate(f.read().strip().split("\n"))
            for x, el in enumerate(row)
            if el == "#"
        ]

    num, aster, data = part1(asteroids)
    print(f"Part 1: {num}")
    print(f"Part 2: {part2(data)}")
