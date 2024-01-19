TOP = 50_000_000_000


def step(state, beg, patterns):
    result = ""
    N = len(state)
    for i in range(N - 4):
        if state[i : i + 5] not in patterns:
            result += "."
        else:
            result += patterns[state[i : i + 5]]
    if result.startswith("...."):
        beg += 2
    elif result.startswith("..."):
        result = "." + result
        beg += 1
    elif result.startswith(".."):
        result = ".." + result
    elif result.startswith("."):
        result = "..." + result
        beg -= 1
    else:
        beg -= 2
    if result.endswith("...."):
        pass
    elif result.endswith("..."):
        result += "."
    elif result.endswith(".."):
        result += ".."
    elif result.endswith("."):
        result += "..."
    return result, beg


def score(state, beg):
    result = 0
    N = len(state)

    for i in range(N):
        if state[i] == "#":
            result += i + beg

    return result


def dump(state, beg):
    print("." * (6 + beg), end="")
    print(state)


if __name__ == "__main__":
    with open("./_inputs/2018/day-12/input.txt", "r", encoding="utf8") as f:
        patterns = {}
        state = f.readline().strip().split(":")[1].strip()
        f.readline()
        for line in f:
            line = line.strip()
            if line == "":
                break
            pattern, res = line.split(" => ")
            patterns[pattern] = res

        state = "...." + state + "...."
        beg = -4
        i = 0

        while True:
            _state, _beg = step(state, beg, patterns)
            if state == _state:
                break
            state = _state
            beg = _beg
            i += 1
            if i == 20:
                print(f"Part 1: {score(state, beg)}")

        beg = beg + (TOP - i)
        print(f"Part 2: {score(state, beg)}")
