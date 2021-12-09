ans = 0

vowels = "aeiou"
bad = ["ab", "cd", "pq", "xy"]

with open("input.txt", "r") as f:
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
            ans += 1
print("Part 1: {}".format(ans))
