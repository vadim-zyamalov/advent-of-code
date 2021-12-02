floor = 0
ans = 0

with open("input.txt", "r") as f:
    while True:
        step = f.read(1)
        if not step:
            break
        elif step == '(':
            floor += 1
            ans += 1
        elif step == ')':
            floor -= 1
            ans += 1
        else:
            exit(1)
        if floor < 0:
            break

print(ans)

