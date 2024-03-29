answer = 0

with open("_inputs/2015/day-02/input.txt", "r", encoding="utf-8") as f:
    for present in f:
        dims = [int(i) for i in present.strip().split("x")]
        dims.sort()
        answer += 2 * (dims[0] + dims[1])
        answer += dims[0] * dims[1] * dims[2]

print(f"Part 2: {answer}")
