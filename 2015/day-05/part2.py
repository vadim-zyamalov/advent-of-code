answer = 0

with open("_inputs/2015/day-05/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        secunda = [f"{a}{b}" for a, b in zip(line[:-1], line[1:])]
        tertia = [f"{a}{b}" for a, b in zip(line[:-2], line[2:]) if a == b]
        if len(tertia) == 0:
            continue
        for i in range(len(secunda) - 2):
            if secunda[i] in secunda[(i + 2) :]:
                answer += 1
                break

print(f"Part 2: {answer}")
