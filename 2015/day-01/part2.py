floor = 0
answer = 0

with open("./input.txt", "r", encoding="utf-8") as f:
    while True:
        step = f.read(1)
        match step:
            case "(":
                floor += 1
                answer += 1
            case ")":
                floor -= 1
                answer += 1
            case _:
                break
        if floor < 0:
            break

print(f"Part 2: {answer}")
