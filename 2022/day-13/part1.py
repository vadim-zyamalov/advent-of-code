import functools

def parse(chunk):
    if chunk[0] != '[':
        return int(chunk)
    nestlv = 0
    res = []
    tmp = ''
    for c in chunk[1:-1]:
        match c:
            case '[':
                tmp += c
                nestlv += 1
            case ']':
                tmp += c
                nestlv -= 1
            case ',' if nestlv == 0:
                res.append(parse(tmp))
                tmp = ''
            case _:
                tmp += c
    if tmp != "":
        res.append(parse(tmp))
    return res


def check(l, r):
    if (type(l) is int) and (type(r) is int):
        if l < r:
            return -1
        elif l > r:
            return 1
        else:
            return 0

    if type(l) is int:
        l = [l]
    if type(r) is int:
        r = [r]

    if l == [] and r != []:
        return -1
    if l != [] and r == []:
        return 1
    if l == [] and r == []:
        return 0

    res = check(l[0], r[0])
    if res:
        return res
    else:
        return check(l[1:], r[1:])


packets = []

with open("../../_inputs/2022/day-13/input.txt", "r", encoding="utf8") as f:
    res = 0
    num = 0
    for line1, line2 in zip(f, f):
        num += 1
        left = parse(line1.strip())
        right = parse(line2.strip())
        packets.append(left)
        packets.append(right)

        if check(left, right) < 0:
            res += num
        f.readline()

print(f"Part 1: {res}")

packets.append([[2]])
packets.append([[6]])
packets.sort(key=functools.cmp_to_key(check))

print(f"Part 2: {(1 + packets.index([[2]])) * (1 + packets.index([[6]]))}")
