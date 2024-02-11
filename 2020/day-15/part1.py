if __name__ == "__main__":
    with open("_inputs/2020/day-15/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    count = {}
    for i, num in enumerate(numbers):
        count[num] = i

    prev = numbers[-1]

    for i in range(len(numbers), 30_000_000):
        if i == 2020:
            print(f"Part 1: {prev}")
        nxt = i - 1 - count.get(prev, i - 1)
        count[prev] = i - 1
        prev = nxt

    print(f"Part 2: {prev}")
