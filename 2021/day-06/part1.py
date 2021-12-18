def step(fishes):
    result = fishes.copy()
    tmp = result[0]
    result[:-1] = result[1:]
    result[8] = tmp
    result[6] += tmp
    return result


with open("input.txt", "r", encoding="utf-8") as f:
    tmp = [int(i) for i in f.readline().strip().split(',')]

steps = {1: 80, 2: 256}

for part, steps_num in steps.items():
    fishes = [0 for _ in range(0, 9)]

    for i in tmp:
        fishes[i] += 1

    for i in range(steps_num):
        fishes = step(fishes)

    print(f"Part {part}: {sum(fishes)}")
