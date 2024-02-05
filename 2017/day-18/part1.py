REGISTERS = ({}, {})
KEYS = []
for ch in range(ord("a"), ord("z") + 1):
    REGISTERS[0][chr(ch)] = 0
    REGISTERS[1][chr(ch)] = 0
    KEYS.append(chr(ch))

SOUNDS = []
QUEUES = ([], [])


def clear_registers():
    for rs in REGISTERS:
        for k in rs:
            rs[k] = 0


def val(x, idx=0):
    return REGISTERS[idx][x] if x in KEYS else x


def proc_command1(command: tuple, i: int, idx=0) -> tuple[int, int | None]:
    output = None
    match command[0]:
        case "snd":
            SOUNDS.append(val(command[1], idx))
        case "set":
            REGISTERS[idx][command[1]] = val(command[2], idx)
        case "add":
            REGISTERS[idx][command[1]] += val(command[2], idx)
        case "mul":
            REGISTERS[idx][command[1]] *= val(command[2], idx)
        case "mod":
            REGISTERS[idx][command[1]] %= val(command[2], idx)
        case "rcv":
            if (val(command[1], idx) != 0) and (SOUNDS != []):
                return i + 1, SOUNDS[-1]
        case "jgz":
            if val(command[1], idx) > 0:
                return i + val(command[2], idx), output
        case "snd":
            QUEUES[1 - idx].append(val(command[1], idx))
        case "rcv":
            if len(QUEUES[idx]) == 0:
                return i, None
            else:
                REGISTERS[idx][command[1]] = QUEUES[idx].pop(0)
    return i + 1, None


def proc_command2(command: tuple, i: int, idx=0) -> tuple[int, int]:
    match command[0]:
        case "set":
            REGISTERS[idx][command[1]] = val(command[2], idx)
        case "add":
            REGISTERS[idx][command[1]] += val(command[2], idx)
        case "mul":
            REGISTERS[idx][command[1]] *= val(command[2], idx)
        case "mod":
            REGISTERS[idx][command[1]] %= val(command[2], idx)
        case "jgz":
            if val(command[1], idx) > 0:
                return i + val(command[2], idx), 0
        case "snd":
            QUEUES[1 - idx].append(val(command[1], idx))
            return i + 1, 1
        case "rcv":
            if len(QUEUES[idx]) == 0:
                return i, 0
            else:
                REGISTERS[idx][command[1]] = QUEUES[idx].pop(0)
    return i + 1, 0


def part1(prog):
    i = 0
    N = len(prog)
    while -1 < i < N:
        i, out = proc_command1(prog[i], i)
        if out is not None:
            print(f"Part 1: {out}")
            break


def part2(prog):
    i, j = 0, 0
    N = len(prog)

    total = 0

    while True:
        out = 0
        ni, nj = i, j

        if -1 < i < N:
            ni, _ = proc_command2(prog[i], i, 0)

        if -1 < j < N:
            nj, out = proc_command2(prog[j], j, 1)

        if (ni == i) and (nj == j):  # deadlock
            print(f"Part 2: {total}")
            break

        total += out
        i, j = ni, nj


if __name__ == "__main__":
    with open("_inputs/2017/day-18/input.txt", "r", encoding="utf8") as f:
        PROG = []
        for line in f:
            ltokens = line.strip().split()
            tmp: list[int | str] = [ltokens[0]]
            for i in range(1, len(ltokens)):
                tmp.append(ltokens[i] if ltokens[i] in KEYS else int(ltokens[i]))
            PROG.append(tuple(tmp))

    part1(PROG)
    clear_registers()
    REGISTERS[0]["p"] = 0
    REGISTERS[1]["p"] = 1
    part2(PROG)
