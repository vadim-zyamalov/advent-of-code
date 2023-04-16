with open("../../_inputs/2022/day-02/input.txt", "r", encoding="utf8") as f:
    score = 0
    for line in f:
        draw = line.strip().split()
        match draw:
            case ["A", "X"] | ["B", "Y"] | ["C", "Z"]:
                score += 3
            case ["A", "Y"] | ["B", "Z"] | ["C", "X"]:
                score += 6
            case _:
                pass
        score += 1 + 'XYZ'.index(draw[1])

print(f"Part 1: {score}")

with open("../../_inputs/2022/day-02/input.txt", "r", encoding="utf8") as f:
    score = 0
    for line in f:
        draw = line.strip().split()
        match draw[1]:
            case "X":
                score += 1 + 'BCA'.index(draw[0])
            case "Y":
                score += 4 + 'ABC'.index(draw[0])
            case "Z":
                score += 7 + 'CAB'.index(draw[0])

print(f"Part 2: {score}")
