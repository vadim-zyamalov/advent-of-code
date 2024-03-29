COMMANDS = []
REGISTERS = {"a": 0, "b": 0, "c": 0, "d": 0}


def process():
    i = 0
    while i < len(COMMANDS):
        cur_command = COMMANDS[i]
        match cur_command[0]:
            case "cpy":
                if isinstance(cur_command[1], int):
                    REGISTERS[cur_command[2]] = cur_command[1]
                else:
                    REGISTERS[cur_command[2]] = REGISTERS[cur_command[1]]
                i += 1
            case "inc":
                REGISTERS[cur_command[1]] += 1
                i += 1
            case "dec":
                REGISTERS[cur_command[1]] -= 1
                i += 1
            case "jnz":
                if isinstance(cur_command[1], int):
                    if cur_command[1] != 0:
                        i += cur_command[2]
                    else:
                        i += 1
                else:
                    if REGISTERS[cur_command[1]] != 0:
                        i += cur_command[2]
                    else:
                        i += 1


with open("_inputs/2016/day-12/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        tmp = line.strip().split()
        if (tmp[0] == "cpy") and (tmp[1] not in REGISTERS):
            COMMANDS.append((tmp[0], int(tmp[1]), tmp[2]))
        elif tmp[0] == "jnz":
            if tmp[1] not in REGISTERS:
                COMMANDS.append((tmp[0], int(tmp[1]), int(tmp[2])))
            else:
                COMMANDS.append((tmp[0], tmp[1], int(tmp[2])))
        else:
            COMMANDS.append(tuple(tmp))

process()

print(f"Part 1: {REGISTERS['a']}")

REGISTERS = {"a": 0, "b": 0, "c": 1, "d": 0}

process()

print(f"Part 2: {REGISTERS['a']}")
