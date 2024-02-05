if __name__ == "__main__":
    with open("_inputs/2017/day-25/input.txt", "r", encoding="utf8") as f:
        lines = f.readlines()

    state = ""
    stop = -1

    states = {}
    tape = {0: 0}

    i = 0
    while i < len(lines):
        line = lines[i].strip(":. \n")
        if line == "":
            pass
        if line.startswith("Begin"):
            state = line.split()[-1]
        elif line.startswith("Perform"):
            stop = int(line.split()[-2])
        elif line.startswith("In state"):
            cur_state = line.split()[-1]
            cur_p1 = int(lines[i + 1].strip(":. \n").split()[-1])
            cur_rule1 = (
                int(lines[i + 2].strip(":. \n").split()[-1]),
                1 if lines[i + 3].strip(":. \n").split()[-1] == "right" else -1,
                lines[i + 4].strip(":. \n").split()[-1],
            )
            cur_p2 = int(lines[i + 5].strip(":. \n").split()[-1])
            cur_rule2 = (
                int(lines[i + 6].strip(":. \n").split()[-1]),
                1 if lines[i + 7].strip(":. \n").split()[-1] == "right" else -1,
                lines[i + 8].strip(":. \n").split()[-1],
            )
            states[cur_state] = {cur_p1: cur_rule1, cur_p2: cur_rule2}
            i += 8
        i += 1

    i = 0
    for _ in range(stop):
        if i not in tape:
            tape[i] = 0
        nv, mv, ns = states[state][tape[i]]
        tape[i] = nv
        i += mv
        state = ns

    print(f"Part 1: {sum(v for v in tape.values())}")
