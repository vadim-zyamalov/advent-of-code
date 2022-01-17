BUTTONS = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
BUTTONS2 = [[None, None, "1", None, None],
            [None, "2", "3", "4", None],
            ["5", "6", "7", "8", "9"],
            [None, "A", "B", "C", None],
            [None, None, "D", None, None]]

with open("input.txt", "r", encoding="utf-8") as f:
    instructions = []
    for line in f:
        if line.strip() == "":
            continue
        instructions.append(line.strip())

current_pos = [1, 1]
answer = ''
for step in instructions:
    for letter in step:
        match letter:
            case "U":
                if current_pos[0] > 0:
                    current_pos[0] -= 1
            case "D":
                if current_pos[0] < 2:
                    current_pos[0] += 1
            case "L":
                if current_pos[1] > 0:
                    current_pos[1] -= 1
            case "R":
                if current_pos[1] < 2:
                    current_pos[1] += 1
    answer += str(BUTTONS[current_pos[0]][current_pos[1]])

print(f"Part 1: {answer}")

current_pos = [2, 0]
answer = ''
for step in instructions:
    for letter in step:
        match letter:
            case "U":
                if (current_pos[0] > 0) and \
                   BUTTONS2[current_pos[0]-1][current_pos[1]]:
                    current_pos[0] -= 1
            case "D":
                if (current_pos[0] < 4) and \
                   BUTTONS2[current_pos[0]+1][current_pos[1]]:
                    current_pos[0] += 1
            case "L":
                if (current_pos[1] > 0) and \
                   BUTTONS2[current_pos[0]][current_pos[1]-1]:
                    current_pos[1] -= 1
            case "R":
                if (current_pos[1] < 4) and \
                   BUTTONS2[current_pos[0]][current_pos[1]+1]:
                    current_pos[1] += 1
    answer += BUTTONS2[current_pos[0]][current_pos[1]]

print(f"Part 2: {answer}")
