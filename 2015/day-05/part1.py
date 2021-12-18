answer = 0

vowels = "aeiou"
bad = ["ab", "cd", "pq", "xy"]

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        prev = ''
        nvowel = 0
        double = False
        nopair = True
        for letter in line:
            if letter in vowels:
                nvowel += 1
            if not double and (prev == letter):
                double = True
            if (prev + letter) in bad:
                nopair = False
                break
            prev = letter
        if nopair and (nvowel > 2) and double:
            answer += 1

print(f"Part 1: {answer}")
