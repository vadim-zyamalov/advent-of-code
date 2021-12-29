DISCS = {}


def test_moment(t, disc):
    N, start_pos = DISCS[disc]
    needed_pos = -disc % N
    shift = (needed_pos - start_pos) % N
    return (t - shift) % N == 0


with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        tmp = line.strip().split()
        number = int(tmp[1][1:])
        pos_num = int(tmp[3])
        tmp_moment = int(tmp[6].split("=")[1][:-1])
        cur_pos = (int(tmp[11][:-1]) - tmp_moment) % pos_num
        DISCS[number] = (pos_num, cur_pos)

test_t = 0
while True:
    if all(test_moment(test_t, d) for d in DISCS):
        print(f"Part 1: {test_t}")
        break
    test_t += 1

max_disc = max(DISCS.keys())
DISCS[max_disc + 1] = (11, 0)

test_t = 0
while True:
    if all(test_moment(test_t, d) for d in DISCS):
        print(f"Part 2: {test_t}")
        break
    test_t += 1
