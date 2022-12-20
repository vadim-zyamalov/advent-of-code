def mix_seq(numlist, poslist):
    POS = poslist.copy()
    for i in range(len(numlist)):
        cur_pos = POS.index(i)
        nx_pos = (cur_pos + numlist[i]) % (len(numlist) - 1)
        POS.pop(cur_pos)
        POS.insert(nx_pos, i)
    return POS


def get_seq(numlist, poslist):
    return [numlist[pos] for pos in poslist]


def find_after_zero(numlist, pos):
    z_pos = numlist.index(0)
    return numlist[(z_pos + pos) % len(numlist)]


NUMBERS = []
MAGIC = 811589153

with open("./sample.txt", "r", encoding="utf8") as f:
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

MIXED = get_seq(NUMBERS, POS)

res = find_after_zero(MIXED, 1000) + \
    find_after_zero(MIXED, 2000) + \
    find_after_zero(MIXED, 3000)
print(f"Part 2: {res}")

