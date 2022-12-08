with open("./input.txt", "r", encoding="utf8") as f:
    res = 0
    res2 = 0
    for line in f:
        elves = [
            [int(i) for i in tmp.split("-")] for tmp in line.strip().split(",")
        ]
        if ((elves[0][0] >= elves[1][0]) and (elves[0][1] <= elves[1][1])) or \
           ((elves[0][0] <= elves[1][0]) and (elves[0][1] >= elves[1][1])):
            res += 1
        if ((elves[0][0] >= elves[1][0]) and (elves[0][0] <= elves[1][1])) or \
           ((elves[0][1] >= elves[1][0]) and (elves[0][1] <= elves[1][1])) or \
           ((elves[1][0] >= elves[0][0]) and (elves[1][0] <= elves[0][1])) or \
           ((elves[1][1] >= elves[0][0]) and (elves[1][1] <= elves[0][1])):
            res2 += 1

print(f"Part 1: {res}")
print(f"Part 2: {res2}")
