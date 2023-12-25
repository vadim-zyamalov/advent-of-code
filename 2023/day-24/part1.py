import sympy as sp
import numpy as np

LB = 200_000_000_000_000
UB = 400_000_000_000_000


def inter2d(obj0, obj1):
    x0, y0, _, vx0, vy0, _ = obj0
    x1, y1, _, vx1, vy1, _ = obj1

    # y = (y0 - vy0/vx0 x0) + vy0/vx0 x
    # y = (y1 - vy1/vx1 x1) + vy1/vx1 x
    # 0 = y1 - vy1/vx1 x1 - y0 + (vy1/vx1 - vy0/vx0) x +

    slope0, slope1 = vy0 / vx0, vy1 / vx1
    if slope0 == slope1:
        if (x0 == x1) and (y0 == y1):
            return x0, y0, 0, 0
        else:
            return None, None, None, None
    inter_x = -((y1 - slope1 * x1) - (y0 - slope0 * x0)) / (slope1 - slope0)
    inter_y = y0 + slope0 * (inter_x - x0)
    inter_t0 = (inter_x - x0) / vx0
    inter_t1 = (inter_x - x1) / vx1

    return inter_x, inter_y, inter_t0, inter_t1


def part1(hails, bounds):
    result = 0
    lb, ub = bounds

    N = len(hails)

    for i in range(N - 1):
        for j in range(i, N):
            h0, h1 = hails[i], hails[j]
            x, y, t0, t1 = inter2d(h0, h1)
            if t0 is not None and t1 is not None and (t0 > 0) and (t1 > 0):
                if (lb <= x <= ub) and (lb <= y <= ub):
                    result += 1
    return result


def part2(hails, N):
    vars = sp.symbols("x y z vx vy vz " + " ".join(f"t_{i}" for i in range(N)))
    eqs = []
    for i, (x0, y0, z0, vx0, vy0, vz0) in enumerate(hails[:N]):
        formuli = [
            f"{x0} + {vx0} * t_{i} = x + vx * t_{i}",
            f"{y0} + {vy0} * t_{i} = y + vy * t_{i}",
            f"{z0} + {vz0} * t_{i} = z + vz * t_{i}",
        ]
        eqs += [sp.Eq(*map(sp.S, formula.split("=", 1))) for formula in formuli]

    roots = sp.solve(eqs, vars)[0]

    return sum(roots[:3])


def part2_lin(hails, N):
    x0, y0, z0, vx0, vy0, vz0 = hails[0]
    x1, y1, z1, vx1, vy1, vz1 = hails[1]
    x2, y2, z2, vx2, vy2, vz2 = hails[2]

    A = np.array(
        [
            [(vy1 - vy0), -(vx1 - vx0), 0, -(y1 - y0), (x1 - x0), 0],
            [(vy2 - vy0), -(vx2 - vx0), 0, -(y2 - y0), (x2 - x0), 0],
            [(vz1 - vz0), 0, -(vx1 - vx0), -(z1 - z0), 0, (x1 - x0)],
            [(vz2 - vz0), 0, -(vx2 - vx0), -(z2 - z0), 0, (x2 - x0)],
            [0, (vz1 - vz0), -(vy1 - vy0), 0, -(z1 - z0), (y1 - y0)],
            [0, (vz2 - vz0), -(vy2 - vy0), 0, -(z2 - z0), (y2 - y0)],
        ]
    )

    b = np.array(
        [
            (x1 * vy1 - y1 * vx1) - (x0 * vy0 - y0 * vx0),
            (x2 * vy2 - y2 * vx2) - (x0 * vy0 - y0 * vx0),
            (x1 * vz1 - z1 * vx1) - (x0 * vz0 - z0 * vx0),
            (x2 * vz2 - z2 * vx2) - (x0 * vz0 - z0 * vx0),
            (y1 * vz1 - z1 * vy1) - (y0 * vz0 - z0 * vy0),
            (y2 * vz2 - z2 * vy2) - (y0 * vz0 - z0 * vy0),
        ]
    ).T

    roots = np.linalg.solve(A, b)

    return sum(roots.flatten()[:3])


if __name__ == "__main__":
    with open("_inputs/2023/day-24/input.txt", "r", encoding="utf8") as f:
        hails = []
        for line in f:
            line = line.strip()
            if line == "":
                break

            xs, vs = line.split(" @ ")
            xs = [int(el.strip()) for el in xs.split(",")]
            vs = [int(el.strip()) for el in vs.split(",")]

            hails.append((*xs, *vs))

    print(f"Part 1: {part1(hails, (LB, UB))}")
    print(f"Part 2: {part2(hails, 5)}")
    print(f"Part 2: {part2_lin(hails, 5)} (linear)")
