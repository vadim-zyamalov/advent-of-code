from itertools import combinations


def num(digits=6, rng=10, cond=lambda x: x >= 2):
    result = 0
    for pos in combinations(range(digits + rng - 1), rng - 1):
        pos = (-1,) + pos + (digits + rng - 1,)
        if any(
            cond(q) for q in [i1 - i0 - 1 for i0, i1 in zip(pos[:-1], pos[1:])]
        ):
            result += 1
    return result


def count(lower, digits=6, cond=lambda x: x >= 2):
    result = 0
    stack = []

    dgts = [9]
    while lower:
        lower, d = divmod(lower, 10)
        dgts = [d] + dgts

    if len(dgts) - 1 < digits:
        return num(digits=digits, rng=9, cond=cond)

    if len(dgts) - 1 > digits:
        return 0

    for i, (d0, d1) in enumerate(zip(dgts[:-1], dgts[1:])):
        if d0 <= d1:
            stack.append((d0 + 1, digits - i))
        else:
            stack.append((d0, digits - i))
            break

    while stack:
        d, n = stack.pop()
        result += num(digits=n, rng=9 - d + 1, cond=cond)

    return result


if __name__ == "__main__":
    with open("_inputs/2019/day-04/input.txt", "r", encoding="utf8") as f:
        lower, upper = tuple(map(int, f.read().strip().split("-")))
    print(f"Part 1: {count(lower) - count(upper)}")
    print(
        f"Part 2: {count(lower, cond=lambda x: x == 2) - count(upper, cond=lambda x: x == 2)}"
    )
