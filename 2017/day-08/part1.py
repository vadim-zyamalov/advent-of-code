REGISTERS = {}

def check_reg(reg, op, val):
    if reg not in REGISTERS:
        REGISTERS[reg] = 0
    match op:
        case "==":
            return REGISTERS[reg] == val
        case "!=":
            return REGISTERS[reg] != val
        case ">":
            return REGISTERS[reg] > val
        case ">=":
            return REGISTERS[reg] >= val
        case "<":
            return REGISTERS[reg] < val
        case "<=":
            return REGISTERS[reg] <= val


def apply_reg(reg, op, val):
    if reg not in REGISTERS:
        REGISTERS[reg] = 0
    match op:
        case "inc":
            REGISTERS[reg] += val
        case "dec":
            REGISTERS[reg] -= val

max_val = 0

with open("../../_inputs/2017/day-08/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        tmp = line.strip().split()
        tmp[2] = int(tmp[2])
        tmp[6] = int(tmp[6])
        if check_reg(tmp[4], tmp[5], tmp[6]):
            apply_reg(tmp[0], tmp[1], tmp[2])
        max_val = max(max_val, max(REGISTERS.values()))

print(f"Part 1: {max(REGISTERS.values())}")
print(f"Part 2: {max_val}")
