def permute(elements):
    if len(elements) == 1:
        return [elements]
    result = []
    for el in elements:
        for v in permute([e for e in elements if e != el]):
            result.append([el] + v)
    return result


def add_self(preferences):
    result = preferences.copy()
    guests = list(result.keys())
    result['_self_'] = {}
    for k in guests:
        result[k]['_self_'] = 0
        result['_self_'][k] = 0
    return result


def calc(variant, preferences):
    answer = 0
    number = len(variant)
    for i in range(number):
        name1 = variant[i]
        name2 = variant[(i + 1) % number]
        answer += preferences[name1][name2] if \
            name1 in preferences and \
            name2 in preferences[name1] \
            else 0
        answer += preferences[name2][name1] if \
            name2 in preferences and \
            name1 in preferences[name2] \
            else 0
    return answer


preferences = {}

with open("input.txt", "r") as f:
    for line in f:
        string = line.strip().strip('.').split()
        if string[0] not in preferences:
            preferences[string[0]] = {}
        preferences[string[0]][string[-1]] = int(string[3]) \
            if string[2] == 'gain' else -int(string[3])

for part in [1, 2]:
    if part == 2:
        preferences = add_self(preferences)

    guests = list(preferences.keys())
    variants = [v for v in permute(guests) if v[0] == guests[0]]
    print("Part {}: {}".format(part,
                               max(calc(v, preferences) for v in variants)))
