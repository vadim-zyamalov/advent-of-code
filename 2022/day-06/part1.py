with open("../../_inputs/2022/day-06/input.txt", "r", encoding="utf8") as f:
    tmp = f.read(3)
    steps = 3
    d = f.read(1)
    while d != "\n":
        steps += 1
        tmp = tmp + d
        if len(set(tmp)) == 4:
            break
        tmp = tmp[1:]
        d = f.read(1)

print(f"Part 1: {steps}")

with open("../../_inputs/2022/day-06/input.txt", "r", encoding="utf8") as f:
    tmp = f.read(13)
    steps = 13
    d = f.read(1)
    while d != "\n":
        steps += 1
        tmp = tmp + d
        if len(set(tmp)) == 14:
            break
        tmp = tmp[1:]
        d = f.read(1)

print(f"Part 2: {steps}")
