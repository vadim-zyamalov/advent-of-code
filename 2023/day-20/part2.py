def gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
    return int(abs(a) / gcd(a, b) * abs(b))


def lcmm(nums: list[int]) -> int:
    if not nums:
        return 1
    num = nums.pop(0)
    return lcm(num, lcmm(nums))


if __name__ == "__main__":
    cycles = [
        int("111100110001", 2),
        int("111011010101", 2),
        int("111010011011", 2),
        int("111010110001", 2),
    ]
    res2 = lcmm(cycles)
    print(f"Part 2: {res2}")
