with open("_inputs/2021/day-10/input.txt", "r", encoding="utf-8") as f:
    stack = []
    answer = 0
    for line in f:
        for char in line.strip():
            if char in "([{<":
                stack.append(char)
            else:
                tmp = stack.pop()
                if (char == ")") and (tmp != "("):
                    answer += 3
                    break
                if (char == "]") and (tmp != "["):
                    answer += 57
                    break
                if (char == "}") and (tmp != "{"):
                    answer += 1197
                    break
                if (char == ">") and (tmp != "<"):
                    answer += 25137
                    break

print(f"Part 1: {answer}")
