sx, sy = 0, 0
rx, ry = 0, 0
houses = set()
houses.add((sx, sy))

with open("input.txt", "r", encoding="utf-8") as f:
    while True:
        step = f.read(1)
        match step:
            case "<":
                sx -= 1
            case ">":
                sx += 1
            case "v":
                sy -= 1
            case "^":
                sy += 1
            case _:
                break

        step = f.read(1)
        match step:
            case "<":
                rx -= 1
            case ">":
                rx += 1
            case "v":
                ry -= 1
            case "^":
                ry += 1
            case _:
                break
        houses.add((sx, sy))
        houses.add((rx, ry))

print(f"Part 2: {len(houses)}")
