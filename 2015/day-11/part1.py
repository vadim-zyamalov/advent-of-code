def inc(line):
    res = list(line)
    pos = len(res) - 1
    while True:
        if res[pos] != 'z':
            res[pos] = chr(ord(res[pos]) + 1)
            break
        else:
            res[pos] = 'a'
            pos -= 1
        if pos < 0:
            break
    return ''.join(res)


def check1(line):
    variants = [(ord(a), ord(b), ord(c)) for a, b, c in zip(line[:-2], line[1:-1], line[2:])]
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


with open("input2.txt", "r") as f:
    line = f.readline()
    line = line.strip()

print(line)
line = inc(line)
while not (check1(line) and check2(line) and check3(line)):
    line = inc(line)
print(line)
