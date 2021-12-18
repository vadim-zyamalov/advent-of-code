def step(molecule, rules):
    result = molecule[0]
    for fst, snd in zip(molecule[:-1], molecule[1:]):
        if (fst + snd) in rules:
            result += rules[fst + snd] + snd
        else:
            result += snd
    return result


def count(molecule):
    result = {}
    for atom in molecule:
        if atom not in result:
            result[atom] = 0
        result[atom] += 1
    return result


def borders(molecule):
    freq = count(molecule)
    amin = len(molecule)
    amax = 0
    for k in freq:
        amin = min(amin, freq[k])
        amax = max(amax, freq[k])
    return amax, amin


molecule = ''
rules = {}

with open("sample.txt", "r", encoding="utf-8") as f:
    molecule = f.readline().strip()
    for line in f:
        if line.strip() == '':
            continue
        key, _, val = line.strip().partition(' -> ')
        rules[key] = val

result = molecule
for i in range(10):
    result = step(result, rules)
    if i == 10 - 1:
        amax, amin = borders(result)
        print(f"Part 1: {amax - amin}")
        print(count(result))
    if i == 40 - 1:
        amax, amin = borders(result)
        print(f"Part 2: {amax - amin}")
