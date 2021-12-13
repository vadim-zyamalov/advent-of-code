dots = []
folds = []

# 0 1 2 3 | 5 6 7
def dump(dots):
    max_x = 0
    max_y = 0
    for dot in dots:
        max_x = max(max_x, dot[0])
        max_y = max(max_y, dot[1])
    result = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for dot in dots:
        result[dot[1]][dot[0]] = '#'
    for row in result:
        for el in row:
            print(el, end='')
        print()
    print()


def fold(rule, dots):
    new_dots = []
    for dot in dots:
        if rule[0] > 0:
            delta = (dot[0] - rule[0], 0)
        else:
            delta = (0, dot[1] - rule[1])
        if delta == (0, 0):
            continue
        if (delta[0] > 0) or (delta[1] > 0):
            new_dots.append((dot[0] - 2 * delta[0],
                             dot[1] - 2 * delta[1]))
        else:
            new_dots.append(dot)
    return list(set(new_dots))


with open("input.txt", "r") as f:
    for line in f:
        if line.strip() == '':
            continue
        tmp = line.strip().split(',')
        if len(tmp) > 1:
            dots.append((int(tmp[0]), int(tmp[1])))
        else:
            tmp = line.strip().split('=')
            folds.append((int(tmp[1]) if tmp[0].endswith('x') else 0,
                          int(tmp[1]) if tmp[0].endswith('y') else 0))

res = fold(folds[0], dots)
print("Part 1: {}".format(len(res)))

res = dots.copy()
for f in folds:
    res = fold(f, res)
print("Part 2:")
dump(res)
