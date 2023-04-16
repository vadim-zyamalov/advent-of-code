ITEMS = [chr(i) for i in range(ord('a'), ord('z') + 1)] + \
    [chr(i) for i in range(ord("A"), ord("Z") + 1)]

with open("../../_inputs/2022/day-03/input.txt", "r", encoding="utf8") as f:
    res = 0
    for line in f:
        line = line.strip()
        fst = line[:len(line) // 2]
        snd = line[len(line) // 2:]
        for c in fst:
            if c in snd:
                res += ITEMS.index(c) + 1
                break

print(f"Part 1: {res}")

with open("../../_inputs/2022/day-03/input.txt", "r", encoding="utf8") as f:
    res = 0
    for line1, line2, line3 in zip(f, f, f):
        line1 = line1.strip()
        line2 = line2.strip()
        line3 = line3.strip()
        for c in line1:
            if (c in line2) and (c in line3):
                res += ITEMS.index(c) + 1
                break

print(f"Part 2: {res}")
