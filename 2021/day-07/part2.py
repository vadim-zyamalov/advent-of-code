with open("input.txt", "r") as f:
    crabs = [int(i) for i in f.readline().strip().split(',')]

ans = None
for i in range(min(crabs), max(crabs) + 1):
    tmp = sum(abs(c - i) * (abs(c - i) + 1) / 2 for c in crabs)
    ans = tmp if not ans or (tmp < ans) else ans

print(int(ans))
