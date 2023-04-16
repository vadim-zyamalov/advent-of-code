elves = []

with open("../../_inputs/2022/day-01/input.txt", "r", encoding="utf8") as f:
    cur_elf = []
    for line in f:
        if line.strip() == "":
            elves.append(cur_elf)
            cur_elf= []
        else:
            cur_elf.append(int(line.strip()))

totals = [sum(l) for l in elves]
totals.sort(reverse=True)
print(f"Part 1: {totals[0]}")
print(f"Part 2: {sum(totals[0:3])}")
