containers = []
volume = 150


def num_to_bin(i, length):
    res = []
    num = i
    while num > 0:
        res.append(num % 2)
        num //= 2
    while len(res) < length:
        res.append(0)
    res.reverse()
    return res


def calc_vol(variant, containers):
    n = len(containers)
    res = 0
    for i in range(n):
        res += variant[i] * containers[i]
    return res


with open("./input.txt", "r") as f:
    for line in f:
        if line.strip() != "":
            containers.append(int(line.strip()))

ans = 0
quant = {}
for i in range(2 ** len(containers)):
    variant = num_to_bin(i, len(containers))
    if calc_vol(variant, containers) == volume:
        ans += 1
        # part 2 below
        num = sum(variant)
        if not num in quant:
            quant[num] = 0
        quant[num] += 1

minimal = min(list(quant.keys()))

print("Part 1: {}".format(ans))
print("Part 2: {}".format(quant[minimal]))

