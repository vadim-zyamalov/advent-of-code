def search_loop(prog, repl=None):
    acc = 0

    ip = 0
    visited = set()

    while ip not in visited and ip < len(prog):
        visited.add(ip)
        op, par = prog[ip]
        if repl is not None and ip == repl:
            op = "nop" if op == "jmp" else "jmp"
        match op:
            case "nop":
                pass
                ip += 1
            case "acc":
                acc = acc + par
                ip += 1
            case "jmp":
                ip += par

    return acc, ip >= len(prog)


def correct_prog(prog):
    cands = [i for i, (op, _) in enumerate(prog) if op != "acc"]

    for idx in cands:
        res, status = search_loop(prog, idx)
        if status:
            return res

    return None


if __name__ == "__main__":
    with open("_inputs/2020/day-08/input.txt", "r", encoding="utf8") as f:
        prog = [
            (line.split()[0], int(line.split()[1]))
            for line in f.read().strip().split("\n")
        ]

    print(f"Part 1: {search_loop(prog)[0]}")
    print(f"Part 2: {correct_prog(prog)}")
