with open("./input.txt", "r", encoding="utf-8") as f:
    number = f.readline().strip()

answer = 0
for i, digit in enumerate(number):
    next_i = (i + 1) % len(number)
    if digit == number[next_i]:
        answer += int(digit)

print(f"Part 1: {answer}")

answer = 0
for i, digit in enumerate(number):
    next_i = (i + len(number) // 2) % len(number)
    if digit == number[next_i]:
        answer += int(digit)

print(f"Part 2: {answer}")
