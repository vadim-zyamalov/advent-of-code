with open("input.txt", "r", encoding="utf-8") as f:
    crabs = [int(i) for i in f.readline().strip().split(',')]

answer = None
for i in range(min(crabs), max(crabs) + 1):
    tmp = sum(abs(c - i) for c in crabs)
    answer = tmp if not answer or (tmp < answer) else answer

print(f"Part 1: {answer}")

answer = None
for i in range(min(crabs), max(crabs) + 1):
    tmp = sum(abs(c - i) * (abs(c - i) + 1) / 2 for c in crabs)
    answer = tmp if not answer or (tmp < answer) else answer

print(f"Part 2: {answer}")
