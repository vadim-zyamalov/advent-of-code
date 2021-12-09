x = 0
y = 0
aim = 0

with open("input.txt", "r") as f:
    for i in f:
        com, _, val = i.strip().partition(' ')
        if com == 'forward':
            x += int(val)
            y += aim * int(val)
        elif com == 'down':
            aim += int(val)
        elif com == 'up':
            aim -= int(val)
        else:
            exit(1)

print("Part 2: {}".format(x * y))
