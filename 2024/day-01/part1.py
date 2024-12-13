if __name__ == "__main__":
    left, right = [], []
    with open("_inputs/2024/day-01/input.txt", "r", encoding="utf8") as f:
        for l in f:
            n0, n1 = l.strip().split()
            left.append(int(n0))
            right.append(int(n1))

    res0 = 0
    for i, j in zip(sorted(left), sorted(right)):
        res0 += abs(i - j)

    res1 = 0
    for i in left:
        res1 += i * right.count(i)

    print(f"Part 1: {res0}")
    print(f"Part 2: {res1}")
