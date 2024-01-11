r5 = 0

seen = set()
last = r5

i = 0
while True:
    r3 = r5 | 65536
    r5 = 9010242

    while r3 > 0:
        r1 = r3 & 255
        r5 += r1
        r5 &= 16777215
        r5 *= 65899
        r5 &= 16777215

        r3 = r3 // 256

    if i == 0:
        print(f"Part 1: {r5}")
        i += 1

    if r5 not in seen:
        seen.add(r5)
        last = r5
    else:
        print(f"Part 2: {last}")
        break
