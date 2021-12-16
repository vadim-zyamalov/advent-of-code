with open("./input.txt", "r") as f:
    stack = []
    answer = 0
    for line in f:
        for char in line.strip():
            if char in '([{<':
                stack.append(char)
            else:
                tmp = stack.pop()
                if (char == ')') and (tmp != '('):
                    answer += 3
                    break
                if (char == ']') and (tmp != '['):
                    answer += 57
                    break
                if (char == '}') and (tmp != '{'):
                    answer += 1197
                    break
                if (char == '>') and (tmp != '<'):
                    answer += 25137
                    break

print("Part 1: {}".format(answer))
