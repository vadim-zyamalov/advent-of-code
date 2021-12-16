message = ''


def hex_to_bin(data):
    result = ''
    for letter in data:
        tmp = bin(int(letter, 16))[2:]
        tmp = '0' * (4 - len(tmp)) + tmp
        result += tmp
    return result


def prod(els):
    result = 1
    for el in els:
        result *= el
    return result


def parse_literal(data, start):
    value = ''
    i = start
    finish = False
    while True:
        if data[i] == '0':
            finish = True
        i += 1
        value += data[i:(i+4)]
        i += 4
        if finish:
            break
    return (int(value, 2), i)


def parse_operator(data, start):
    value = []
    length = None
    number = None
    i = start
    if data[i] == '0':
        i += 1
        length = int(data[i:(i+15)], 2)
        i += 15
    else:
        i += 1
        number = int(data[i:(i+11)], 2)
        i += 11
    if length:
        si = i
        while (i - si < length):
            tmp, i = parse(data, i)
            value.append(tmp)
    if number:
        for _ in range(number):
            tmp, i = parse(data, i)
            value.append(tmp)
    return (value, i)


def parse(data, start=0):
    i = start
    assert i < len(data)

    version = int(data[i:(i+3)], 2)
    i += 3

    typeid = int(data[i:(i+3)], 2)
    i += 3

    if typeid == 4:
        value, i = parse_literal(data, i)
    else:
        value, i = parse_operator(data, i)

    return ({'Version': version,
             'TypeID': typeid,
             'Value': value}, i)


def vsum(input):
    result = input['Version']
    if isinstance(input['Value'], list):
        for el in input['Value']:
            result += vsum(el)
    return result


def execute(input):
    typeid = input['TypeID']
    if typeid == 4:
        return input['Value']
    else:
        tmp = []
        for el in input['Value']:
            tmp.append(execute(el))

        if typeid == 0:
            return sum(tmp)
        elif typeid == 1:
            return prod(tmp)
        elif typeid == 2:
            return min(tmp)
        elif typeid == 3:
            return max(tmp)
        elif typeid == 5:
            return 1 if tmp[0] > tmp[1] else 0
        elif typeid == 6:
            return 1 if tmp[0] < tmp[1] else 0
        elif typeid == 7:
            return 1 if tmp[0] == tmp[1] else 0


with open("input.txt", "r") as f:
    message = f.readline().strip()

bmessage = hex_to_bin(message)
result = parse(bmessage)
print("Part 1: {}".format(vsum(result[0])))
print("Part 2: {}".format(execute(result[0])))
