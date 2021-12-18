answer = 0

with open("input.txt", "r", encoding="utf-8") as f:
    for present in f:
        dims = [int(i) for i in present.strip().split("x")]
        dims.sort()
        answer += 3 * dims[0] * dims[1]
        answer += 2 * dims[1] * dims[2]
        answer += 2 * dims[0] * dims[2]

print(f"Part 1: {answer}")
