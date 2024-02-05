import time
from itertools import product

CHECKS = ["N", "S", "W", "E"]
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def check_still(elves, nx_elves):
    return all(elf in nx_elves for elf in elves)


def check_move(pos, dir, elves):
    match dir:
        case "N":
            dx = [-1]
            dy = [-1, 0, 1]
        case "S":
            dx = [1]
            dy = [-1, 0, 1]
        case "W":
            dx = [-1, 0, 1]
            dy = [-1]
        case _:
            dx = [-1, 0, 1]
            dy = [1]
    return all((pos[0] + x, pos[1] + y) not in elves for x, y in product(dx, dy))


def check_lone(pos, elves):
    dx = [-1, 0, 1]
    dy = [-1, 0, 1]
    return all(
        (pos[0] + x, pos[1] + y) not in elves
        for x, y in product(dx, dy)
        if (x, y) != (0, 0)
    )


def cycle(elves, i):
    nx_pos = {}
    filter_pos = {}

    for elf in elves:
        if check_lone(elf, elves):
            nx_pos[elf] = elf
            if elf not in filter_pos:
                filter_pos[elf] = 1
        else:
            dx, dy = 0, 0
            for c in range(4):
                if check_move(elf, CHECKS[(i % 4 + c) % 4], elves):
                    dx, dy = MOVES[(i % 4 + c) % 4]
                    break
            nx_elf = (elf[0] + dx, elf[1] + dy)
            nx_pos[elf] = nx_elf
            if nx_elf not in filter_pos:
                filter_pos[nx_elf] = 0
            filter_pos[nx_elf] += 1

    for elf, nx_elf in nx_pos.items():
        if (nx_elf in filter_pos) and filter_pos[nx_elf] > 1:
            nx_pos[elf] = elf

    return tuple(sorted(nx_pos.values()))


def dump(elves):
    min_x = min(elf[0] for elf in elves)
    min_y = min(elf[1] for elf in elves)
    max_x = max(elf[0] for elf in elves)
    max_y = max(elf[1] for elf in elves)

    for row in range(min_x, max_x + 1, 1):
        for col in range(min_y, max_y + 1, 1):
            if (row, col) in elves:
                print("#", end="")
            else:
                print(".", end="")
        print()


def count_empty(elves):
    min_x = min(elf[0] for elf in elves)
    min_y = min(elf[1] for elf in elves)
    max_x = max(elf[0] for elf in elves)
    max_y = max(elf[1] for elf in elves)

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)


ELVES = []

with open("_inputs/2022/day-23/input.txt", "r", encoding="utf8") as f:
    row = -1
    for line in f:
        row += 1
        for col in range(len(line.strip())):
            if line[col] == "#":
                ELVES.append((row, col))

t0 = time.time()

ELVES_W = tuple(ELVES)

# print("Initial:")
# dump(ELVES_W)
# print()

for i in range(10):
    ELVES_W = cycle(ELVES_W, i)
    # print(f"Cycle {i}")
    # dump(ELVES_W)
    # print()

print(f"Part 1: {count_empty(ELVES_W)}")
print(f"  elapsed in {time.time() - t0:3.2f}")

t0 = time.time()

ELVES_W = ELVES.copy()

i = -1
while True:
    i += 1
    ELVES_NX = cycle(ELVES_W, i)
    if ELVES_W == ELVES_NX:
        break
    ELVES_W = ELVES_NX

print(f"Part 2: {i + 1}")
print(f"  elapsed in {time.time() - t0:3.2f}")
