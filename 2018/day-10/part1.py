def part1(x, y, dx, dy):
    xs, ys, dxs, dys = x.copy(), y.copy(), dx.copy(), dy.copy()
    delta_x = max(xs) - min(xs)
    # delta_y = max(ys) - min(ys)
    secs = 0
    while True:
        secs += 1
        for i, (_dx, _dy) in enumerate(zip(dxs, dys)):
            xs[i] += _dx
            ys[i] += _dy
        d_x = max(xs) - min(xs)
        # d_y = max(ys) - min(ys)
        if delta_x >= d_x:
            delta_x = d_x
            # delta_y = d_y
        else:
            secs -= 1
            for i, (_dx, _dy) in enumerate(zip(dxs, dys)):
                xs[i] -= _dx
                ys[i] -= _dy
            break
    return xs, ys, secs


def dump(x, y):
    stars = sorted((_x, _y) for _x, _y in zip(x, y))
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)

    for _y in range(min_y, max_y + 1):
        for _x in range(min_x, max_x + 1):
            if (_x, _y) in stars:
                print("#", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    stars = []
    x, y, dx, dy = [], [], [], []
    with open("_inputs/2018/day-10/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            pos, vel = line.split("> ")
            _x, _y = [int(i) for i in pos.split("<")[1].split(",")]
            _dx, _dy = [int(i) for i in vel.strip(">").split("<")[1].split(",")]
            x.append(_x)
            y.append(_y)
            dx.append(_dx)
            dy.append(_dy)
    xs, ys, secs = part1(x, y, dx, dy)
    print("Part 1:")
    dump(xs, ys)
    print(f"Part 2: {secs}")
