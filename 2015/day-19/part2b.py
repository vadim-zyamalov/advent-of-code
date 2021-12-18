replacements = []
molecule = ''

filter = set()


def process(molecule, replacements):
    stack = []

    stack.append((len(molecule), 0, molecule))
    filter.add(molecule)

    while stack != []:
        _, steps, state = stack.pop()

        if state == 'e':
            return steps

        length = len(state)
        for i in range(length):
            for fst, snd in replacements:
                if state[i:].startswith(snd):
                    tmp = state[:i] + fst + state[(i + len(snd)):]
                    if tmp not in filter:
                        filter.add(tmp)
                        stack.append((len(tmp), steps + 1, tmp))


with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "=>" in line:
            key, _, val = line.strip().partition(" => ")
            replacements.append((key, val))
        elif line.strip() == "":
            continue
        else:
            molecule = line.strip()

print(f"Part 2: {process(molecule, replacements)}")
