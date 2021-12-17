target = {}

with open("input.txt", "r") as f:
    tmp = f.readline().strip().split(": ")
    tmp = tmp[1].split(", ")
    tmp_x = tmp[0][2:].split("..")
    tmp_y = tmp[1][2:].split("..")
    target['x'] = (int(tmp_x[0]), int(tmp_x[1]))
    target['y'] = (int(tmp_y[0]), int(tmp_y[1]))

v_y_max = max(abs(target['y'][0]), abs(target['y'][1]))
if v_y_max == abs(target['y'][0]):
    v_y_max -= 1

print("Part 1: {}".format(v_y_max * (v_y_max + 1) / 2))

v_y_max = max(abs(target['y'][0]), abs(target['y'][1]))

possible_v_x = {}
for v in range(1, target['x'][1] + 1):
    n = 1
    while (0 <= v - (n - 1)) and ((v - (n - 1) / 2) * n <= target['x'][1]):
        if (v - (n - 1) / 2) * n >= target['x'][0]:
            if v not in possible_v_x:
                possible_v_x[v] = []
            possible_v_x[v].append(n)
        n += 1

possible_v_y = {}
for v in range(-v_y_max, v_y_max + 1):
    n = 1
    while (v - (n - 1) / 2) * n >= target['y'][0]:
        if (v - (n - 1) / 2) * n <= target['y'][1]:
            if v not in possible_v_y:
                possible_v_y[v] = []
            possible_v_y[v].append(n)
        n += 1

answer = 0
for v_x in possible_v_x:
    for v_y in possible_v_y:
        tmp = set(possible_v_x[v_x]) & set(possible_v_y[v_y])
        if len(tmp) > 0:
            answer += 1
        elif (max(possible_v_x[v_x]) < min(possible_v_y[v_y])) and \
             (v_x - (max(possible_v_x[v_x]) - 1) == 0):
            answer += 1
print("Part 2: {}".format(answer))

# Bruteforce :)
answer = 0
for speed_x in range(1, target['x'][1] + 1):
    for speed_y in range(-v_y_max, v_y_max + 1):
        x, y = 0, 0
        vx = speed_x
        vy = speed_y

        while (x <= target['x'][1]) and \
              (y >= target['y'][0]):
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            vy -= 1
            if (target['x'][0] <= x <= target['x'][1]) and \
               (target['y'][0] <= y <= target['y'][1]):
                answer += 1
                break
print("Part 2: {}".format(answer))
