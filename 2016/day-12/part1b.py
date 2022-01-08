mult = 14

a = 1
b = 1
c = 0
d = 26
if c != 0:
    d += 7
for _ in range(d):
    a, b = a + b, a
a += mult * 14

print(f"Part 1: {a}")

a = 1
b = 1
c = 1
d = 26
if c != 0:
    d += 7
for _ in range(d):
    a, b = a + b, a
a += mult * 14

print(f"Part 1: {a}")
