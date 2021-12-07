# Function to process list of Aunties Sues
def score(sue, clues):
    denominator = len(sue)
    nominator = 0
    for k in sue:
        if sue[k] == clues[k]:
            nominator += 1
    return nominator / denominator


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
                if clues[fact] == int(val.strip()):
                    numerator += 1
            if numerator == denominator:
                print(f"Possible Auntie Sue is one of number {number}")

