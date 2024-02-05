def step(fishes):
    tmp = fishes.pop(0)
    fishes.append(tmp)
    fishes[6] += tmp


with open("_inputs/2021/day-06/input.txt", "r", encoding="utf-8") as f:
    tmp = [int(i) for i in f.readline().strip().split(",")]

steps = {1: 80, 2: 256}

for part, steps_num in steps.items():
    fishes = [0 for _ in range(0, 9)]

    for i in tmp:
        fishes[i] += 1

    for i in range(steps_num):
        step(fishes)

    print(f"Part {part}: {sum(fishes)}")
