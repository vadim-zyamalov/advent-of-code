def splitx(input):
    opener = '[{'
    closer = ']}'

    res = []
    tmp = ''
    counter = 0
    for letter in input:
        if letter in opener:
            if counter > 0:
                tmp += letter
            counter += 1
        elif letter in closer:
            counter -= 1
            if counter > 0:
                tmp += letter
            else:
                res.append(tmp)
                tmp = ''
        elif letter == ',':
            if counter > 1:
                tmp += letter
            else:
                res.append(tmp)
                tmp = ''
        else:
            tmp += letter
    return res


def elparser(input):
    key, _, val = input.partition(':')
    return key.strip('"'), val.strip('"')


def parser(input):
    if len(input) == 0:
        return None
    if input[0] == '[':
        res = []
        elements = splitx(input)
        for i in elements:
            tmp = parser(i.strip())
            res.append(tmp)
        return res
    elif input[0] == '{':
        res = {}
        elements = splitx(input)
        for i in elements:
            key, val = elparser(i.strip())
            tmp = parser(val)
            res[key] = tmp
        return res
    elif input.strip().lstrip('-').isnumeric():
        return int(input.strip())
    else:
        return input.strip().strip('"')


def dive(data):
    ans = 0
    if isinstance(data, dict):
        for i in data:
            tmp = dive(data[i])
            if tmp:
                ans += tmp
        return ans
    elif isinstance(data, list):
        for i in data:
            tmp = dive(i)
            if tmp:
                ans += tmp
        return ans
    elif isinstance(data, int):
        return data
    else:
        return 0


with open("input.txt", "r") as f:
    data = f.read()
    data = parser(data.strip())

print("Part 1: {}".format(dive(data)))
