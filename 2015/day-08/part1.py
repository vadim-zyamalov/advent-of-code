chars = 0
codes = 0

with open("_inputs/2015/day-08/input.txt", "r", encoding="utf-8") as f:
    for line in f:
        string = []
        for letter in line.strip():
            string.append(letter)
        i = 0
        while i < len(string):
            match string[i]:
                case '"':
                    codes += 1
                case "\\":
                    codes += 1
                    match string[i + 1]:
                        case '"':
                            codes += 1
                            chars += 1
                            i += 1
                        case "\\":
                            codes += 1
                            chars += 1
                            i += 1
                        case "x":
                            codes += 3
                            chars += 1
                            i += 3
                case _:
                    codes += 1
                    chars += 1
            i += 1
print(f"Part 1: {codes - chars}")
