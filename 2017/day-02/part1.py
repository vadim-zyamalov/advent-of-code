GRID = []

with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        GRID.append([int(i) for i in line.strip().split()])

answer = 0
for row in GRID:
    answer += max(row) - min(row)

print(f"Part 1: {answer}")

answer = 0
for row in GRID:
    nextrow = False
    for i, digit_i in enumerate(row):
        for j, digit_j in enumerate(row):
            if i == j:
                continue
            if digit_i % digit_j == 0:
                answer += digit_i / digit_j
                nextrow = True
                break
        if nextrow:
            break

print(f"Part 2: {answer}")
