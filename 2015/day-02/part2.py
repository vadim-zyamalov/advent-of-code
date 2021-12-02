ans = 0

with open("input.txt", "r") as f:
    for present in f:
        dims = [int(i) for i in present.strip().split("x")]
        dims.sort()
        ans += 2 * (dims[0] + dims[1])
        ans += dims[0] * dims[1] * dims[2]

print(ans)
