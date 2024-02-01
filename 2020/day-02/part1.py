from collections import Counter


if __name__ == "__main__":
    with open("_inputs/2020/day-02/input.txt", "r", encoding="utf8") as f:
        part1 = 0
        part2 = 0
        for line in f:
            line = line.strip()
            if line == "":
                break
            policy, password = line.split(": ")
            rng, letter = policy.split()
            lb, ub = tuple(map(int, rng.split("-")))

            count = Counter(password)
            if lb <= count[letter] <= ub:
                part1 += 1

            if (password[lb - 1] == letter) ^ (password[ub - 1] == letter):
                part2 += 1

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
