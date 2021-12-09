x, y = 0, 0
houses = set()
houses.add((x, y))

with open("input.txt", "r") as f:
    while True:
        step = f.read(1)
        if not step:
            break
        elif step == "^":
            y += 1
        elif step == ">":
            x += 1
        elif step == "v":
            y -= 1
        else:
            x -= 1
        houses.add((x, y))

print("Part 1: {}".format(len(houses)))
