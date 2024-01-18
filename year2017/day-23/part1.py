REGISTERS = {}
KEYS = list("abcdefgh")

for i in KEYS:
    REGISTERS[i] = 0
REGISTERS["a"] = 1


def clear_registers():
    for rs in REGISTERS:
        for k in rs:
            rs[k] = 0


def val(x):
    return REGISTERS[x] if x in KEYS else x


def proc_command1(command: tuple, i: int) -> tuple[int, int]:
    output = 0
    match command[0]:
        case "set":
            REGISTERS[command[1]] = val(command[2])
        case "add":
            REGISTERS[command[1]] += val(command[2])
        case "sub":
            REGISTERS[command[1]] -= val(command[2])
        case "mul":
            REGISTERS[command[1]] *= val(command[2])
            output = 1
        case "mod":
            REGISTERS[command[1]] %= val(command[2])
        case "jgz":
            if val(command[1]) > 0:
                return i + val(command[2]), output
        case "jnz":
            if val(command[1]) != 0:
                return i + val(command[2]), output
    return i + 1, output


def part1(prog):
    i = 0
    N = len(prog)
    total = 0
    while -1 < i < N:
        i, out = proc_command1(prog[i], i)
        total += out
    print(f"Part 1: {total}")


if __name__ == "__main__":
    with open("../../_inputs/2017/day-23/sample.txt", "r", encoding="utf8") as f:
        PROG = []
        for line in f:
            ltokens = line.strip().split()
            tmp: list[int | str] = [ltokens[0]]
            for i in range(1, len(ltokens)):
                tmp.append(ltokens[i] if ltokens[i] in KEYS else int(ltokens[i]))
            PROG.append(tuple(tmp))

    part1(PROG)
    print(REGISTERS)
