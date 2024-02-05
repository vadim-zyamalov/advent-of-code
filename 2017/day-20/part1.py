from math import sqrt
from functools import reduce


def part1(points):
    minval = float("inf")
    res = -1
    for i in range(len(points)):
        tmp = sum(abs(x) for x in points[i]["a"])
        if tmp < minval:
            minval = tmp
            res = i
    return res


def roots(a, b, c):
    result = []
    if (a == 0) and (b == 0):
        pass
    elif a == 0:
        result = [-c / b]
    else:
        d = b**2 - 4 * a * c
        if d < 0:
            pass
        elif d == 0:
            result = [-b / (2 * a)]
        else:
            result = [(-b - sqrt(d)) / (2 * a), (-b + sqrt(d)) / (2 * a)]
    return sorted([int(x) for x in result if (int(x) == x) and (x > 0)])


def collide(p1, p2, rr=3):
    res = []
    for i in range(rr):
        a = (p1["a"][i] - p2["a"][i]) / 2
        b = p1["v"][i] - p2["v"][i] + a
        c = p1["p"][i] - p2["p"][i]
        res.append(set(roots(a, b, c)))
    return list(reduce(lambda x, y: x & y, res))


def part2(points, rr=3):
    N = len(points)
    cols = set()
    for i in range(N - 1):
        for j in range(i + 1, N):
            moments = collide(points[i], points[j], rr)
            points[i]["c"].update(moments)
            points[j]["c"].update(moments)
            cols.update(moments)
    cols = sorted(list(cols))
    gone = []

    for mm in cols:
        count = 0
        cands = []
        for i in range(N):
            if (i not in gone) and (mm in points[i]["c"]):
                count += 1
                cands.append(i)
        if count > 1:
            gone.extend(cands)

    return N - len(gone)


if __name__ == "__main__":
    with open("_inputs/2017/day-20/input.txt", "r", encoding="utf8") as f:
        points = []
        for line in f:
            point = {}
            tmp = line.strip().split(", ")
            for chunk in tmp:
                nums = []
                part = chunk[0]
                chunk = chunk[3:-1].split(",")
                for d in chunk:
                    nums.append(int(d))
                point[part] = nums
            point["c"] = set()
            points.append(point)

    print(f"Part 1: {part1(points)}")
    print(f"Part 2: {part2(points)}")
