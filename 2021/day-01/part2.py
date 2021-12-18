answer = 0
prev = None

a1 = None
a2 = None
a3 = None

with open("input.txt", "r", encoding="utf-8") as f:
    for i in f:
        if not a1:
            a1 = int(i)
        elif not a2:
            a2, a1 = a1, int(i)
        elif not a3:
            a3, a2, a1 = a2, a1, int(i)
            prev = a1 + a2 + a3
        else:
            a3, a2, a1 = a2, a1, int(i)
            if prev and (prev < a1 + a2 + a3):
                answer += 1
            prev = a1 + a2 + a3

print(f"Part 2: {answer}")
