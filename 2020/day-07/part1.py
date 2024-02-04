from collections import defaultdict


def search_outers(outer, beg="shiny gold"):
    stack = [beg]
    res = set()

    while stack:
        cur = stack.pop()
        if cur not in outer:
            continue
        res |= set(outer[cur])
        stack.extend(outer[cur])

    return len(res)


def count_inners(inner, beg="shiny gold"):
    queue = [(beg, 1)]
    res = -1

    while queue:
        cur, num = queue.pop(0)
        res += num
        if cur in inner:
            for nxt, nnum in inner[cur]:
                queue.append((nxt, num * nnum))

    return res


if __name__ == "__main__":
    outer = defaultdict(list)
    inner = defaultdict(list)

    with open("_inputs/2020/day-07/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n")

    for line in lines:
        ob, _, ibs = line.partition(" contain ")
        ob = " ".join(ob.split()[:-1])
        for ib in ibs.split(", "):
            els = ib.split()
            if els[0] != "no":
                num, name = int(els[0]), " ".join(els[1:-1])
                inner[ob].append((name, num))
                outer[name].append(ob)

    print(f"Part 1: {search_outers(outer)}")
    print(f"Part 1: {count_inners(inner)}")
