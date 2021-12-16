answer = 0

with open("./input.txt", "r") as f:
    while True:
        step = f.read(1)
        if not step:
            break
        elif step == '(':
            answer += 1
        elif step == ')':
            answer -= 1
        else:
            exit(1)

print("Part 1: {}".format(answer))
