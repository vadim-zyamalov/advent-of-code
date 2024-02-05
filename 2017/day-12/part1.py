def find_group(node, map):
    assert node in map
    group = []
    queue = [node]

    while queue:
        cn = queue.pop()
        for nn in map[cn]:
            if nn not in group:
                group.append(nn)
                queue.append(nn)

    return group


def find_groups(map: dict, init=0):
    total = 0
    nodes = map.keys()

    while nodes:
        gnodes = find_group(init, map)
        nodes = [el for el in nodes if el not in gnodes]
        total += 1
        if nodes:
            init = nodes[0]

    return total


if __name__ == "__main__":
    pipes = {}

    with open("_inputs/2017/day-12/input.txt", "r", encoding="utf8") as f:
        for line in f:
            lhs, rhs = line.strip().split(" <-> ")
            pipes[int(lhs)] = [int(i) for i in rhs.split(",")]

    print(f"Part 1: {len(find_group(0, pipes))}")
    print(f"Part 2: {find_groups(pipes)}")
