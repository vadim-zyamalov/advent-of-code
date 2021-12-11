powers = {'a': 1<<6,
          'b': 1<<5,
          'c': 1<<4,
          'd': 1<<3,
          'e': 1<<2,
          'f': 1<<1,
          'g': 1<<0}


def pattern_to_num(pattern):
    result = 0
    for letter in pattern:
        result |= powers[letter]
    return result


def diff(x, y):
    return x ^ (x & y)


def dict_invert(dictionary, original):
    result = {}
    for k in dictionary:
        result[dictionary[k]] = original[k]
    return result


def decoder(number, codelist):
    result = 0
    for i in codelist:
        if (number & i):
            result += codelist[i]
    return result


def get_a(numbers, segments, patterns):
    return diff(numbers[7], numbers[1])


def get_b(numbers, segments, patterns):
    tmp_d = get_d(numbers, segments, patterns)
    return diff(diff(numbers[4], numbers[7]), tmp_d)


def get_c(numbers, segments, patterns):
    tmp_6 = get_6(numbers, segments, patterns)
    return diff(numbers[8], tmp_6)


def get_d(numbers, segments, patterns):
    tmp_0 = get_0(numbers, segments, patterns)
    return diff(numbers[8], tmp_0)


def get_e(numbers, segments, patterns):
    tmp_9 = get_9(numbers, segments, patterns)
    return diff(numbers[8], tmp_9)


def get_f(numbers, segments, patterns):
    tmp_c = get_c(numbers, segments, patterns)
    return diff(numbers[1], tmp_c)


def get_g(numbers, segments, patterns):
    for p in patterns:
        tmp = diff(diff(p, numbers[7]), numbers[4])
        if bin(tmp).count('1') == 1:
            return tmp
    exit(1)


def get_0(numbers, segments, patterns):
    for p in patterns:
        tmp = diff(numbers[8], p)
        if (bin(tmp).count('1') == 1) and \
                (bin(tmp & diff(numbers[4], numbers[1])).count('1') == 1):
            return p
    exit(1)


def get_6(numbers, segments, patterns):
    for p in patterns:
        tmp = diff(numbers[8], p)
        if (bin(tmp).count('1') == 1) and (bin(tmp & numbers[1]).count('1') == 1):
            return p
    exit(1)


def get_9(numbers, segments, patterns):
    for p in patterns:
        tmp = diff(numbers[8], p)
        if (bin(tmp).count('1') == 1) and (bin(tmp & numbers[4]).count('1') == 0):
            return p
    exit(1)


# key - length, value - digit
lengths = {2: 1,
           4: 4,
           3: 7,
           7: 8}

digits = [pattern_to_num('abcefg'),
          pattern_to_num('cf'),
          pattern_to_num('acdeg'),
          pattern_to_num('acdfg'),
          pattern_to_num('bcdf'),
          pattern_to_num('abdfg'),
          pattern_to_num('abdefg'),
          pattern_to_num('acf'),
          pattern_to_num('abcdefg'),
          pattern_to_num('abcdfg')]

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

        numbers = {1: 0,
                   4: 0,
                   7: 0,
                   8: 0}

        patterns, _, output = line.strip().partition(' | ')
        patterns = [pattern_to_num(d) for d in patterns.split()]
        output = [pattern_to_num(d) for d in output.split()]
        for d in patterns:
            length = bin(d).count('1')
            if length in lengths:
                numbers[lengths[length]] = d
        segments['a'] = get_a(numbers, segments, patterns)
        segments['b'] = get_b(numbers, segments, patterns)
        segments['d'] = get_d(numbers, segments, patterns)
        segments['c'] = get_c(numbers, segments, patterns)
        segments['e'] = get_e(numbers, segments, patterns)
        segments['f'] = get_f(numbers, segments, patterns)
        segments['g'] = get_g(numbers, segments, patterns)

        codelist = dict_invert(segments, powers)
        result = sum(
            digits.index(decoder(output[d], codelist)) * \
            (10 ** (len(output) - 1 - d)) \
            for d in range(len(output)))
        answer += result

print("Part 2: {}".format(answer))
