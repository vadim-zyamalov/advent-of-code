b = [0]
c = [0]

stack = []
PAIRS = []

digit = 0
i = 0
with open("./input.txt", "r", encoding="utf-8") as f:
    tmp_a = -1
    tmp_b = -1
    tmp_c = -1
    for line in f:
        if line.strip() == "":
            continue
        if line.startswith("inp"):
            tmp_a = -1
            tmp_b = -1
            tmp_c = -1
            digit += 1
            i = 0
            continue
        i += 1
        if i == 4:
            tmp_a = int(line.strip().split()[2])
        if i == 5:
            tmp_b = int(line.strip().split()[2])
        if i == 15:
            tmp_c = int(line.strip().split()[2])
            if tmp_a == 1:
                stack.append(digit)
            else:
                fst = stack.pop()
                PAIRS.append((fst, digit))
            b.append(tmp_b)
            c.append(tmp_c)


MAX = " " + "0" * 14
MIN = " " + "0" * 14

DIGITS = {}
for i in range(1, 15):
    DIGITS[i] = []

for digit_in, digit_out in PAIRS:
    for fst in range(1, 10):
        snd = fst + c[digit_in] + b[digit_out]
        if 0 < snd < 10:
            DIGITS[digit_in].append(fst)
            DIGITS[digit_out].append(snd)
    res_in  = max(DIGITS[digit_in])
    res_out = DIGITS[digit_out][DIGITS[digit_in].index(res_in)]
    MAX = MAX[:digit_in] + str(res_in) + \
        MAX[digit_in+1:digit_out] + \
        str(res_out) + MAX[digit_out+1:]
    res_in  = min(DIGITS[digit_in])
    res_out = DIGITS[digit_out][DIGITS[digit_in].index(res_in)]
    MIN = MIN[:digit_in] + str(res_in) + \
        MIN[digit_in+1:digit_out] + \
        str(res_out) + MIN[digit_out+1:]

print(f"Part 1: {MAX}")
print(f"Part 2: {MIN}")
