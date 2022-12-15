def dist(s: tuple[int, int], b: tuple[int, int]):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])


def check(line, start, data, ss, bs):
    res = 0

    step = 0
    while True:
        stop = True
        c = (start + step, line)
        # if (c not in ss) and \
        #    (c not in bs):
        for s, _, d in data:
            dd = dist(c, s)
            if dd <= d:
                extra = (d - dd) + (2 if c[0] < s[0] else 0) * (s[0] - c[0])
                res += extra + 1
                step += extra
                stop = False
                break
        # else:
        #     stop = False
        if stop:
            break
        step += 1

    step = 1
    while True:
        stop = True
        c = (start - step, line)
        # if (c not in ss) and \
        #    (c not in bs):
        for s, _, d in data:
            dd = dist(c, s)
            if dd <= d:
                extra = (d - dd) + (2 if c[0] > s[0] else 0) * (c[0] - s[0])
                res += extra + 1
                step += extra
                stop = False
                break
        # else:
        #     stop = False
        if stop:
            break
        step += 1

    for s in ss:
        if s[1] == line:
            res -= 1
    for b in bs:
        if b[1] == line:
            res -= 1

    return res


def search(limx, limy, data, ss, bs):
    y = limy[0]
    while y <= limy[1]:
        if y % 10000 == 1:
            print(".", end="")
        if y % 100000 == 0:
            print()
        x = limx[0]
        while x <= limx[1]:
            cont = False
            if ((x, y) not in ss) and ((x, y) not in bs):
                for s, _, d in data:
                    dd = dist((x, y), s)
                    if dd <= d:
                        x += (d - dd) + (2 if x < s[0] else 0) * (s[0] - x)
                        cont = True
                        break
            else:
                cont = True
            if cont:
                x += 1
            else:
                print()
                return (x, y)
        y += 1


DATA = []
sensors = set()
beacons = set()
lower = float("inf")
upper = -float("inf")

with open("./input.txt", "r", encoding="utf8") as f:
    for line in f:
        s = (0, 0)
        b = (0, 0)
        fst, snd = line.strip().split(":")
        fst = fst.split()
        for el in fst:
            if el[-1] == ",":
                el = el[:-1]
            if el[0] == "x":
                s = (int(el.split("=")[1]), s[1])
            if el[0] == "y":
                s = (s[0], int(el.split("=")[1]))
        snd = snd.split()
        for el in snd:
            if el[-1] == ",":
                el = el[:-1]
            if el[0] == "x":
                b = (int(el.split("=")[1]), b[1])
            if el[0] == "y":
                b = (b[0], int(el.split("=")[1]))
        d = dist(s, b)
        lower = min(lower, b[1])
        upper = max(upper, b[1])
        DATA.append((s, b, d))
        sensors.add(s)
        beacons.add(b)

res = check(2000000, int((lower + upper) // 2), DATA, sensors, beacons)
print(f"Part 1: {res}")

res = search((0, 4000000), (0, 4000000), DATA, sensors, beacons)
print(f"Part 2: {4000000 * res[0] + res[1]}")
