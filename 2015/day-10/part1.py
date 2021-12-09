def look_and_say_slow(string):
    res = ''
    groups = []

    prev = None
    tmp = []
    for letter in string:
        if not prev:
            tmp.append(letter)
            prev = letter
        else:
            if prev != letter:
                groups.append(tmp)
                tmp = [letter]
                prev = letter
            else:
                tmp.append(letter)
    groups.append(tmp)
    for group in groups:
        res = res + str(len(group)) + group[0]
    return res


def look_and_say_fast(string):
    res = ''
    count = 0
    prev = None
    for letter in string:
        if not prev:
            count += 1
            prev = letter
        elif prev != letter:
            res += str(count) + prev
            count = 1
            prev = letter
        else:
            count += 1
    if count > 0:
        res += str(count) + str(prev)
    return res

part = {1: 40, 2: 50}
for k in part:
    with open("input.txt", "r") as f:
        line = f.read()
        line = line.strip()

    for i in range(part[k]):
        line = look_and_say_fast(line)

    print("Part {}: {}".format(k, len(line)))
