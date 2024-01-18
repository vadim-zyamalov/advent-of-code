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


def knot_step(prog):
    prog = [int(i) for i in prog.split(",")]

    LIST = [i for i in range(256)]
    POS = 0
    SKIP = 0

    for l in prog:
        LIST, POS, SKIP = process_list(l, LIST, POS, SKIP)

    return LIST[0] * LIST[1]


def knot_hash(prog, extra=[17, 31, 73, 47, 23]):
    prog = [ord(c) for c in prog]
    prog.extend(extra)

    LIST = [i for i in range(256)]
    POS = 0
    SKIP = 0

    for i in range(64):
        for l in prog:
            LIST, POS, SKIP = process_list(l, LIST, POS, SKIP)

    res = []

    for i in range(16):
        res.append(reduce(lambda x, y: x ^ y, LIST[(16 * i) : (16 * (i + 1))]))

    return "".join(f"{i:02x}" for i in res)


with open("_inputs/2017/day-10/input.txt", "r", encoding="utf-8") as f:
    line = f.read().strip()

print(f"Part 1: {knot_step(line)}")
print(f"Part 2: {knot_hash(line)}")
