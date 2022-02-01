MOVES = [(1, 0),
         (0, -1),
         (-1, 0),
         (0, 1)]


def expand(grid):
    result = []
    size = len(grid)
    result.append(list(0 for _ in range(size + 2)))
    for row in grid:
        result.append([0] + row + [0])
    result.append(list(0 for _ in range(size + 2)))
    return result


with open("./input.txt", "r", encoding="utf-8") as f:
    number = int(f.readline().strip())

base = 1
while base ** 2 <= number:
    base += 2

answer = number - (base - 2) ** 2
while answer >= base:
    answer -= base - 1
answer = max(answer, base - (answer + 1))

print(f"Part 1: {answer}")

grid = [[1]]

i, j = 0, 0
dm = 0
current = 1

while current <= number:
    if (i == len(grid) - 1) and \
       (j == len(grid) - 1):
        grid = expand(grid)
        i += 1
        j += 1
    if (i == len(grid) - 1) and \
       dm == 0:
        dm = 1
    if (j == 0) and \
       dm == 1:
        dm = 2
    if (i == 0) and \
       dm == 2:
        dm = 3
    if (j == len(grid) - 1) and \
       dm == 3:
        dm = 0
    i, j = i + MOVES[dm][0], j + MOVES[dm][1]
    grid[i][j] = sum(x
                     for row in grid[max(0, i-1):i+2]
                     for x in row[max(0, j-1):j+2])
    current = grid[i][j]

print(f"Part 2: {current}")
