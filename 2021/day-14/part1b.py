def step(pairs, rules):
    result = {}
    for k in pairs:
        pair0, pair1 = k[0] + rules[k], rules[k] + k[1]
        if pair0 not in result:
            result[pair0] = 0
        result[pair0] += pairs[k]
        if pair1 not in result:
            result[pair1] = 0
        result[pair1] += pairs[k]
    return result


def count(pairs, molecule):
    result = {}
    result[molecule[-1]] = 1
    for k in pairs:
        if k[0] not in result:
            result[k[0]] = 0
        result[k[0]] += pairs[k]
    return result


rules = {}
pairs = {}
molecule = ''

with open("input.txt", "r") as f:
    molecule = f.readline().strip()
    for line in f:
        if line.strip() == '':
            continue
        key, _, val = line.strip().partition(' -> ')
        rules[key] = val
        pairs[key] = 0

for fst, snd in zip(molecule[:-1], molecule[1:]):
    pairs[fst + snd] += 1

for i in range(40):
    pairs = step(pairs, rules)
    if i == 9: # 10-th step
        tmp = count(pairs, molecule)
        amax = max(tmp.values())
        amin = min(tmp.values())
        print("Part 1: {}".format(amax - amin))
    if i == 39: # 10-th step
        tmp = count(pairs, molecule)
        amax = max(tmp.values())
        amin = min(tmp.values())
        print("Part 2: {}".format(amax - amin))
