def value(tree):
    children, meta = tree

    if children == []:
        return sum(meta)

    child_num = len(children)
    result = 0

    for i in meta:
        if i <= child_num:
            result += value(children[i - 1])

    return result


def tree(data, beg=0):
    i = beg

    child_num = data[i]
    meta_num = data[i + 1]
    i += 2

    children = []
    meta_sum = 0
    for _ in range(child_num):
        i, child_tree, child_sum = tree(data, i)
        children.append(child_tree)
        meta_sum += child_sum
    meta = []
    for _ in range(meta_num):
        meta.append(data[i])
        i += 1

    return i, (children, meta), sum(meta) + meta_sum


if __name__ == "__main__":
    with open("./_inputs/2018/day-08/input.txt", "r", encoding="utf8") as f:
        data = [int(i) for i in f.read().strip().split()]

        i, data_tree, meta_sum = tree(data)

        print(f"Part 1: {meta_sum}")
        print(f"Part 2: {value(data_tree)}")
