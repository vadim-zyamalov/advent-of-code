ans = 0

with open("input.txt", "r") as f:
    for line in f:
        secunda = [f"{a}{b}" for a, b in zip(line[:-1], line[1:])]
        tertia  = [f"{a}{b}" for a, b in zip(line[:-2], line[2:]) if a == b]
        if len(tertia) == 0:
            continue
        for i in range(len(secunda) - 2):
            if secunda[i] in secunda[(i + 2):]:
                ans += 1
                break

print("Part 2: {}".format(ans))

