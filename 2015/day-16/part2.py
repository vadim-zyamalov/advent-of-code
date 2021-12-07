clues = {}

with open("clues.txt", "r") as f:
    for line in f:
        if line.strip() != '':
            fact, _, val = line.strip().partition(':')
            clues[fact] = int(val.strip())

with open("input.txt", "r") as f:
    for line in f:
        if line.strip() != '':
            name, _, rest = line.strip().partition(":")
            _, number = name.split()
            facts = rest.strip().split(',')
            denominator = len(facts)
            numerator = 0
            for el in facts:
                fact, _, val = el.strip().partition(':')
                val = int(val.strip())
                if fact in ['cats', 'trees'] and (clues[fact] < val):
                    numerator += 1
                elif fact in ['pomeranians', 'goldfish'] and (clues[fact] > val):
                    numerator += 1
                elif clues[fact] == val:
                    numerator += 1
            if numerator == denominator:
                print(f"Possible Auntie Sue is one of number {number}")

