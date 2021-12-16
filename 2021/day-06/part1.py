def step(fishes):
    result = fishes.copy()
    tmp = result[0]
    result[:-1] = result[1:]
    result[8] = tmp
    result[6] += tmp
    return result


with open("input.txt", "r") as f:
    tmp = [int(i) for i in f.readline().strip().split(',')]

steps = {1: 80, 2: 256}

for k in steps:
    fishes = [0 for _ in range(0, 9)]

    for i in tmp:
        fishes[i] += 1

    for i in range(steps[k]):
        fishes = step(fishes)

    print("Part {}: {}".format(k, sum(fishes)))
