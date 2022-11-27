from functools import reduce


def process_list(length):
    global POS
    global SKIP
    end_pos = (POS + length - 1) % LEN
    for i in range(length // 2):
        LIST[(POS + i) % LEN], LIST[(end_pos - i) % LEN] = \
            LIST[(end_pos - i) % LEN], LIST[(POS + i) % LEN]
    POS += length + SKIP
    SKIP += 1


with open("./input.txt", "r", encoding="utf-8") as f:
    line = f.read().strip()
    PROG1 = [int(i) for i in line.split(",")]
    PROG2 = [ord(c) for c in line]
    PROG2.extend([17, 31, 73, 47, 23])

LIST = [i for i in range(256)]
LEN = len(LIST)
POS = 0
SKIP = 0

for l in PROG1:
    process_list(l)

print(f"Part 1: {LIST[0] * LIST[1]}")

LIST = [i for i in range(256)]
LEN = len(LIST)
POS = 0
SKIP = 0

for i in range(64):
    for l in PROG2:
        process_list(l)

res = []

for i in range(16):
    res.append(reduce(lambda x, y: x ^ y, LIST[(16 * i):(16 * (i + 1))]))

res_str = ''.join(f"{i:02x}" for i in res)
print(f"Part 2: {res_str}")
