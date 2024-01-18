def dist(p0, p1):
    return sum(abs(c0 - c1) for c0, c1 in zip(p0, p1))


def parse_points(points):
    constellations = 0
    mask = [False for p in points]

    for i, point in enumerate(points):
        if mask[i]:
            continue

        constellation = [point]
        mask[i] = True

        idx = 0

        while idx < len(constellation):
            for j, other in enumerate(points):
                if mask[j]:
                    continue
                if dist(constellation[idx], other) > 3:
                    continue
                mask[j] = True
                constellation.append(other)
            idx += 1
        constellations += 1

    return constellations


if __name__ == "__main__":
    with open("_inputs/2018/day-25/input.txt", "r", encoding="utf8") as f:
        points = [
            tuple(int(el) for el in point.split(","))
            for point in f.read().strip().split("\n")
        ]
    print(f"Part 1: {parse_points(points)}")
