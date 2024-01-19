import time

CMDS = [
    "addr",
    "addi",
    "mulr",
    "muli",
    "banr",
    "bani",
    "borr",
    "bori",
    "setr",
    "seti",
    "gtir",
    "gtri",
    "gtrr",
    "eqir",
    "eqri",
    "eqrr",
]


def proc(
    cmd: str, oper: tuple[int, ...], reg_in: tuple[int, ...]
) -> tuple[int, ...]:
    _, ra, rb, rc = oper
    tmp = list(reg_in)
    match cmd:
        case "addr" | "addi":
            tmp[rc] = tmp[ra] + (tmp[rb] if cmd == "addr" else rb)
        case "mulr" | "muli":
            tmp[rc] = tmp[ra] * (tmp[rb] if cmd == "mulr" else rb)
        case "banr" | "bani":
            tmp[rc] = tmp[ra] & (tmp[rb] if cmd == "banr" else rb)
        case "borr" | "bori":
            tmp[rc] = tmp[ra] | (tmp[rb] if cmd == "borr" else rb)
        case "setr" | "seti":
            tmp[rc] = tmp[ra] if cmd == "setr" else ra
        case "gtir" | "gtri" | "gtrr":
            tmp[rc] = (tmp[ra] if cmd in ["gtri", "gtrr"] else ra) > (
                tmp[rb] if cmd in ["gtir", "gtrr"] else rb
            )
        case "eqir" | "eqri" | "eqrr":
            tmp[rc] = (tmp[ra] if cmd in ["eqri", "eqrr"] else ra) == (
                tmp[rb] if cmd in ["eqir", "eqrr"] else rb
            )
    return tuple(tmp)


def execute(
    opcs: dict[int, str], program: list[tuple[int, ...]]
) -> tuple[int, ...]:
    regs = (0, 0, 0, 0)

    for oper in program:
        cmd = opcs[oper[0]]
        regs = proc(cmd, oper, regs)

    return regs


def chk_command(
    oper: tuple[int, ...], reg_in: tuple[int, ...], reg_out: tuple[int, ...]
) -> tuple[int, list[str]]:
    result = 0
    rescmd = []
    for cmd in CMDS:
        if proc(cmd, oper, reg_in) == reg_out:
            result += 1
            rescmd.append(cmd)
    return result, rescmd


def decipher(patterns: list[tuple[tuple[int, ...], ...]]) -> dict[int, str]:
    result = {k: set() for k in range(16)}

    for oper, reg_in, reg_out in patterns:
        opc = oper[0]
        _, cmd = chk_command(oper, reg_in, reg_out)
        if len(result[opc]) == 0:
            result[opc] = set(cmd)
        else:
            result[opc] &= set(cmd)

    while not all(len(v) == 1 for v in result.values()):
        for k, v in result.items():
            if len(v) == 1:
                for k2 in result:
                    if k == k2:
                        continue
                    result[k2] -= result[k]

    return {k: list(v)[0] for k, v in result.items()}


if __name__ == "__main__":
    with open("_inputs/2018/day-16/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip("\n")
        data1, data2 = lines.split("\n\n\n\n")

    data1 = data1.split("\n\n")
    patterns = []
    for el in data1:
        reg_in, oper, reg_out = el.split("\n")

        reg_in = tuple(
            int(i) for i in reg_in.split(": ")[1].strip(" []").split(",")
        )
        oper = tuple(int(i) for i in oper.split())
        reg_out = tuple(
            int(i) for i in reg_out.split(": ")[1].strip(" []").split(",")
        )
        patterns.append((oper, reg_in, reg_out))

    data2 = data2.split("\n")
    program = []
    for el in data2:
        program.append(tuple(int(i) for i in el.split()))

    t0 = time.time()
    result = 0
    for oper, reg_in, reg_out in patterns:
        result += chk_command(oper, reg_in, reg_out)[0] >= 3
    print(f"Part 1: {result}")
    print(f"    took {time.time() - t0:.2f} secs")

    t0 = time.time()
    opcs = decipher(patterns)
    print(f"Part 2: {execute(opcs, program)[0]}")
    print(f"    took {time.time() - t0:.2f} secs")
