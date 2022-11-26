def restore_tree(node, progs_d):
    res = []
    tmp_weight = progs_d[node]["weight"]
    node_weight = tmp_weight
    tmp_sub = []
    for k in progs_d[node]["upper"]:
        tmp_sub.append(restore_tree(k, progs_d))
    if tmp_sub:
        for i in tmp_sub:
            tmp_weight += i[2]
    res.append(node)
    res.append(node_weight)
    res.append(tmp_weight)
    res.append(tmp_sub)
    return(res)


def search_wrong(tree, diff):
    weights = []
    for k in tree[3]:
        weights.append(k[2])
    tmp_weights = weights.copy()
    weights.sort()
    if weights[0] != weights[len(weights) - 1]:
        if weights[0] != weights[len(weights) // 2]:
            wrong_weight = weights[0]
        else:
            wrong_weight = weights[len(weights) - 1]
        cur_diff = wrong_weight - weights[len(weights) // 2]
        cur_index = tmp_weights.index(wrong_weight)
        return(search_wrong(tree[3][cur_index], cur_diff))
    else:
        return(tree[1] - diff)


PROGS = {}

with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        tmp = line.strip().split()
        tmp[1] = tmp[1].strip("()")
        tmp_l = []
        if len(tmp) > 2:
            for i in range(3, len(tmp)):
                tmp_l.append(tmp[i].strip(","))
        PROGS[tmp[0]] = {
            "weight": int(tmp[1]),
            "upper": tmp_l
        }


ROOT = ""

for k in PROGS.keys():
    found = False
    for kk in PROGS.keys():
        if k in PROGS[kk]["upper"]:
            found = True
            break
    if not found:
        print(f"Part 1: {k}")
        ROOT = k
        break

print(f"Part 2: {search_wrong(restore_tree(ROOT, PROGS), 0)}")
