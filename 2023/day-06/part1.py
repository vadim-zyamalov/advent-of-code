from math import sqrt, floor, ceil


def solve_times(time, dist):
    d = time**2 - 4 * dist
    if d < 0:
        return 0
    x1, x2 = (time - sqrt(d)) / 2, (time + sqrt(d)) / 2

    if x1 == ceil(x1):
        x1 += 1
    if x2 == floor(x2):
        x2 -= 1

    x1, x2 = ceil(x1), floor(x2)

    return x2 - x1 + 1


if __name__ == "__main__":
    with open("_inputs/2023/day-06/input.txt", "r", encoding="utf8") as f:
        times = [int(el) for el in f.readline().split(":")[1].strip().split()]
        dists = [int(el) for el in f.readline().split(":")[1].strip().split()]

    res = 1
    for t, d in zip(times, dists):
        res *= solve_times(t, d)

    print(f"Part 1: {res}")

    btime = int("".join(str(el) for el in times))
    bdist = int("".join(str(el) for el in dists))

    print(f"Part 2: {solve_times(btime, bdist)}")
