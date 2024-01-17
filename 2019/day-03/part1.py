from typing import NamedTuple


class Pos(NamedTuple("Pos", [("x", int), ("y", int)])):
    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)


def dist(p0, p1=Pos(0, 0)):
    return abs(p0.x - p1.x) + abs(p0.y - p1.y)


def intersections(w0, w1):
    result = []
    for b0, e0 in zip(w0[:-1], w0[1:]):
        b0, e0 = min(b0, e0), max(b0, e0)
        for b1, e1 in zip(w1[:-1], w1[1:]):
            b1, e1 = min(b1, e1), max(b1, e1)
            if ((b0.x < b1.x < e0.x) and (b1.y < b0.y < e1.y)) or (
                (b1.x < b0.x < e1.x) and (b0.y < b1.y < e0.y)
            ):
                if b0.x == e0.x:
                    result.append(Pos(b0.x, b1.y))
                else:
                    result.append(Pos(b1.x, b0.y))
    result.sort(key=lambda p: dist(p))
    return result


def timingw(path):
    result = {}

    pos = Pos(0, 0)
    lng = 0

    result[pos] = lng
    for p in path:
        d, s = p[0], int(p[1:])
        match d:
            case "U" | "D":
                dp = Pos(0, -1 if d == "U" else 1)
            case "L" | "R":
                dp = Pos(-1 if d == "L" else 1, 0)
        for _ in range(s):
            pos += dp
            lng += 1
            if pos not in result:
                result[pos] = lng
    return result


if __name__ == "__main__":
    with open("_inputs/2019/day-03/input.txt", "r", encoding="utf8") as f:
        pathes = [path.split(",") for path in f.read().strip().split("\n")]

    wires = []
    for path in pathes:
        wire = [Pos(0, 0)]
        for el in path:
            d, s = el[0], int(el[1:])
            match d:
                case "U":
                    wire.append(wire[-1] + Pos(0, -s))
                case "D":
                    wire.append(wire[-1] + Pos(0, s))
                case "L":
                    wire.append(wire[-1] + Pos(-s, 0))
                case "R":
                    wire.append(wire[-1] + Pos(s, 0))
        wires.append(wire)

    inters = intersections(*wires)
    print(f"Part 1: {dist(inters[0])}")

    times0 = timingw(pathes[0])
    times1 = timingw(pathes[1])
    print(f"Part 2: {min(times0[p] + times1[p] for p in inters)}")
