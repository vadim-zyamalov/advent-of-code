x = 0
y = 0

with open("input.txt", "r") as f:
    for i in f:
        com, _, val = i.strip().partition(' ')
        if com == 'forward':
            x += int(val)
        elif com == 'down':
            y += int(val)
        elif com == 'up':
            y -= int(val)
        else:
            exit(1)
print(x * y)
