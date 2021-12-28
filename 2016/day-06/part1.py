freq = {}
length = 0

with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        length += 1
        for i, letter in enumerate(line.strip()):
            if i not in freq:
                freq[i] = {}
            if letter not in freq[i]:
                freq[i][letter] = 0
            freq[i][letter] += 1

answer = ""
for i in freq:
    letter = ""
    maxq = 0
    for key, val in freq[i].items():
        if val > maxq:
            maxq = val
            letter = key
    answer += letter

print(f"Part 1: {answer}")

answer = ""
for i in freq:
    letter = ""
    minq = length
    for key, val in freq[i].items():
        if val < minq:
            minq = val
            letter = key
    answer += letter

print(f"Part 2: {answer}")
