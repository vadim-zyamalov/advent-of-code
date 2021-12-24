import time

REGISTERS = {"w": 0,
             "x": 0,
             "y": 0,
             "z": 0}

PROGRAM = []


def reset_registers():
    for key in REGISTERS:
        REGISTERS[key] = 0


def process_input(data, sequentially=False):
    if isinstance(data, str):
        if not sequentially:
            yield int(data)
        else:
            for letter in data:
                yield int(letter)
    else:
        if not sequentially:
            yield data
        else:
            for letter in str(data):
                yield int(letter)


def process(data, program, sequentially=False):
    reset_registers()
    data_gen = process_input(data, sequentially)
    for command in program:
        com = command[0]
        arg_0 = command[1]
        arg_1 = command[2] \
            if not command[2] or isinstance(command[2], int) \
            else REGISTERS[command[2]]
        if com == "inp":
            REGISTERS[arg_0] = next(data_gen)
        elif com == "add":
            REGISTERS[arg_0] += arg_1
        elif com == "mul":
            REGISTERS[arg_0] *= arg_1
        elif com == "div":
            REGISTERS[arg_0] //= arg_1
            if REGISTERS[arg_0] < 0:
                REGISTERS[arg_0] += 1
        elif com == "mod":
            REGISTERS[arg_0] %= arg_1
        elif com == "eql":
            REGISTERS[arg_0] = 1 if REGISTERS[arg_0] == arg_1 else 0


with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        tmp = line.strip().split()
        if len(tmp) == 2:
            PROGRAM.append((tmp[0], tmp[1], None))
        else:
            if tmp[-1].replace("-", "").isnumeric():
                PROGRAM.append((tmp[0], tmp[1], int(tmp[2])))
            else:
                PROGRAM.append((tmp[0], tmp[1], tmp[2]))

t_0 = time.time()
START = int('9' * 14)
FINISH = int('1' * 14)
for i in range(START, FINISH - 1, -1):
    if i % 10000 == 1:
        print(i, end='\r')
    if '0' in str(i):
        continue
    process(i, PROGRAM, True)
    if REGISTERS["z"] == 0:
        print()
        print(f"Part 1: {i}")
        print(f"Elapsed in {time.time() - t_0:.2f} seconds")
        break
