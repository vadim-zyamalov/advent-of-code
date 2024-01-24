from math import lcm


def coord(xs, vs):
    N = len(xs)

    dv = [0] * N

    for i in range(N - 1):
        for j in range(i + 1, N):
            dx = xs[i] - xs[j]
            dv[i] += 1 if dx < 0 else -1 if dx > 0 else 0
            dv[j] += 1 if dx > 0 else -1 if dx < 0 else 0

    for i in range(N):
        vs[i] += dv[i]
        xs[i] += vs[i]


def coord_cycle(xs):
    cache = {}

    i = 0
    vs = [0] * len(xs)
    cache[tuple(xs + vs)] = 0

    while True:
        i += 1
        coord(xs, vs)
        if tuple(xs + vs) in cache:
            return cache[tuple(xs + vs)], i
        cache[tuple(xs + vs)] = i


def step(xyzs, vxyzs):
    for xs, vs in zip(xyzs, vxyzs):
        coord(xs, vs)


def total_energy(xyzs: list[list], vxyzs: list[list]):
    result = 0
    for x, y, z, vx, vy, vz in zip(*xyzs, *vxyzs):
        pot = abs(x) + abs(y) + abs(z)
        kin = abs(vx) + abs(vy) + abs(vz)
        result += pot * kin
    return result


if __name__ == "__main__":
    with open("./_inputs/2019/day-12/input.txt", "r", encoding="utf8") as f:
        moons = []
        for line in f:
            line = line.strip()
            if line == "":
                break
            moons.append(
                [int(el.strip()[2:]) for el in line.strip("<>").split(",")]
            )

    moons = list(map(list, zip(*moons)))
    _moons = [list(cs) for cs in moons]

    speeds = [[0] * len(cs) for cs in moons]

    for i in range(1000):
        step(moons, speeds)

    print(f"Part 1: {total_energy(moons, speeds)}")

    result = 1
    for xs in _moons:
        _, cl = coord_cycle(xs)
        result = lcm(result, cl)

    print(f"Part 2: {result}")
