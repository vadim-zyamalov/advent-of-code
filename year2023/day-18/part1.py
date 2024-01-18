DIRS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
DIRN = "RDLU"


def shape(trench: set[tuple[int, ...]]) -> tuple[int, ...]:
    lx, ly = 0, 0
    ux, uy = 0, 0

    for x, y in trench:
        lx = x if lx is None else min(x, lx)
        ux = x if ux is None else max(x, ux)
        ly = y if ly is None else min(y, ly)
        uy = x if uy is None else max(y, uy)

    return lx, ux, ly, uy


def area(trench: set[tuple[int, ...]]) -> int:
    lx, ux, ly, uy = shape(trench)
    lx -= 1
    ly -= 1
    ux += 1
    uy += 1

    total_area = (ux - lx + 1) * (uy - ly + 1)

    outer = set()

    queue = [(lx, ly)]

    while queue:
        x, y = queue.pop()
        if (x, y) not in trench and (x, y) not in outer:
            outer.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (lx <= (nx := x + dx) <= ux) and (ly <= (ny := y + dy) <= uy):
                    queue.append((nx, ny))

    return total_area - len(outer)


def dump(trench):
    lx, ux, ly, uy = shape(trench)
    for i in range(lx, ux + 1):
        for j in range(ly, uy + 1):
            if (i, j) in trench:
                print("#", end="")
            else:
                print(".", end="")
        print()


def vertices(prog):
    result = []

    x, y = 0, 0

    for (dx, dy), steps in prog:
        result.append((x, y))
        x += dx * steps
        y += dy * steps

    return result


def area2(prog):
    result = 0
    length = 0

    verts = vertices(prog)
    verts.append(verts[0])
    verts.reverse()

    for (x0, y0), (x1, y1) in zip(verts[:-1], verts[1:]):
        result += (x0 * y1 - x1 * y0) / 2
        length += abs(x0 - x1) + abs(y0 - y1)

    return int(result + length / 2 + 1)


if __name__ == "__main__":
    with open("_inputs/2023/day-18/input.txt") as f:
        prog = []
        prog2 = []

        for line in f:
            line = line.strip()
            if line == "":
                break
            d, steps, colour = line.split()
            prog.append((DIRS[d], int(steps)))

            colour = colour.strip("(#)")
            steps = int(colour[:-1], 16)
            dx, dy = DIRS[DIRN[int(colour[-1])]]
            prog2.append(((dx, dy), steps))

        x, y = 0, 0
        trench = {(x, y)}

        for (dx, dy), steps in prog:
            for i in range(1, steps + 1):
                x += dx
                y += dy
                trench.add((x, y))

        # dump(trench)
        res1 = area(trench)
        print(f"Part 1: {res1} (floodfill)")

        res1 = area2(prog)
        print(f"Part 1: {res1}")

        res2 = area2(prog2)
        print(f"Part 2: {res2}")
