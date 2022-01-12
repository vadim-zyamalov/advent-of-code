def process():
    i = 0
    while i < len(COMMANDS):
        cur_command = COMMANDS[i]
        if cur_command[0] == "cpy":
            if cur_command[2] in REGISTERS:
                REGISTERS[cur_command[2]] = int(cur_command[1]) \
                    if cur_command[1] not in REGISTERS \
                       else REGISTERS[cur_command[1]]
            i += 1
        elif cur_command[0] == "inc":
            if cur_command[1] in REGISTERS:
                REGISTERS[cur_command[1]] += 1
            i += 1
        elif cur_command[0] == "dec":
            if cur_command[1] in REGISTERS:
                REGISTERS[cur_command[1]] -= 1
            i += 1
        elif cur_command[0] == "jnz":
            tmp_test = int(cur_command[1]) \
                if cur_command[1] not in REGISTERS \
                   else REGISTERS[cur_command[1]]
            if tmp_test != 0:
                i += int(cur_command[2]) \
                    if cur_command[2] not in REGISTERS \
                       else REGISTERS[cur_command[2]]
            else:
                i += 1
        elif cur_command[0] == "tgl":
            tgl_shift = int(cur_command[1]) \
                if cur_command[1] not in REGISTERS else \
                   REGISTERS[cur_command[1]]
            tgl_i = i + tgl_shift
            if (tgl_i >= len(COMMANDS)) or \
               (tgl_i < 0):
                pass
            else:
                if len(COMMANDS[tgl_i]) == 2:
                    if COMMANDS[tgl_i][0] == "inc":
                        COMMANDS[tgl_i] = ("dec", COMMANDS[tgl_i][1])
                    else:
                        COMMANDS[tgl_i] = ("inc", COMMANDS[tgl_i][1])
                else:
                    if COMMANDS[tgl_i][0] == "jnz":
                        COMMANDS[tgl_i] = ("cpy",) + COMMANDS[tgl_i][1:]
                    else:
                        COMMANDS[tgl_i] = ("jnz",) + COMMANDS[tgl_i][1:]
            i += 1


COMMANDS = []
REGISTERS = {'a': 7,
             'b': 0,
             'c': 0,
             'd': 0}

with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        tmp = line.strip().split()
        COMMANDS.append(tuple(tmp))

process()

print(f"Part 1: {REGISTERS['a']}")

COMMANDS = []
REGISTERS = {'a': 12,
             'b': 0,
             'c': 0,
             'd': 0}

with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        tmp = line.strip().split()
        COMMANDS.append(tuple(tmp))

process()

print(f"Part 2: {REGISTERS['a']}")
