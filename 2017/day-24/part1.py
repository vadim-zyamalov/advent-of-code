BRIDGES = []


def next_cs(pin, used, comps):
    res = []
    N = len(comps)
    for i in range(N):
        if i in used:
            continue
        if (comps[i][0] == pin) or (comps[i][1] == pin):
            res.append(i)
    return res


def bridge(pin=0, used=(), comps=[]):
    nx = next_cs(pin, used, comps)
    result = []
    for x in nx:
        nused = used + (x,)
        BRIDGES.append(nused)
        npin = comps[x][0] if comps[x][1] == pin else comps[x][1]
        result.append(comps[x][0] + comps[x][1] + bridge(npin, nused, comps))
    if result != []:
        return max(result)
    return 0


def longest_bridge(pin=0, used=(), comps=[]):
    nx = next_cs(pin, used, comps)
    length = -1
    result = -1
    idx = -1
    for x in nx:
        nused = used + (x,)
        # BRIDGES.append(nused)
        npin = comps[x][0] if comps[x][1] == pin else comps[x][1]
        ll, ss = longest_bridge(npin, nused, comps)
        if length < ll:
            length = ll
            result = ss
            idx = x
        elif length == ll:
            if result <= ss:
                result = ss
                idx = x
    if result > -1:
        return length + 1, comps[idx][0] + comps[idx][1] + result
    return 0, 0


def dump(used, comps):
    result = []
    for el in used:
        result.append("/".join(str(i) for i in comps[el]))
    print("--".join(result))


if __name__ == "__main__":
    components = []
    with open("_inputs/2017/day-24/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            components.append(tuple(int(el) for el in line.split("/")))

    print(f"Part 1: {bridge(0, (), components)}")
    print(f"Part 2: {longest_bridge(0, (), components)}")
    # for el in BRIDGES:
    #    dump(el, components)
