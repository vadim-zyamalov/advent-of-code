# key - length, value - digit
lengths = {2: 1,
           4: 4,
           3: 7,
           7: 8}

digits = [set('abcefg'),
          set('cf'),
          set('acdeg'),
          set('acdfg'),
          set('bcdf'),
          set('abdfg'),
          set('abdefg'),
          set('acf'),
          set('abcdefg'),
          set('abcdfg')]


def dict_invert(dictionary):
    result = {}
    for k in dictionary:
        result[dictionary[k]] = k
    return result


def decoder(number, codelist):
    tmp = list(number)
    result = set()
    for i in tmp:
        result.add(codelist[i])
    return result


def get_a(numbers, segments, patterns):
    return list(numbers[7] - numbers[1])[0]


def get_b(numbers, segments, patterns):
    tmp_d = get_d(numbers, segments, patterns)
    return list(numbers[4] - numbers[7] - set(tmp_d))[0]


def get_c(numbers, segments, patterns):
    tmp_6 = get_6(numbers, segments, patterns)
    return list(numbers[8] - tmp_6)[0]


def get_d(numbers, segments, patterns):
    tmp_0 = get_0(numbers, segments, patterns)
    return list(numbers[8] - tmp_0)[0]


def get_e(numbers, segments, patterns):
    tmp_9 = get_9(numbers, segments, patterns)
    return list(numbers[8] - tmp_9)[0]


def get_f(numbers, segments, patterns):
    tmp_c = get_c(numbers, segments, patterns)
    return list(numbers[1] - set(tmp_c))[0]


def get_g(numbers, segments, patterns):
    for p in patterns:
        tmp = p - numbers[7] - numbers[4]
        if len(tmp) == 1:
            return list(tmp)[0]
    exit(1)


def get_0(numbers, segments, patterns):
    for p in patterns:
        tmp = numbers[8] - p
        if (len(tmp) == 1) and \
                (len(tmp & (numbers[4] - numbers[1])) == 1):
            return p
    exit(1)


def get_6(numbers, segments, patterns):
    for p in patterns:
        tmp = numbers[8] - p
        if (len(tmp) == 1) and (len(tmp & numbers[1]) == 1):
            return p
    exit(1)


def get_9(numbers, segments, patterns):
    for p in patterns:
        tmp = numbers[8] - p
        if (len(tmp) == 1) and (len(tmp & numbers[4]) == 0):
            return p
    exit(1)


answer = 0
with open("input.txt", "r") as f:
    for line in f:
        segments = {'a': None,
                    'b': None,
                    'c': None,
                    'd': None,
                    'e': None,
                    'f': None,
                    'g': None}

        numbers = {1: set(),
                   4: set(),
                   7: set(),
                   8: set()}

        patterns, _, output = line.strip().partition(' | ')
        patterns = [set(d) for d in patterns.split()]
        output = [set(d) for d in output.split()]
        for d in patterns:
            length = len(d)
            if length in lengths:
                numbers[lengths[length]] = d
        segments['a'] = get_a(numbers, segments, patterns)
        segments['b'] = get_b(numbers, segments, patterns)
        segments['d'] = get_d(numbers, segments, patterns)
        segments['c'] = get_c(numbers, segments, patterns)
        segments['e'] = get_e(numbers, segments, patterns)
        segments['f'] = get_f(numbers, segments, patterns)
        segments['g'] = get_g(numbers, segments, patterns)

        codelist = dict_invert(segments)
        result = ''.join([str(digits.index(decoder(d, codelist))) for d in output])

        answer += int(result)

print("Part 2: {}".format(answer))
