from itertools import product
# from math import sqrt
# import heapq


# def neighbors(pos, limits):
#     result = []
#     for dx, dy in [(-1, 0),
#                    (1, 0),
#                    (0, -1),
#                    (0, 1)]:
#         if (0 <= pos[0] + dx <= limits[0]) and \
#            (0 <= pos[1] + dy <= limits[1]):
#             result.append((pos[0] + dx, pos[1] + dy))
#     return result


# def state_replace(pos, val, state):
#     tmp_row = state[pos[0]][:pos[1]] + \
#         (val,) + \
#         state[pos[0]][pos[1]+1:]
#     return state[:pos[0]] + \
#         (tmp_row,) + \
#         state[pos[0]+1:]


# def move(pos, dest, state):
#     tmp_pos = (state[pos[0]][pos[1]][0],
#                0,
#                state[pos[0]][pos[1]][0])
#     tmp_dest = (state[dest[0]][dest[1]][0],
#                 state[dest[0]][dest[1]][1] + state[pos[0]][pos[1]][1],
#                 state[dest[0]][dest[1]][2] - state[pos[0]][pos[1]][1])
#     return state_replace(dest, tmp_dest,
#                          state_replace(pos, tmp_pos, state))


# def potential_moves(pos, state):
#     if state[pos[0]][pos[1]][1] == 0:
#         return []
#     result = []
#     lim_x, lim_y = len(state)-1, len(state[0])-1
#     for x, y in neighbors(pos, (lim_x, lim_y)):
#         if state[pos[0]][pos[1]][1] <= state[x][y][2]:
#             result.append(((x, y), move(pos, (x, y), state)))
#     return result


# def distance(point_0, point_1):
#     return int(sqrt(
#         (point_0[0] + point_1[0]) ** 2 + \
#         (point_0[1] + point_1[1]) ** 2
#     ))


NODES = {}

with open("./input.txt", "r", encoding="utf-8") as f:
    max_x = -1
    max_y = -1
    for line in f:
        if line.strip() == "":
            continue
        if not line.startswith("/dev/"):
            continue
        tmp = line.strip().split()
        tmp_node = tmp[0].split("/")[3].split("-")
        tmp_x = int(tmp_node[1][1:])
        tmp_y = int(tmp_node[2][1:])
        if tmp_x not in NODES:
            NODES[tmp_x] = {}
        NODES[tmp_x][tmp_y] = (int(tmp[1][:-1]),
                               int(tmp[2][:-1]),
                               int(tmp[3][:-1]))
        max_x = max(max_x, tmp_x)
        max_y = max(max_y, tmp_y)

GRID = tuple(tuple(el for _, el in row.items()) for _, row in NODES.items())

answer = 0
for x_0, y_0 in product(range(max_x+1), range(max_y+1)):
    for x_1, y_1 in product(range(max_x+1), range(max_y+1)):
        if (x_0 == x_1) and (y_0 == y_1):
            continue
        if GRID[x_0][y_0][1] == 0:
            continue
        if GRID[x_0][y_0][1] > GRID[x_1][y_1][2]:
            continue
        answer += 1

print(f"Part 1: {answer}")

for i in range(len(GRID)):
    for j in range(len(GRID[i])):
        if (i, j) == (max_x, 0):
            print("G", sep="", end="")
        elif (i, j) == (0, 0):
            print("O", sep="", end="")
        elif GRID[i][j][0] > 100:
            print("#", sep="", end="")
        elif GRID[i][j][1] == 0:
            print("_", sep="", end="")
        else:
            print(".", sep="", end="")
    print()
print()


# TARGET = (max_x, 0)

# START = (0, (GRID, TARGET, 0))

# queue = [START]
# answer = 1000000000

# while queue:
#     _, current_state = heapq.heappop(queue)
#     current_grid, current_target, current_steps = current_state
#     if current_target == (0, 0):
#         answer = min(answer, current_steps)
#         break
#     for x, y in product(range(max_x, -1, -1), range(max_y+1)):
#         tmp = potential_moves((x, y), current_grid)
#         for new_target, new_grid in tmp:
#             if (x, y) == current_target:
#                 heapq.heappush(queue,
#                                (current_steps + 1,
#                                 (new_grid, new_target, current_steps + 1)))
#             else:
#                 heapq.heappush(queue,
#                                (current_steps + 1 + 3 * distance(current_target, (x, y)),
#                                 (new_grid, current_target, current_steps + 1)))

# print(f"Part 2: {answer}")
