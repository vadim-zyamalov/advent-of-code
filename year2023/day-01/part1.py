with open("../../_inputs/2023/day-01/input.txt", "r", encoding="utf8") as f:
    total = 0

    for line in f:
        if line.strip() == "":
            break
        digits = [el for el in line.strip() if el.isdigit()]
        total += int(digits[0] + digits[-1])

    print(f"Part 1: {total}")
