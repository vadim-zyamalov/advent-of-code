import time
import heapq

FAV_NUM = 1358

START = (1, 1)
TARGET = (31, 39)


def is_wall(pos, favourite=FAV_NUM):
    x, y = pos
    tmp_sum = x * x + 3 * x + 2 * x * y + y + y * y + favourite
    return sum(int(el) for el in bin(tmp_sum)[2:]) % 2 == 1


def moves(pos):
    x, y = pos
    result = [(x + 1, y),
              (x, y + 1)]
    if x > 0:
        result.append((x - 1, y))
    if y > 0:
        result.append((x, y - 1))
    return result


queue = []
heapq.heappush(queue, (0, START))

visited = {}

t_0 = time.time()
while queue:
    cur_steps, cur_pos = heapq.heappop(queue)
    if cur_pos == TARGET:
        print(f"Part 1: {cur_steps}")
        print(f"  elapsed in {time.time() - t_0:.2f} seconds")
        break
    if cur_pos in visited and \
            visited[cur_pos] <= cur_steps:
        continue
    visited[cur_pos] = cur_steps
    for variant in moves(cur_pos):
        if is_wall(variant):
            continue
        heapq.heappush(queue, (cur_steps + 1, variant))

print(f"Part 2: {sum(1 for _, v in visited.items() if v <= 50)}")
