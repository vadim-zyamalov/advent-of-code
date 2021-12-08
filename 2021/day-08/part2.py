lengths = {2: 1, 4: 4, 3: 7, 7: 8}

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
    res = {}
    for k in dictionary:
        res[dictionary[k]] = k
    return res


def decoder(number, codelist):
    tmp = list(number)
    res = set()
    for i in tmp:
        res.add(codelist[i])
    return res


def get_a(numbers, segments, patterns):
    return list(numbers[7] - numbers[1])[0]


def get_b(numbers, segments, patterns):
    return list(numbers[4] - numbers[7] - set(segments['d']))[0]


def get_c(numbers, segments, patterns):
    return list(numbers[8] - numbers[6])[0]


def get_d(numbers, segments, patterns):
    return list(numbers[8] - numbers[0])[0]


def get_e(numbers, segments, patterns):
    return list(numbers[8] - numbers[9])[0]


def get_f(numbers, segments, patterns):
    return list(numbers[1] - set(segments['c']))[0]


def get_g(numbers, segments, patterns):
    for p in patterns:
        tmp = p - numbers[7] - numbers[4]
        if len(tmp) == 1:
            return list(tmp)[0]
    exit(1)


def get_0(numbers, segments, patterns):
    tmp_bd = numbers[4] - numbers[1]
    for p in patterns:
        tmp = numbers[8] - p
        if (len(tmp) == 1) and (len(tmp & tmp_bd) == 1):
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


ans = 0
with open("input.txt", "r") as f:
    for line in f:
        segments = {'a': None,
                    'b': None,
                    'c': None,
                    'd': None,
                    'e': None,
                    'f': None,
                    'g': None}

        numbers = {0: set(),
                   1: set(),
                   2: set(),
                   3: set(),
                   4: set(),
                   5: set(),
                   6: set(),
                   7: set(),
                   8: set(),
                   9: set()}

        patterns, _, output = line.strip().partition(' | ')
        patterns = [set(d) for d in patterns.split()]
        output = [set(d) for d in output.split()]
        for d in patterns:
            length = len(d)
            if length in lengths:
                numbers[lengths[length]] = d
        numbers[0] = get_0(numbers, segments, patterns)
        numbers[6] = get_6(numbers, segments, patterns)
        numbers[9] = get_9(numbers, segments, patterns)
        segments['a'] = get_a(numbers, segments, patterns)
        segments['d'] = get_d(numbers, segments, patterns)
        segments['b'] = get_b(numbers, segments, patterns)
        segments['g'] = get_g(numbers, segments, patterns)
        segments['e'] = get_e(numbers, segments, patterns)
        segments['c'] = get_c(numbers, segments, patterns)
        segments['f'] = get_f(numbers, segments, patterns)

        codelist = dict_invert(segments)
        res = ''.join([str(digits.index(decoder(d, codelist))) for d in output])

        ans += int(res)

print(ans)
