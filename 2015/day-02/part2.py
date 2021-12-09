answer = 0

with open("input.txt", "r") as f:
    for present in f:
        dims = [int(i) for i in present.strip().split("x")]
        dims.sort()
        answer += 2 * (dims[0] + dims[1])
        answer += dims[0] * dims[1] * dims[2]

print("Part 2: {}".format(answer))
