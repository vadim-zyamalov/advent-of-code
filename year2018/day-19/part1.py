def proc(
    oper: tuple[int, ...], ip: tuple[int, int], reg_in: tuple[int, ...]
) -> tuple[int, tuple[int, ...]]:
    rp, rv = ip
    cmd, ra, rb, rc = oper

    tmp = list(reg_in)
    tmp[rp] = rv

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
            tmp[rc] = int(
                (tmp[ra] if cmd in ["gtri", "gtrr"] else ra)
                > (tmp[rb] if cmd in ["gtir", "gtrr"] else rb)
            )
        case "eqir" | "eqri" | "eqrr":
            tmp[rc] = int(
                (tmp[ra] if cmd in ["eqri", "eqrr"] else ra)
                == (tmp[rb] if cmd in ["eqir", "eqrr"] else rb)
            )

    rv = tmp[rp]

    return rv + 1, tuple(tmp)


if __name__ == "__main__":
    with open("_inputs/2018/day-19/input.txt", "r", encoding="utf8") as f:
        rp = int(f.readline().strip().split()[1])

        program = []

        for line in f:
            line = line.strip()
            if line == "":
                break
            cmd, r1, r2, r3 = line.split()
            r1, r2, r3 = int(r1), int(r2), int(r3)

            program.append((cmd, r1, r2, r3))

    N = len(program)

    regs = (0, 0, 0, 0, 0, 0)

    ip = 0
    while ip < N:
        ip, regs = proc(program[ip], (rp, ip), regs)

    print(f"Part 1: {regs[0]}")

    # regs = (1, 0, 0, 0, 0, 0)
    #
    # ip = 0
    # print(f"{regs} | {ip}")
    #
    # for _ in range(200):
    #     ip, regs = proc(program[ip], (rp, ip), regs)
    #     print(f"{regs} | {ip}")
