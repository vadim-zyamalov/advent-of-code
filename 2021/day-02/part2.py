import sys

x = 0
y = 0
aim = 0

with open("input.txt", "r") as f:
    for i in f:
        com, _, val = i.strip().partition(' ')
        match com:
            case 'forward':
                x += int(val)
                y += aim * int(val)
            case 'down':
                aim += int(val)
            case 'up':
                aim -= int(val)
            case _:
                sys.exit(1)

print(f"Part 2: {x * y}")
