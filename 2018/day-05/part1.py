def reduce_line(line, rm=None):
    result = ""
    skip = False
    changed = False

    for c0, c1 in zip(line[:-1], line[1:]):
        if rm is not None and (c0.lower() == rm):
            changed = True
            continue
        if skip:
            skip = False
            continue
        if (c0 != c1) and (c0.lower() == c1.lower()):
            skip = True
            changed = True
            continue
        result += c0

    if not skip:
        if rm is None or (rm is not None and (line[-1] != rm)):
            result += line[-1]

    return result, changed


def reduce(line, rm=None):
    changed = True
    while changed:
        line, changed = reduce_line(line, rm)
    return line


if __name__ == "__main__":
    with open("./_inputs/2018/day-05/input.txt", "r", encoding="utf8") as f:
        line = f.read().strip()
        units = [el for el in sorted(set(line)) if el.islower()]

        liner = reduce(line)
        print(f"Part 1: {len(liner)}")

        shortest = len(line)
        for unit in units:
            liner = reduce(line, unit)
            shortest = min(shortest, len(liner))
        print(f"Part 2: {shortest}")
