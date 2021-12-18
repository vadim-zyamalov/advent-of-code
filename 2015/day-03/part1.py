x, y = 0, 0
houses = set()
houses.add((x, y))

with open("input.txt", "r", encoding="utf-8") as f:
    while True:
        step = f.read(1)
        if not step:
            break
        if step == "^":
            y += 1
        elif step == ">":
            x += 1
        elif step == "v":
            y -= 1
        else:
            x -= 1
        houses.add((x, y))

print(f"Part 1: {len(houses)}")
