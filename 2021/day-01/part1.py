prev = None
answer = 0

with open("../../_inputs/2021/day-01/input.txt", "r", encoding="utf-8") as f:
    for i in f:
        if prev and (prev < int(i)):
            answer += 1
        prev = int(i)

print(f"Part 1: {answer}")
