clues = {}

with open("clues.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() != '':
            fact, _, val = line.strip().partition(':')
            clues[fact] = int(val.strip())

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() != '':
            name, _, rest = line.strip().partition(":")
            _, number = name.split()
            facts = rest.strip().split(',')
            denominator = len(facts)
            numerator = 0
            for el in facts:
                fact, _, val = el.strip().partition(':')
                if clues[fact] == int(val.strip()):
                    numerator += 1
            if numerator == denominator:
                print(f"Part 1: {number}")
