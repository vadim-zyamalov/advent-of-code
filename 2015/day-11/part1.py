def inc(line):
    result = list(line)
    position = len(result) - 1
    while True:
        if result[position] != 'z':
            result[position] = chr(ord(result[position]) + 1)
            break
        else:
            result[position] = 'a'
            position -= 1
        if position < 0:
            break
    return ''.join(result)


def check1(line):
    variants = [(ord(a), ord(b), ord(c))
                for a, b, c in zip(line[:-2], line[1:-1], line[2:])]
    for i in variants:
        if (i[1] - i[0] == 1) and \
           (i[2] - i[1] == 1):
            return True
    return False


def check2(line):
    for i in line:
        if i in "iol":
            return False
    return True


def check3(line):
    variants = [a == b for a, b in zip(line[:-1], line[1:])]
    for i in range(len(variants) - 2):
        if variants[i] and any(variants[(i + 2):]):
            return True
    return False


for part in [1, 2]:
    with open("input{}.txt".format(part), "r", encoding="utf-8") as f:
        line = f.readline()
        line = line.strip()

    line = inc(line)
    while not (check1(line) and check2(line) and check3(line)):
        line = inc(line)
    print(f"Part {part}: {line}")
