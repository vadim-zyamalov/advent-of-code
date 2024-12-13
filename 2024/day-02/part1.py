def safe(report):
    diff = [i - j for i, j in zip(report[:-1], report[1:])]
    if not all(i > 0 for i in diff) and not all(i < 0 for i in diff):
        return False
    if not all(1 <= abs(i) <= 3 for i in diff):
        return False
    return True


def damp(report):
    if safe(report):
        return True
    for i in range(len(report)):
        if safe(report[:i] + report[(i + 1) :]):
            return True
    return False


if __name__ == "__main__":
    res0 = 0
    res1 = 0
    with open("_inputs/2024/day-02/input.txt", "r") as f:
        for l in f:
            levels = list(map(int, l.strip().split()))
            res0 += 1 if safe(levels) else 0
            res1 += 1 if damp(levels) else 0
    print(f"Part 1: {res0}")
    print(f"Part 2: {res1}")
