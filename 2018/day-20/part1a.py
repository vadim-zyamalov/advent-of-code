from collections import defaultdict, deque

DIRS = {"N": -1, "S": 1, "W": -1j, "E": 1j}


def go(line):
    dist = defaultdict(int)
    stack = deque()

    pos = {0}
    svd = set()

    for c in line:
        match c:
            case "N" | "S" | "W" | "E":
                nxt = set()
                for p in pos:
                    nxt_p = p + DIRS[c]
                    if dist[nxt_p] != 0:
                        dist[nxt_p] = min(dist[nxt_p], dist[p] + 1)
                    else:
                        dist[nxt_p] = dist[p] + 1
                    nxt.add(nxt_p)
                pos = nxt
            case "(":
                stack.append((pos, svd))
                svd = set()
            case "|":
                svd.update(pos)
                pos, _ = stack[-1]
            case ")":
                svd.update(pos)
                _, svdsvd = stack.pop()
                pos, svd = svd, svdsvd

    return dist


if __name__ == "__main__":
    with open("_inputs/2018/day-20/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("$")
        if lines[-1] == "":
            del lines[-1]
        for i, v in enumerate(lines):
            lines[i] = v[1:]

    dists = go(lines[0])
    print(f"Part 1: {max(dists.values())}")
    print(f"Part 2: {sum(d >= 1000 for d in dists.values())}")
