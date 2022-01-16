def splitx(input):
    opener = '[{'
    closer = ']}'

    result = []
    tmp = ''
    counter = 0
    for letter in input:
        match letter:
            case l if l in opener:
                if counter > 0:
                    tmp += letter
                counter += 1
            case l if l in closer:
                counter -= 1
                if counter > 0:
                    tmp += letter
                else:
                    result.append(tmp)
                    tmp = ''
            case ',':
                if counter > 1:
                    tmp += letter
                else:
                    result.append(tmp)
                    tmp = ''
            case _:
                tmp += letter
    return result


def elparser(input):
    key, _, val = input.partition(':')
    return key.strip('"'), val.strip('"')


def parser(input):
    if len(input) == 0:
        return None
    match input[0]:
        case '[':
            result = []
            elements = splitx(input)
            for i in elements:
                tmp = parser(i.strip())
                result.append(tmp)
            return result
        case '{':
            result = {}
            elements = splitx(input)
            for i in elements:
                key, val = elparser(i.strip())
                tmp = parser(val)
                result[key] = tmp
            return result
        case _:
            if input.strip().lstrip('-').isnumeric():
                return int(input.strip())
            else:
                return input.strip().strip('"')


def dive(data):
    ans = 0
    if isinstance(data, dict):
        for i in data:
            if isinstance(data[i], str) and (data[i] == 'red'):
                return 0
        for i in data:
            tmp = dive(data[i])
            if tmp:
                ans += tmp
        return ans
    if isinstance(data, list):
        for i in data:
            tmp = dive(i)
            if tmp:
                ans += tmp
        return ans
    if isinstance(data, int):
        return data
    return 0


with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read()
    data = parser(data.strip())

print(f"Part 2: {dive(data)}")
