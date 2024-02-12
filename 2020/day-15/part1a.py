if __name__ == "__main__":
    with open("_inputs/2020/day-15/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    count = [0] * 30_000_000

    for i, num in enumerate(numbers):
        count[num] = i + 1

    prev = numbers[-1]

    for i in range(len(numbers) + 1, 30_000_000 + 1):
        if i == 2021:
            print(f"Part 1: {prev}")
        nxt = (i - 1 - count[prev]) if count[prev] != 0 else 0
        count[prev] = i - 1
        prev = nxt

    print(f"Part 2: {prev}")
