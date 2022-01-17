powers = {'a': 1 << 6,
          'b': 1 << 5,
          'c': 1 << 4,
          'd': 1 << 3,
          'e': 1 << 2,
          'f': 1 << 1,
          'g': 1 << 0}


def split_patterns(patterns):
    unique = {}
    plural = []
    for p in patterns:
        n = bin(p).count('1')
        match n:
            case 2:
                unique[1] = p
            case 4:
                unique[4] = p
            case 3:
                unique[7] = p
            case 7:
                unique[8] = p
            case _:
                plural.append(p)
    return unique, plural


def pattern_to_num(pattern):
    result = 0
    for letter in pattern:
        result |= powers[letter]
    return result


def diff(x, y):
    return x ^ (x & y)


def single(x):
    return True if x and not (x & (x - 1)) else False


def create_codelist(corrupted, original):
    result = {}
    for k in corrupted:
        result[corrupted[k]] = original[k]
    return result


def decoder(number, codelist):
    result = 0
    for i in codelist:
        if (number & i):
            result |= codelist[i]
    return result


def get_a(numbers, *_):
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


def get_g(numbers, _, patterns):
    for p in patterns:
        tmp = diff(diff(p, numbers[7]), numbers[4])
        if bin(tmp).count('1') == 1:
            return tmp
    exit(1)


def get_0(numbers, _, patterns):
    for p in patterns:
        tmp = diff(numbers[8], p)
        if single(tmp) and \
                single(tmp & diff(numbers[4], numbers[1])):
            return p
    exit(1)


def get_6(numbers, _, patterns):
    for p in patterns:
        tmp = diff(numbers[8], p)
        if single(tmp) and single(tmp & numbers[1]):
            return p
    exit(1)


def get_9(numbers, _, patterns):
    for p in patterns:
        tmp = diff(numbers[8], p)
        if single(tmp) and not (tmp & numbers[4]):
            return p
    exit(1)


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
with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        segments = {'a': None,
                    'b': None,
                    'c': None,
                    'd': None,
                    'e': None,
                    'f': None,
                    'g': None}

        patterns, _, output = line.strip().partition(' | ')
        patterns = [pattern_to_num(d) for d in patterns.split()]
        output = [pattern_to_num(d) for d in output.split()]
        numbers, patterns = split_patterns(patterns)

        segments['a'] = get_a(numbers, segments, patterns)
        segments['b'] = get_b(numbers, segments, patterns)
        segments['d'] = get_d(numbers, segments, patterns)
        segments['c'] = get_c(numbers, segments, patterns)
        segments['e'] = get_e(numbers, segments, patterns)
        segments['f'] = get_f(numbers, segments, patterns)
        segments['g'] = get_g(numbers, segments, patterns)

        codelist = create_codelist(segments, powers)
        result = 0
        for d in output:
            result *= 10
            result += digits.index(decoder(d, codelist))
        answer += result

print(f"Part 2: {answer}")
