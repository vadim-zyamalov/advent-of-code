def mix_seq(numlist, poslist):
    POS = poslist.copy()
    for i in range(len(numlist)):
        cur_pos = POS.index(i)
        # Here's the magic hidden! :)
        nx_pos = (cur_pos + numlist[i]) % (len(numlist) - 1)
        if cur_pos < nx_pos:
            POS.insert(nx_pos + 1, i)
            POS.pop(cur_pos)
        elif cur_pos > nx_pos:
            POS.insert(nx_pos, i)
            POS.pop(cur_pos + 1)
        # print(f"{cur_pos:2d} {nx_pos:2d} {[numlist[pos] for pos in POS]}")
    return POS


def get_seq(numlist, poslist):
    return [numlist[pos] for pos in poslist]


def find_after_zero(numlist, pos):
    z_pos = numlist.index(0)
    return numlist[(z_pos + pos) % len(numlist)]


NUMBERS = []
MAGIC = 811589153

with open("./input.txt", "r", encoding="utf8") as f:
    for line in f:
        NUMBERS.append(int(line.strip()))
POS = list(range(len(NUMBERS)))

MIXED = get_seq(NUMBERS, mix_seq(NUMBERS, POS))
res = find_after_zero(MIXED, 1000) + \
    find_after_zero(MIXED, 2000) + \
    find_after_zero(MIXED, 3000)
print(f"Part 1: {res}")

NUMBERS = [el * MAGIC for el in NUMBERS]

for i in range(10):
    POS = mix_seq(NUMBERS, POS)
    # print(get_seq(NUMBERS, POS))

MIXED = get_seq(NUMBERS, POS)

res = find_after_zero(MIXED, 1000) + \
    find_after_zero(MIXED, 2000) + \
    find_after_zero(MIXED, 3000)
print(f"Part 2: {res}")

