answer = 0

with open("./input.txt", "r", encoding="utf-8") as f:
    while True:
        step = f.read(1)
        match step:
            case "(":
                answer += 1
            case ")":
                answer -= 1
            case _:
                break

print(f"Part 1: {answer}")
