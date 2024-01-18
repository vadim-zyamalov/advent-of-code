def init_tree(commands):
    res = {}
    path = []
    cur_dir = ""
    for com in commands:
        lcom = com.split()
        if lcom[0] == "$":
            if lcom[1] == "cd":
                if lcom[2] == "..":
                    path = path[:-1]
                    cur_dir = "/".join(path)
                else:
                    if lcom[2] == "/":
                        cur_dir = "/"
                    else:
                        path.append(lcom[2])
                        cur_dir = "/" + "/".join(path)
                    if cur_dir not in res:
                        res[cur_dir] = {"files": {}, "dirs": set()}
        else:
            if lcom[0] == "dir":
                res[cur_dir]["dirs"].add(lcom[1])
            else:
                res[cur_dir]["files"][lcom[1]] = int(lcom[0])
    return res


def restore_tree(node, raw_tree):
    res = {node: {"files": raw_tree[node]["files"], "dirs": {}}}
    for d in raw_tree[node]["dirs"]:
        if node == "/":
            new_node = "/" + d
        else:
            new_node = node + "/" + d
        res[node]["dirs"].update(restore_tree(new_node, raw_tree))
    return res


def count(tree, res_min: list[int], res_all: list[int], limit=100000):
    res = 0
    for v in tree["files"].values():
        res += v
    for d in tree["dirs"]:
        res += count(tree["dirs"][d], res_min, res_all)
    if res <= limit:
        res_min.append(res)
    res_all.append(res)
    return res


COMMS = []
limit = 30000000
with open("../../_inputs/2022/day-07/input.txt", "r", encoding="utf8") as f:
    for line in f:
        COMMS.append(line.strip())

res = []
res2 = []

total_size = count(restore_tree("/", init_tree(COMMS))["/"], res, res2)
print(f"Part 1: {sum(res)}")
print(f"Part 2: {min([i for i in res2 if i >= (limit - (70000000 - total_size))])}")
