replacements = {}
molecule = ""
result = set()


def splitx(molecule):
    result = []
    tmp = ""
    for letter in molecule:
        if str.isupper(letter) and tmp:
            result.append(tmp)
            tmp = ""
        tmp += letter
    if tmp:
        result.append(tmp)
    return result


with open("_inputs/2015/day-19/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "=>" in line:
            key, _, val = line.strip().partition(" => ")
            if key not in replacements:
                replacements[key] = []
            replacements[key].append(val)
        elif line.strip() == "":
            continue
        else:
            molecule = splitx(line.strip())

length = len(molecule)
for atom in range(length):
    if molecule[atom] in replacements:
        for action in replacements[molecule[atom]]:
            result.add("".join(molecule[:atom] + [action] + molecule[(atom + 1) :]))

print(f"Part 1: {len(result)}")
