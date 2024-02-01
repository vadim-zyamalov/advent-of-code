from itertools import combinations


if __name__ == "__main__":
    with open("_inputs/2020/day-01/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split("\n")))

    for i, j in combinations(numbers, 2):
        if i + j == 2020:
            print(f"Part 1: {i * j}")
            break

    for i, j, k in combinations(numbers, 3):
        if i + j + k == 2020:
            print(f"Part 2: {i * j * k}")
            break
