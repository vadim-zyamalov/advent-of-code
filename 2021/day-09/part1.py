levels = []


def check(i, j, levels=levels):
    dimi, dimj = len(levels), len(levels[i])
    res = levels[i][j]
    if (i > 0) and (res >= levels[i-1][j]):
        return False
    if (i < dimi - 1) and (res >= levels[i+1][j]):
        return False
    if (j > 0) and (res >= levels[i][j-1]):
        return False
    if (j < dimj - 1) and (res >= levels[i][j+1]):
        return False
    return True


def basin(i, j, visited, levels=levels):
    cur = levels[i][j]
    if cur == 9:
        return 0
    dimi, dimj = len(levels), len(levels[i])
    res = 1
    visited[i][j] = 1
    if (i > 0) and (visited[i-1][j] == 0):
        res += basin(i - 1, j, visited, levels)
    if (i < dimi - 1) and (visited[i+1][j] == 0):
        res += basin(i + 1, j, visited, levels)
    if (j > 0) and (visited[i][j-1] == 0):
        res += basin(i, j - 1, visited, levels)
    if (j < dimj - 1) and (visited[i][j+1] == 0):
        res += basin(i, j + 1, visited, levels)
    return res



with open("./input.txt", "r") as f:
    for line in f:
        levels.append([int(i) for i in line.strip()])

res = 0
for i in range(len(levels)):
    for j in range(len(levels[i])):
        if check(i, j, levels):
            res += 1 + levels[i][j]

print("Part 1: {}".format(res))

res = []
visited = [[0 for _ in range(len(levels[i]))] for i in range(len(levels))]
for i in range(len(levels)):
    for j in range(len(levels[i])):
        if check(i, j, levels):
            res.append(basin(i, j, visited, levels))
res.sort()
print("Part 2: {}".format(res[-1] * res[-2] * res[-3]))
