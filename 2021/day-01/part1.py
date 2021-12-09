prev = None
ans  = 0

with open("input.txt", "r") as f:
    for i in f:
        if prev and (prev < int(i)):
            ans += 1
        prev = int(i)

print("Part 1: {}".format(ans))
