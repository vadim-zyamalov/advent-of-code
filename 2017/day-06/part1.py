with open("../../_inputs/2017/day-06/input.txt", "r", encoding="utf-8") as f:
    line = f.read()
    CELLS = [int(b) for b in line.split("\t")]

STATES = []

LEN = len(CELLS)

print(CELLS)

res = 0

while (CELLS not in STATES):
    res += 1
    # print(CELLS)
    STATES.append(CELLS.copy())
    cur_cell = CELLS.index(max(CELLS))
    cur_blocks = CELLS[cur_cell]
    CELLS[cur_cell] = 0
    while cur_blocks > 0:
        cur_cell = (cur_cell + 1) % LEN
        CELLS[cur_cell] += 1
        cur_blocks -= 1

print(f"Part 1: {res}")
print(f"Part 2: {res - STATES.index(CELLS)}")
