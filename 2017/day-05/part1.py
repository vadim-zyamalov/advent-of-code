ARRAY = []
with open("../../_inputs/2017/day-05/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        ARRAY.append(int(line.strip()))

LEN = len(ARRAY)
cur_pos = 0
res = 0

while cur_pos < LEN:
    cur_jump = ARRAY[cur_pos]
    ARRAY[cur_pos] += 1
    cur_pos += cur_jump
    res += 1

print(res)

ARRAY = []
with open("../../_inputs/2017/day-05/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        ARRAY.append(int(line.strip()))

LEN = len(ARRAY)
cur_pos = 0
res = 0

while cur_pos < LEN:
    cur_jump = ARRAY[cur_pos]
    if cur_jump > 2:
        ARRAY[cur_pos] -= 1
    else:
        ARRAY[cur_pos] += 1
    cur_pos += cur_jump
    res += 1

print(res)
