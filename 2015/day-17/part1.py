containers = []
volume = 150


def num_to_bin(i, length):
    result = []
    number = i
    while number > 0:
        result.append(number % 2)
        number //= 2
    while len(result) < length:
        result.append(0)
    result.reverse()
    return result


def calc_vol(variant, containers):
    n = len(containers)
    result = 0
    for i in range(n):
        result += variant[i] * containers[i]
    return result


with open("_inputs/2015/day-17/input.txt", "r") as f:
    for line in f:
        if line.strip() != "":
            containers.append(int(line.strip()))

answer = 0
quantity = {}
for i in range(2 ** len(containers)):
    variant = num_to_bin(i, len(containers))
    if calc_vol(variant, containers) == volume:
        answer += 1
        # part 2 below
        number = sum(variant)
        if number not in quantity:
            quantity[number] = 0
        quantity[number] += 1

minimal = min(list(quantity.keys()))

print(f"Part 1: {answer}")
print(f"Part 2: {quantity[minimal]}")
