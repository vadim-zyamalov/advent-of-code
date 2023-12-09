def diff(x: list[int]) -> list[int]:
    if len(x) <= 1:
        return x
    return [x2 - x1 for x1, x2 in zip(x[:-1], x[1:])]


def extrapolate(history: list[int]) -> tuple[int, int]:
    deltas = []
    cur = history

    while True:
        deltas.append(cur)

        if not any(cur):
            break

        cur = diff(cur)

    first, last = 0, 0
    for delta in deltas[-2::-1]:
        last = last + delta[-1]
        first = delta[0] - first

    return first, last


if __name__ == "__main__":
    histories = []
    with open("_inputs/2023/day-09/input.txt", "r", encoding="utf8") as f:
        for line in f:
            if line.strip() == "":
                break
            histories.append([int(el) for el in line.strip().split()])

    res1, res2 = 0, 0
    for history in histories:
        tmp1, tmp2 = extrapolate(history)
        res1 += tmp1
        res2 += tmp2
    print(f"Part 1: {res2}")
    print(f"Part 2: {res1}")
