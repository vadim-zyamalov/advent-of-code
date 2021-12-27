def rotate(letter, num):
    return chr((ord(letter) - ord('a') + num) % 26 + ord('a'))


answer = 0
correct = []

with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        rest, checksum = line.strip()[:-1].split("[")
        name, sector_id = rest.rsplit("-", 1)
        freq = {}
        for letter in name:
            if letter != "-":
                if letter not in freq:
                    freq[letter] = 0
                freq[letter] -= 1
        testsum = "".join([k
                           for k, _ in sorted(
                                   freq.items(),
                                   key=lambda x: (x[1], x[0])
                           )][:5])
        if testsum == checksum:
            answer += int(sector_id)
            decoded = ""
            for letter in name:
                if letter == "-":
                    decoded += " "
                else:
                    decoded += rotate(letter, int(sector_id))
            correct.append((decoded, int(sector_id)))

print(f"Part 1: {answer}")

for name, sector_id in correct:
    if "north" in name:
        print(f"Part 2: {sector_id}, {name}")
