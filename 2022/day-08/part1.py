def visible(r, c, forest):
    dimr, dimc = len(forest), len(forest[0])

    if (r == 0) or (r == dimr - 1) or (c == 0) or (c == dimc - 1):
        return 1

    res = 4
    for i in range(r - 1, -1, -1):
        if forest[i][c] >= forest[r][c]:
            res -= 1
            break
    for i in range(r + 1, dimr):
        if forest[i][c] >= forest[r][c]:
            res -= 1
            break
    for i in range(c - 1, -1, -1):
        if forest[r][i] >= forest[r][c]:
            res -= 1
            break
    for i in range(c + 1, dimc):
        if forest[r][i] >= forest[r][c]:
            res -= 1
            break

    return 1 if res > 0 else 0


def score(r, c, forest):
    dimr, dimc = len(forest), len(forest[0])

    res = 1
    tmp = 0
    for i in range(r - 1, -1, -1):
        tmp += 1
        if forest[i][c] >= forest[r][c]:
            break
    res *= tmp
    tmp = 0
    for i in range(r + 1, dimr):
        tmp += 1
        if forest[i][c] >= forest[r][c]:
            break
    res *= tmp
    tmp = 0
    for i in range(c - 1, -1, -1):
        tmp += 1
        if forest[r][i] >= forest[r][c]:
            break
    res *= tmp
    tmp = 0
    for i in range(c + 1, dimc):
        tmp += 1
        if forest[r][i] >= forest[r][c]:
            break
    res *= tmp

    return res


forest = []

with open("../../_inputs/2022/day-08/input.txt", "r", encoding="utf8") as f:
    for line in f:
        forest.append([int(i) for i in line.strip()])

res = sum(
    sum(visible(j, i, forest) for i in range(len(forest[0])))
    for j in range(len(forest))
)

print(f"Part 1: {res}")

res = max(
    max(score(j, i, forest) for i in range(len(forest[0]))) for j in range(len(forest))
)

print(f"Part 1: {res}")
