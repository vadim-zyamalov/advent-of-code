import sys

x = 0
y = 0

with open("input.txt", "r") as f:
    for i in f:
        com, _, val = i.strip().partition(' ')
        match com:
            case 'forward':
                x += int(val)
            case 'down':
                y += int(val)
            case 'up':
                y -= int(val)
            case _:
                sys.exit(1)

print(f"Part 1: {x * y}")
