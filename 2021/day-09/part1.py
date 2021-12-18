levels = []


def check(i, j, levels=levels):
    dimi, dimj = len(levels), len(levels[i])
    result = levels[i][j]
    if (i > 0) and (result >= levels[i-1][j]):
        return False
    if (i < dimi - 1) and (result >= levels[i+1][j]):
        return False
    if (j > 0) and (result >= levels[i][j-1]):
        return False
    if (j < dimj - 1) and (result >= levels[i][j+1]):
        return False
    return True


def basin(i, j, visited, levels=levels):
    cur = levels[i][j]
    if cur == 9:
        return 0
    dimi, dimj = len(levels), len(levels[i])
    result = 1
    visited[i][j] = 1
    if (i > 0) and (visited[i-1][j] == 0):
        result += basin(i - 1, j, visited, levels)
    if (i < dimi - 1) and (visited[i+1][j] == 0):
        result += basin(i + 1, j, visited, levels)
    if (j > 0) and (visited[i][j-1] == 0):
        result += basin(i, j - 1, visited, levels)
    if (j < dimj - 1) and (visited[i][j+1] == 0):
        result += basin(i, j + 1, visited, levels)
    return result


with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        levels.append([int(i) for i in line.strip()])

result = 0
for i, _ in enumerate(levels):
    for j, _ in enumerate(levels[i]):
        if check(i, j, levels):
            result += 1 + levels[i][j]

print(f"Part 1: {result}")

result = []
visited = [[0 for _ in range(len(levels[i]))] for i in range(len(levels))]
for i in range(len(levels)):
    for j in range(len(levels[i])):
        if check(i, j, levels):
            result.append(basin(i, j, visited, levels))
result.sort()
print(f"Part 2: {result[-1] * result[-2] * result[-3]}")
