with open("./input.txt", "r", encoding="utf-8") as f:
    answer = []
    for line in f:
        stack = []
        lineOk = True
        for char in line.strip():
            if char in '([{<':
                stack.append(char)
            else:
                tmp = stack.pop()
                if (char == ')') and (tmp != '('):
                    lineOk = False
                if (char == ']') and (tmp != '['):
                    lineOk = False
                if (char == '}') and (tmp != '{'):
                    lineOk = False
                if (char == '>') and (tmp != '<'):
                    lineOk = False
        if not lineOk:
            continue
        result = 0
        while len(stack) > 0:
            tmp = stack.pop()
            result *= 5
            if tmp == '(':
                result += 1
            if tmp == '[':
                result += 2
            if tmp == '{':
                result += 3
            if tmp == '<':
                result += 4
        answer.append(result)

answer.sort()
print(f"Part 2: {answer[len(answer) // 2]}")
