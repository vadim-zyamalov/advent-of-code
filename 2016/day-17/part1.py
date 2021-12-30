import hashlib
import heapq
import time


MOVES = {"U": (0, -1),
         "D": (0, 1),
         "L": (-1, 0),
         "R": (1, 0)}


def moves(pos, path, code):
    result = []
    tmp = hashlib.md5(f"{code}{path}".encode()).hexdigest()[:4]
    for i, direction in enumerate(MOVES.keys()):
        new_pos = (pos[0] + MOVES[direction][0],
                   pos[1] + MOVES[direction][1])
        if (0 <= new_pos[0] <= 3) and \
           (0 <= new_pos[1] <= 3) and \
           ("b" <= tmp[i] <= "f"):
            result.append((new_pos, direction))
    return result


with open("./input.txt", "r", encoding="utf-8") as f:
    CODE = f.readline().strip()

START = (0, 0)
TARGET = (3, 3)

queue = []
heapq.heappush(queue, (0, (START, "")))

t_0 = time.time()
while queue:
    cur_priority, cur_state = heapq.heappop(queue)
    cur_pos, cur_path = cur_state
    if cur_pos == TARGET:
        print(f"Part 1: {cur_path}")
        print(f"  elapsed in {time.time() - t_0:.2f} seconds")
        break
    for new_pos, direction in moves(cur_pos, cur_path, CODE):
        heapq.heappush(queue,
                       (cur_priority + 1, (new_pos, cur_path + direction)))

queue = []
heapq.heappush(queue, (0, (START, "")))
length = []

t_0 = time.time()
while queue:
    cur_priority, cur_state = heapq.heappop(queue)
    cur_pos, cur_path = cur_state
    if cur_pos == TARGET:
        length.append(len(cur_path))
        continue
    for new_pos, direction in moves(cur_pos, cur_path, CODE):
        heapq.heappush(queue,
                       (cur_priority - 1, (new_pos, cur_path + direction)))

print(f"Part 2: {max(length)}")
print(f"  elapsed in {time.time() - t_0:.2f} seconds")
