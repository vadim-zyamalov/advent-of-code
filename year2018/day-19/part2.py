r5 = 955
r0 = 0
for r3 in range(1, r5 + 1):
    if r5 % r3 == 0:
        r0 += r3

print(f"Part 1: {r0}")

r5 = 10551355
r0 = 0
for r3 in range(1, r5 + 1):
    if r5 % r3 == 0:
        r0 += r3

print(f"Part 2: {r0}")
