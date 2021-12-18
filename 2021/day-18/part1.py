from math import floor, ceil


def parse(number):
    if number[0] != '[':
        return int(number)
    result = []
    tmp = ''
    count = 0
    for letter in number[1:-1]:
        if letter == '[':
            tmp += letter
            count += 1
        elif letter == ']':
            tmp += letter
            count -= 1
        elif (letter == ',') and \
             (count == 0):
            result.append(parse(tmp))
            tmp = ''
        else:
            tmp += letter
    if tmp != '':
        result.append(parse(tmp))
    return result


def magnitude(number):
    if isinstance(number, int):
        return number
    if isinstance(number[0], int) and \
       isinstance(number[1], int):
        return 3 * number[0] + 2 * number[1]
    return (3 * magnitude(number[0]) +
            2 * magnitude(number[1]))


def magnitude_line(number):
    result = number
    while True:
        ex_start = -1
        ex_finish = -1
        length = len(result)

        for i in range(length):
            if result[i] == '[':
                ex_start = i
                ex_finish = i
            elif result[i] == ']':
                ex_finish = i
                break
        if ex_start == -1:
            break
        left_chunk = result[:ex_start]
        right_chunk = result[(ex_finish+1):]
        tmp = result[(ex_start+1):ex_finish].split(",")
        result = left_chunk + \
            str(3 * int(tmp[0]) + 2 * int(tmp[1])) + \
            right_chunk
    return int(result)


def find_explodable_line(number):
    ex_start = -1
    ex_finish = -1
    length = len(number)

    count = 0
    for i in range(length):
        if number[i] == '[':
            count += 1
            ex_start = i
            ex_finish = i
        elif number[i] == ']':
            if count > 4:
                ex_finish = i
                break
            count -= 1
            ex_start = -1
            ex_finish = -1
    if ex_finish > 0:
        return (ex_start, ex_finish)
    return (-1, -1)


def find_splittable_line(number):
    r_start = -1
    r_finish = -1
    length = len(number)

    for i in range(length):
        if number[i].isdigit():
            if r_start == -1:
                r_start = i
                r_finish = i
            else:
                r_finish = i
        else:
            if (r_start > -1) and \
               (r_finish - r_start > 0):
                return (r_start, r_finish)
            r_start = -1
            r_finish = -1
    return (r_start, r_finish)


def find_regular_line(chunk, ltr=True):
    step = 1 if ltr else -1
    start = 0 if ltr else (len(chunk) - 1)
    finish = len(chunk) if ltr else -1

    r_start = -1
    r_finish = -1
    for i in range(start, finish, step):
        if chunk[i].isdigit():
            if r_start == -1:
                r_start = i
                r_finish = i
            else:
                r_finish = i
        else:
            if r_start != -1:
                r_start, r_finish = \
                    min(r_start, r_finish), max(r_start, r_finish)
                return (r_start, r_finish)
    return (r_start, r_finish)


def explode_line(number, explodable):
    left_chunk = number[:explodable[0]]
    right_chunk = number[(explodable[1]+1):]
    target = [int(el)
              for el in number[(explodable[0]+1):explodable[1]].split(',')]

    tmp = find_regular_line(left_chunk, False)
    if tmp[0] != -1:
        left_chunk = left_chunk[:tmp[0]] + \
            str(int(left_chunk[tmp[0]:(tmp[1]+1)]) + target[0]) + \
            left_chunk[(tmp[1]+1):]

    tmp = find_regular_line(right_chunk, True)
    if tmp[0] != -1:
        right_chunk = right_chunk[:tmp[0]] + \
            str(int(right_chunk[tmp[0]:(tmp[1]+1)]) + target[1]) + \
            right_chunk[(tmp[1]+1):]

    return left_chunk + '0' + right_chunk


def split_line(number, splittable):
    left_chunk = number[:splittable[0]]
    right_chunk = number[(splittable[1]+1):]
    tmp = int(number[splittable[0]:(splittable[1]+1)])
    fst, snd = floor(tmp / 2), ceil(tmp / 2)
    return left_chunk + '[{},{}]'.format(fst, snd) + right_chunk


def reduce_line(number):
    result = number
    while True:
        ex = find_explodable_line(result)
        if ex[0] != -1:
            result = explode_line(result, ex)
            continue
        sp = find_splittable_line(result)
        if sp[0] != -1:
            result = split_line(result, sp)
            continue
        if (ex[0] == -1) and (sp[0] == -1):
            break
    return result


def num_add(n1, n2):
    return f"[{n1},{n2}]"


numbers = []
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        numbers.append(line.strip())

answer = numbers[0]
for number in numbers[1:]:
    answer = reduce_line(num_add(answer, number))
answer = magnitude_line(answer)
print(f"Part 1: {answer}")

answer = []
for i, number1 in enumerate(numbers):
    for j, number2 in enumerate(numbers):
        if i == j:
            continue
        answer.append(
            magnitude_line(
                reduce_line(num_add(number1, number2))
            )
        )

print(f"Part 2: {max(answer)}")
