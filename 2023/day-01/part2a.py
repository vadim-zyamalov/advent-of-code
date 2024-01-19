DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse_digits(line: str) -> list[int]:
    res = []

    for i in range(len(line)):
        if line[i] in "0123456789":
            res.append(int(line[i]))
            continue
        for k, v in DIGITS.items():
            if line[i:].startswith(k):
                res.append(v)
                break

    return res


with open("../../_inputs/2023/day-01/input.txt", "r", encoding="utf8") as f:
    total = 0

    for line in f:
        if line.strip() == "":
            break

        digits = parse_digits(line.strip())
        total += 10 * digits[0] + digits[-1]

    print(f"Part 2: {total}")
