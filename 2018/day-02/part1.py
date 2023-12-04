def lcount(line: str) -> dict:
    return {l: line.count(l) for l in set(line)}


def check_ids(id1: str, id2: str) -> bool:
    res = sum(1 for el1, el2 in zip(id1, id2) if el1 != el2)
    return res == 1


if __name__ == "__main__":
    ids = []
    rest = ""
    res2 = 0
    res3 = 0
    with open("_inputs/2018/day-02/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break

            if rest == "":
                for id0 in ids:
                    if check_ids(line, id0):
                        rest = "".join(
                            [el1 for el1, el2 in zip(line, id0) if el1 == el2]
                        )

            ids.append(line)
            lnum = lcount(line)
            if any(v == 2 for v in lnum.values()):
                res2 += 1
            if any(v == 3 for v in lnum.values()):
                res3 += 1

    print(f"Part 1: {res2 * res3}")
    print(f"Part 2: {rest}")
