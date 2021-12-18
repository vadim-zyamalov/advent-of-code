sx, sy = 0, 0
rx, ry = 0, 0
houses = set()
houses.add((sx, sy))

with open("input.txt", "r", encoding="utf-8") as f:
    while True:
        step = f.read(1)
        if not step:
            break
        if step == "^":
            sy += 1
        elif step == ">":
            sx += 1
        elif step == "v":
            sy -= 1
        else:
            sx -= 1

        step = f.read(1)
        if not step:
            break
        if step == "^":
            ry += 1
        elif step == ">":
            rx += 1
        elif step == "v":
            ry -= 1
        else:
            rx -= 1
        houses.add((sx, sy))
        houses.add((rx, ry))

print(f"Part 2: {len(houses)}")
