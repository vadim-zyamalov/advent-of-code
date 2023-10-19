from functools import reduce


def process_list(length, list_seq, pos, skip):
    LEN = len(list_seq)
    end_pos = (pos + length - 1) % LEN
    for i in range(length // 2):
        list_seq[(pos + i) % LEN], list_seq[(end_pos - i) % LEN] = (
            list_seq[(end_pos - i) % LEN],
            list_seq[(pos + i) % LEN],
        )
    return list_seq, pos + length + skip, skip + 1


with open("../../_inputs/2017/day-10/input.txt", "r", encoding="utf-8") as f:
    line = f.read().strip()
    PROG1 = [int(i) for i in line.split(",")]
    PROG2 = [ord(c) for c in line]
    PROG2.extend([17, 31, 73, 47, 23])

LIST = [i for i in range(256)]
POS = 0
SKIP = 0

for l in PROG1:
    LIST, POS, SKIP = process_list(l, LIST, POS, SKIP)

print(f"Part 1: {LIST[0] * LIST[1]}")

LIST = [i for i in range(256)]
POS = 0
SKIP = 0

for i in range(64):
    for l in PROG2:
        LIST, POS, SKIP = process_list(l, LIST, POS, SKIP)

res = []

for i in range(16):
    res.append(reduce(lambda x, y: x ^ y, LIST[(16 * i) : (16 * (i + 1))]))

res_str = "".join(f"{i:02x}" for i in res)
print(f"Part 2: {res_str}")
