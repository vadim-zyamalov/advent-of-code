matrix = []
for i in range(1000):
    matrix.append([0] * 1000)

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        command = line.strip().split(' ')

        if len(command) > 4:
            command = command[1:]

        start = [int(i) for i in command[1].split(',')]
        finish = [int(i) for i in command[3].split(',')]
        action = command[0]

        for i in range(start[0], finish[0] + 1):
            for j in range(start[1], finish[1] + 1):
                match action:
                    case 'toggle':
                        matrix[i][j] = (matrix[i][j] + 1) % 2
                    case 'on':
                        matrix[i][j] = 1
                    case _:
                        matrix[i][j] = 0

print(f"Part 1: {sum([sum(i) for i in matrix])}")
