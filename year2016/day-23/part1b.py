def fact(x):
    ans = 1
    for i in range(x, 1, -1):
        ans *= i
    return ans


c = 85
d = 76

a = 7
print(f"Part 1: {fact(a) + c * d}")

a = 12
print(f"Part 2: {fact(a) + c * d}")
