import regex


def regexp(rules, idx=0):
    result = rules[idx].copy()

    while any(v.isdecimal() for v in result):
        i = 0
        while i < len(result):
            instr = result[i]
            if not instr.isdecimal():
                pass
            else:
                newInstr = rules[int(instr)]
                result = result[:i] + ["("] + newInstr + [")"] + result[i + 1 :]
            i += 1

    return ("".join(result)).replace("(a)", "a").replace("(b)", "b")


if __name__ == "__main__":
    with open("_inputs/2020/day-19/input.txt", "r", encoding="utf8") as f:
        parts = f.read().strip().split("\n\n")

    rules = {}
    for line in parts[0].split("\n"):
        idx, rule = line.split(": ")
        rules[int(idx)] = list(rule.replace('"', "").split(" "))

    pat = regexp(rules)
    res = sum(regex.fullmatch(pat, line) is not None for line in parts[1].split("\n"))
    print(f"Part 1: {res}")

    rules[8] = ["42", "+"]
    rules[11] = ["(?<Z>", "42", "(?&Z)*", "31", ")"]
    # _rule = rules[11]
    # for _ in range(5):
    #     _rule = _rule[:1] + _rule + _rule[-1:]
    #     rules[11] = rules[11] + ["|"] + _rule
    pat = regexp(rules)
    res = sum(regex.fullmatch(pat, line) is not None for line in parts[1].split("\n"))
    print(f"Part 2: {res}")
