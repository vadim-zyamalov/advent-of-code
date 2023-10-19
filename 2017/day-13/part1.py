import copy


def update(map):
    for k in map:
        p, w, s = map[k]
        if -1 < p + s < w:
            map[k][0] += s
        else:
            map[k][2] *= -1
            map[k][0] -= s


def solve_p1(map):
    cmap = copy.deepcopy(map)

    result = 0
    caught = False
    fin = max(cmap.keys())

    for i in range(fin + 1):
        if i in cmap:
            if cmap[i][0] == 0:
                result += i * cmap[i][1]
                caught = True
        update(cmap)

    return result, caught


def solve_p2(map):
    result = 0
    cmap = copy.deepcopy(map)

    while True:
        result += 1
        if all((result + k) % (2 * (i[1] - 1)) != 0 for k, i in cmap.items()):
            return result


if __name__ == "__main__":
    scans = {}

    with open("../../_inputs/2017/day-13/input.txt", "r", encoding="utf8") as f:
        for line in f:
            layer, width = line.strip().split(":")
            scans[int(layer)] = [0, int(width), 1]

    print(f"Part 1: {solve_p1(scans)[0]}")
    print(f"Part 2: {solve_p2(scans)}")
