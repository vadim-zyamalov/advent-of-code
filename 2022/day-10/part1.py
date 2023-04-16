def check(cycle, reg, storage):
    if (cycle == 20) or ((cycle - 20) % 40 == 0):
        storage.append(cycle * reg)


def draw(cycle, reg, screen):
    rpos = (cycle - 1) % 40
    if ((reg - 1 == rpos) or (reg == rpos) or (reg + 1 == rpos)) and \
       (cycle < 240):
        screen[cycle - 1] = "#"


def show(screen):
    for i in range(len(screen)):
        print(screen[i], end="")
        if (i + 1) % 40 == 0:
            print()


REG = 1
cycle = 0

sig_strength = []
CRT = ["."] * 240

with open("../../_inputs/2022/day-10/input.txt", "r", encoding="utf8") as f:
    while line := f.readline():
        tmp = line.strip().split()
        match tmp[0]:
            case "noop":
                cycle += 1
                check(cycle, REG, sig_strength)
                draw(cycle, REG, CRT)
            case "addx":
                cycle += 2
                check(cycle - 1, REG, sig_strength)
                draw(cycle - 1, REG, CRT)
                check(cycle, REG, sig_strength)
                draw(cycle, REG, CRT)
                REG += int(tmp[1])

print(f"Part 1: {sum(sig_strength)}")
print("Part 2:")
show(CRT)
