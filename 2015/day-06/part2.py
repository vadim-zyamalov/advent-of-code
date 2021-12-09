matrix = []
for i in range(1000):
    matrix.append([0] * 1000)

with open("input.txt", "r") as f:
    for line in f:
        command = line.strip().split(' ')

        if len(command) > 4:
            command = command[1:]

        start  = [int(i) for i in command[1].split(',')]
        finish = [int(i) for i in command[3].split(',')]
        action = command[0]

        for i in range(start[0], finish[0] + 1):
            for j in range(start[1], finish[1] + 1):
                if action == 'toggle':
                    matrix[i][j] += 2
                elif action == 'on':
                    matrix[i][j] += 1
                else:
                    matrix[i][j] = max(matrix[i][j] - 1, 0)

print("Part 2: {}".format(sum([sum(i) for i in matrix])))
