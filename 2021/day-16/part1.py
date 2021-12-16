def hex_to_bin(data):
    answer = ''
    for letter in data:
        tmp = bin(int(letter, 16))[2:]
        tmp = '0' * (4 - len(tmp)) + tmp
        answer += tmp
    return answer


def prod(elements):
    answer = 1
    for element in elements:
        answer *= element
    return answer


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
        chunk_start = i
        while i - chunk_start < length:
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


def vsum(packet):
    answer = packet['Version']
    if isinstance(packet['Value'], list):
        for sub_packet in packet['Value']:
            answer += vsum(sub_packet)
    return answer


def execute(packet):
    typeid = packet['TypeID']
    if typeid == 4:
        return packet['Value']
    tmp = []
    for sub_packet in packet['Value']:
        tmp.append(execute(sub_packet))

    answer = None
    if typeid == 0:
        answer = sum(tmp)
    elif typeid == 1:
        answer = prod(tmp)
    elif typeid == 2:
        answer = min(tmp)
    elif typeid == 3:
        answer = max(tmp)
    elif typeid == 5:
        answer = 1 if tmp[0] > tmp[1] else 0
    elif typeid == 6:
        answer = 1 if tmp[0] < tmp[1] else 0
    elif typeid == 7:
        answer = 1 if tmp[0] == tmp[1] else 0
    return answer


with open("input.txt", "r") as f:
    message = f.readline().strip()

bmessage = hex_to_bin(message)
result = parse(bmessage)
print("Part 1: {}".format(vsum(result[0])))
print("Part 2: {}".format(execute(result[0])))
