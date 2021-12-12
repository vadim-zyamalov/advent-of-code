replacements = {}
molecule = ''

MAX_LEN = 1000


def alen(molecule):
    return sum(1 for _ in atomize(molecule))


def atomize(molecule):
    tmp = ''
    length = len(molecule)
    start = 0
    for i in range(length):
        if str.isupper(molecule[i]) and tmp:
            yield tmp, start, i - 1
            tmp = ''
        tmp += molecule[i]
        start = i
    if tmp:
        yield tmp, start, length - 1


def process(molecule, replacements, echo):
    length = len(molecule)
    if length < 1:
        return MAX_LEN
    if molecule in replacements and \
        'e' in replacements[molecule]:
        return 1
    pool = []
    for i in range(length):
        if str.islower(molecule[i]):
            continue
        if echo:
            print("{}/{}".format(i, length))
        for k in replacements:
            if molecule[i:].startswith(k):
                for r in replacements[k]:
                    if r != 'e':
                        tmp = process(molecule[:i] + r + molecule[(i+len(k)):], replacements, False)
                        if tmp < MAX_LEN:
                            pool.append(tmp)
    if pool:
        return 1 + min(pool)
    return MAX_LEN


with open("input.txt", "r") as f:
    for line in f:
        if "=>" in line:
            key, _, val = line.strip().partition(" => ")
            if val not in replacements:
                replacements[val] = []
            replacements[val].append(key)
        elif line.strip() == "":
            continue
        else:
            molecule = line.strip()

print(process(molecule, replacements, True))
