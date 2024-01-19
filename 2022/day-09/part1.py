def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


def far(h, t):
    return (abs(h[0] - t[0]) > 1) or (abs(h[1] - t[1]) > 1)


def step(h, t):
    if far(h, t):
        return (sign(h[0] - t[0]), sign(h[1] - t[1]))
    return (0, 0)


head = (0, 0)
tail = (0, 0)
knots = [head]
for i in range(10):
    knots.append((0, 0))
visited = set()
visited2 = set()

with open("../../_inputs/2022/day-09/input.txt", "r", encoding="utf8") as f:
    for line in f:
        dir, dist = line.strip().split()
        dist = int(dist)

        for s in range(dist):
            match dir:
                case "U":
                    head = (head[0], head[1] + 1)
                case "D":
                    head = (head[0], head[1] - 1)
                case "R":
                    head = (head[0] + 1, head[1])
                case "L":
                    head = (head[0] - 1, head[1])
            knots[0] = head
            dx, dy = step(head, tail)
            tail = (tail[0] + dx, tail[1] + dy)
            visited.add(tail)
            for i in range(1, 10):
                dx, dy = step(knots[i - 1], knots[i])
                knots[i] = (knots[i][0] + dx, knots[i][1] + dy)
            visited2.add(knots[9])

print(f"Part 1: {len(visited)}")
print(f"Part 2: {len(visited2)}")
