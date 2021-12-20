with open("input.txt", "r", encoding="utf-8") as f:
    PATH = f.readline().strip().split(", ")

DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]

pos = (0, 0)
FACE = 0
for step in PATH:
    if step[0] == "R":
        FACE = (FACE + 1) % 4
    else:
        FACE = (FACE - 1) % 4
    pos = (pos[0] + DIR[FACE][0] * int(step[1:]),
           pos[1] + DIR[FACE][1] * int(step[1:]))

print(f"Part 1: {abs(pos[0]) + abs(pos[1])}")

visited = []
pos = (0, 0)
FACE = 0
STOP = False
for step in PATH:
    if step[0] == "R":
        FACE = (FACE + 1) % 4
    else:
        FACE = (FACE - 1) % 4
    for i in range(1, int(step[1:]) + 1):
        pos = (pos[0] + DIR[FACE][0],
               pos[1] + DIR[FACE][1])
        if pos in visited:
            STOP = True
            break
        visited.append(pos)
    if STOP:
        break


print(f"Part 2: {abs(pos[0]) + abs(pos[1])}")
