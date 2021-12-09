with open("input.txt", "r") as f:
    crabs = [int(i) for i in f.readline().strip().split(',')]

ans = None
for i in range(min(crabs), max(crabs) + 1):
    tmp = sum(abs(c - i) for c in crabs)
    ans = tmp if not ans or (tmp < ans) else ans

print("Part 1: {}".format(ans))
