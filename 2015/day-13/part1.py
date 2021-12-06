def permute(elements):
    if len(elements) == 1:
        return elements
    res = []
    for el in elements:
        for v in permute([l for l in elements if l != el]):
            res.append([el] + (v if isinstance(v, list) else [v]))
    return res


def add_self(preferences):
    res = preferences.copy()
    guests = list(res.keys())
    res['_self_'] = {}
    for k in guests:
        res[k]['_self_'] = 0
        res['_self_'][k] = 0
    return res


def calc(variant, preferences):
    ans = 0
    num = len(variant)
    for i in range(num):
        name1 = variant[i]
        name2 = variant[(i + 1) % num]
        ans += preferences[name1][name2] if \
            name1 in preferences and \
            name2 in preferences[name1] \
            else 0
        ans += preferences[name2][name1] if \
            name2 in preferences and \
            name1 in preferences[name2] \
            else 0
    return ans


preferences = {}

with open("input.txt", "r") as f:
    for line in f:
        string = line.strip().strip('.').split()
        if string[0] not in preferences:
            preferences[string[0]] = {}
        preferences[string[0]][string[-1]] = int(string[3]) \
            if string[2] == 'gain' else -int(string[3])

# part2
preferences = add_self(preferences)
# end of part2

guests = list(preferences.keys())
variants = [v for v in permute(guests) if v[0] == guests[0]]
print(max(calc(v, preferences) for v in variants))
