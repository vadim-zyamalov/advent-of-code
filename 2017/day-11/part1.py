def sign(x):
    if x >= 0:
        return 1
    return -1


def count_dist(pos):
    res = 0
    if abs(pos[0]) >= abs(pos[1]):
        while abs(pos[1]) > 0:
            pos[0] -= 0.5 * sign(pos[0])
            pos[1] -= 0.5 * sign(pos[1])
            res += 1
        res += pos[0]
    else:
        while abs(pos[0]) > 0:
            pos[0] -= 0.5 * sign(pos[0])
            pos[1] -= 0.5 * sign(pos[1])
            res += 1
        res += abs(pos[1]) * 2
    return res


def process_path(path):
    pos : list[float] = [0, 0]
    max_dist = 0
    for step in path:
        match step:
            case "n":
                pos[0] -= 1
            case "s":
                pos[0] += 1
            case "ne":
                pos[0] -= 0.5
                pos[1] += 0.5
            case "se":
                pos[0] += 0.5
                pos[1] += 0.5
            case "nw":
                pos[0] -= 0.5
                pos[1] -= 0.5
            case "sw":
                pos[0] += 0.5
                pos[1] -= 0.5
        max_dist = max(max_dist, count_dist(pos.copy()))
    return pos, int(max_dist)


with open("../../_inputs/2017/day-11/input.txt", "r", encoding="utf-8") as f:
    PATH = f.read().strip().split(",")

POS, max_dist = process_path(PATH)

print(f"Part 1: {int(count_dist(POS.copy()))}")
print(f"Part 2: {max_dist}")
