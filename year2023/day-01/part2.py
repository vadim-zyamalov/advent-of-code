DIGITS = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


with open("../../_inputs/2023/day-01/input.txt", "r", encoding="utf8") as f:
    total = 0

    for line in f:
        if line.strip() == "":
            break

        for k, v in DIGITS.items():
            line = line.replace(k, v)

        digits = [el for el in line.strip() if el.isdigit()]
        total += int(digits[0] + digits[-1])

    print(f"Part 2: {total}")
