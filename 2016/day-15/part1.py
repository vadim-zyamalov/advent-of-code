DISCS = {}


def test_moment(t, disc):
    return (t - DISCS[disc][1]) % DISCS[disc][0] == 0


with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        tmp = line.strip().split()
        disc_number = int(tmp[1][1:])
        disc_capacity = int(tmp[3])
        tmp_moment = int(tmp[6].split("=")[1][:-1])
        current_pos = (int(tmp[11][:-1]) - tmp_moment) % disc_capacity
        needed_pos = -disc_number % disc_capacity
        disc_shift = (needed_pos - current_pos) % disc_capacity
        DISCS[disc_number] = (disc_capacity, disc_shift)

test_t = 0
while True:
    if all(test_moment(test_t, d) for d in DISCS):
        print(f"Part 1: {test_t}")
        break
    test_t += 1

new_disc = max(DISCS.keys()) + 1
new_capacity = 11
new_position = 0
new_shift = ((-new_disc % new_capacity) - new_position) % new_capacity
DISCS[new_disc] = (new_capacity, new_shift)

test_t = 0
while True:
    if all(test_moment(test_t, d) for d in DISCS):
        print(f"Part 2: {test_t}")
        break
    test_t += 1
