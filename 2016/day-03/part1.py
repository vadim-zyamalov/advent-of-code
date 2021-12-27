answer = 0

with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        a, b, c = (int(el) for el in line.strip().split())
        if (a + b > c) and (b + c > a) and (c + a > b):
            answer += 1

print(f"Part 1: {answer}")

answer = 0
with open("./input.txt", "r", encoding="utf-8") as f:
    for line_a, line_b, line_c in zip(f, f, f):
        a_0, a_1, a_2 = (int(el) for el in line_a.strip().split())
        b_0, b_1, b_2 = (int(el) for el in line_b.strip().split())
        c_0, c_1, c_2 = (int(el) for el in line_c.strip().split())
        if (a_0 + b_0 > c_0) and (b_0 + c_0 > a_0) and (c_0 + a_0 > b_0):
            answer += 1
        if (a_1 + b_1 > c_1) and (b_1 + c_1 > a_1) and (c_1 + a_1 > b_1):
            answer += 1
        if (a_2 + b_2 > c_2) and (b_2 + c_2 > a_2) and (c_2 + a_2 > b_2):
            answer += 1

print(f"Part 2: {answer}")
