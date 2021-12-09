prev = None
answer  = 0

with open("input.txt", "r") as f:
    for i in f:
        if prev and (prev < int(i)):
            answer += 1
        prev = int(i)

print("Part 1: {}".format(answer))
