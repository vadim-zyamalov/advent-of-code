x, y = 0, 0
houses = set()
houses.add((x, y))

with open("input.txt", "r", encoding="utf-8") as f:
    while True:
        step = f.read(1)
        match step:
            case "<":
                x -= 1
            case ">":
                x += 1
            case "v":
                y -= 1
            case "^":
                y += 1
            case _:
                break
        houses.add((x, y))

print(f"Part 1: {len(houses)}")
