replacements = []
molecule = ''
processed = set()


def process(molecule, replacements, echo):
    if molecule == 'e':
        return 0
    length = len(molecule)
    pool = []
    for i in range(length):
        if str.islower(molecule[i]):
            continue
        if echo:
            print("{}/{}".format(i, length))
        for fst, snd in replacements:
            if molecule[i:].startswith(snd):
                r = molecule[:i] + fst + molecule[(i+len(snd)):]
                if r not in processed:
                    processed.add(r)
                    tmp = process(r, replacements, False)
                    if tmp is not None:
                        pool.append(tmp)
    if pool != []:
        return 1 + min(pool)
    return None


with open("input.txt", "r") as f:
    for line in f:
        if "=>" in line:
            key, _, val = line.strip().partition(" => ")
            replacements.append((key, val))
        elif line.strip() == "":
            continue
        else:
            molecule = line.strip()

print(process(molecule, replacements, True))
