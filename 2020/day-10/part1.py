from collections import Counter
from functools import cache


@cache
def combinations(num, numbers):
    if num == max(numbers):
        return 1
    return sum(combinations(num + i, numbers) for i in (1, 2, 3) if num + i in numbers)


if __name__ == "__main__":
    with open("_inputs/2020/day-10/input.txt", "r", encoding="utf8") as f:
        numbers = tuple(sorted(map(int, f.read().strip().split("\n"))))

    diff = [n1 - n0 for n0, n1 in zip((0,) + numbers, numbers + (numbers[-1] + 3,))]
    count = Counter(diff)
    print(f"Part 1: {count[1] * count[3]}")

    print(f"Part 2: {combinations(0, numbers)}")
