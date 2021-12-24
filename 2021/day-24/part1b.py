import functools
import time

PROGRAM = []


def set_register(val, reg, registers):
    registers[ord(reg) - ord("w")] = val


def get_register(reg, registers):
    return registers[ord(reg) - ord("w")]

@functools.lru_cache(maxsize=None)
def process(step, z, backwards=True):
    if backwards:
        start = 9
        finish = 0
        delta = -1
    else:
        start = 1
        finish = 10
        delta = 1
    for digit in range(start, finish, delta):
        state = [0, 0, 0, 0]
        set_register(z, "z", state)
        set_register(digit, PROGRAM[step][1], state)
        i = step + 1
        while True:
            if i == len(PROGRAM):
                if get_register("z", state) != 0:
                    return None
                return str(digit)
            com = PROGRAM[i][0]
            arg_0 = PROGRAM[i][1]
            arg_1 = PROGRAM[i][2] \
                if not isinstance(PROGRAM[i][2], str) \
                else get_register(PROGRAM[i][2], state)
            if com == "inp":
                res = process(i, get_register("z", state))
                if res is not None:
                    return str(digit) + res
                break
            if com == "add":
                set_register(get_register(arg_0, state) + arg_1,
                             arg_0,
                             state)
            if com == "mul":
                set_register(get_register(arg_0, state) * arg_1,
                             arg_0,
                             state)
            if com == "div":
                set_register(get_register(arg_0, state) // arg_1,
                             arg_0,
                             state)
            if com == "mod":
                set_register(get_register(arg_0, state) % arg_1,
                             arg_0,
                             state)
            if com == "eql":
                set_register(int(get_register(arg_0, state) == arg_1),
                             arg_0,
                             state)
            i += 1


with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        tmp = line.strip().split()
        if len(tmp) == 2:
            PROGRAM.append((tmp[0], tmp[1], None))
        else:
            PROGRAM.append((tmp[0],
                            tmp[1],
                            tmp[2]
                            if tmp[2] in ["w", "x", "y", "z"]
                            else int(tmp[2])))

t_0 = time.time()
print(f"Part 1: {process(0, 0)}")
print(f"Elapsed in {time.time() - t_0:.2f}")
