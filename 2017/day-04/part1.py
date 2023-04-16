with open("../../_inputs/2017/day-04/input.txt", "r", encoding="utf-8") as f:
    res = 0
    for line in f:
        words_l = line.strip().split()
        words_s = set(words_l)
        if len(words_l) == len(words_s):
            res += 1

print(f"Part 1: {res}")

with open("../../_inputs/2017/day-04/input.txt", "r", encoding="utf-8") as f:
    res = 0
    for line in f:
        words_l = line.strip().split()
        for i in range(len(words_l)):
            tmp = list(words_l[i])
            tmp.sort()
            words_l[i] = ''.join(tmp)
        words_s = set(words_l)
        if len(words_l) == len(words_s):
            res += 1

print(f"Part 2: {res}")
