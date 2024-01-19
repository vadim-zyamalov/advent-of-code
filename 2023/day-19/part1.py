def parse_wf(line: str) -> tuple[str, list[tuple]]:
    result = []

    name, wfs = line.split("{")

    wfs = wfs.strip("{}").split(",")
    for ws in wfs:
        if ":" in ws:
            cond, dest = ws.split(":")
            if "<" in cond:
                ch, val = cond.split("<")
                result.append((ch, "<", int(val), dest))
            elif ">" in cond:
                ch, val = cond.split(">")
                result.append((ch, ">", int(val), dest))
        else:
            result.append((ws,))

    return name, result


def parse_part(line: str) -> dict[str, int]:
    result = {}

    line = line.strip("{}")
    for el in line.split(","):
        ch, val = el.split("=")
        result[ch] = int(val)

    return result


def process(part: dict[str, int], wfs: dict[str, list]) -> int:
    cur_wf = "in"

    while True:
        for action in wfs[cur_wf]:
            if len(action) > 1:
                ch, act, val, dest = action
                if ((act == ">") and (part[ch] > val)) or (
                    (act == "<") and (part[ch] < val)
                ):
                    cur_wf = dest
                    break
            else:
                cur_wf = action[0]
        if cur_wf == "R":
            return 0
        if cur_wf == "A":
            return sum(part.values())


def prod(bounds):
    result = 1

    for lb, ub in bounds.values():
        result *= ub - lb + 1

    return result


def process_all(cur_wf, wfs, bounds):
    result = 0
    _bounds = bounds.copy()

    if cur_wf == "R":
        return 0
    if cur_wf == "A":
        return prod(_bounds)

    for action in wfs[cur_wf]:
        __bounds = _bounds.copy()
        if len(action) > 1:
            ch, act, val, dest = action
            match act:
                case "<":
                    if _bounds[ch] is not None and (val > _bounds[ch][0]):
                        __bounds[ch] = (_bounds[ch][0], min(val - 1, _bounds[ch][1]))
                        result += process_all(dest, wfs, __bounds)
                        if val <= _bounds[ch][1]:
                            _bounds[ch] = (val, _bounds[ch][1])
                        else:
                            _bounds[ch] = None
                case ">":
                    if _bounds[ch] is not None and (val < _bounds[ch][1]):
                        __bounds[ch] = (max(val + 1, _bounds[ch][0]), _bounds[ch][1])
                        result += process_all(dest, wfs, __bounds)
                        if _bounds[ch][0] <= val:
                            _bounds[ch] = (_bounds[ch][0], val)
                        else:
                            _bounds[ch] = None
        else:
            result += process_all(action[0], wfs, _bounds)

    return result


if __name__ == "__main__":
    with open("_inputs/2023/day-19/input.txt") as f:
        wfs = {}
        parts = []
        contents = f.read()
        _wfs, _parts = contents.strip().split("\n\n")

        for wf in _wfs.split("\n"):
            name, conds = parse_wf(wf)
            wfs[name] = conds

        res1 = 0
        for part in _parts.split("\n"):
            part = parse_part(part)
            parts.append(part)
            res1 += process(part, wfs)

        print(f"Part 1: {res1}")

        res2 = process_all(
            "in", wfs, {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
        )

        print(f"Part 2: {res2}")
