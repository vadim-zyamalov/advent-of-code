answer = 0
bad = ["ab", "cd", "pq", "xy"]

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        vowels = sum([1 for i in line if i in "aeiou"])
        tmp = [f"{a}{b}" for a, b in zip(line[:-1], line[1:])]
        double = False
        nopair = True
        for pair in tmp:
            if pair in bad:
                nopair = False
                break
            if pair[0] == pair[1]:
                double = True
        if (vowels > 2) and double and nopair:
            answer += 1

print(f"Part 1: {answer}")
