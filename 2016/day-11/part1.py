import time
import heapq
from itertools import combinations


ELEMENTS = {"Th": 1,
            "Pu": 2,
            "Sr": 3,
            "Pr": 4,
            "Rt": 5,
            "El": 6,
            "Di": 7}


def sort_floor(data):
    return tuple(sorted(data))


def remove_from_floor(element, data):
    return sort_floor(
        tuple(el for el in data if el not in element))


def add_to_floor(element, data):
    return sort_floor(data + element)


def replace_in_state(idx, value, data):
    return data[:idx] + (value,) + data[idx+1:]


def check_end(state):
    # The elevator is on the floor 4
    # and all floors but the 4-th are empty
    return (state[0] == 4) and \
        (len(state[1]) == 0) and \
        (len(state[2]) == 0) and \
        (len(state[3]) == 0)


def check_floor(data):
    # Empty is an eligible floor
    # as well as the floor with only chips
    # and the floor with generatore only
    if not data or \
       ((data[0] < 0) and (data[-1] < 0)) or \
       ((data[0] > 0) and (data[-1] > 0)):
        return True
    # Otherwise we should have every chip connected
    # to the corresponding generator
    return all(-el in data for el in data if el < 0)


def possible_moves(state):
    result = []
    cur_floor = state[0]
    floor_variants = [cur_floor + d
                      for d in [-1, 1]
                      if 1 <= cur_floor + d <= 4]
    # Move one or two elements
    moves = list(combinations(state[cur_floor], r=1)) + \
        list(combinations(state[cur_floor], r=2))
    for move in moves:
        tmp_cur_floor = remove_from_floor(move, state[cur_floor])
        if not check_floor(tmp_cur_floor):
            continue
        for next_floor in floor_variants:
            tmp_next_floor = add_to_floor(move, state[next_floor])
            if not check_floor(tmp_next_floor):
                continue
            next_state = replace_in_state(0, next_floor, state)
            next_state = replace_in_state(cur_floor, tmp_cur_floor, next_state)
            next_state = replace_in_state(next_floor, tmp_next_floor, next_state)
            result.append(next_state)
    return result


def encode_state(state):
    return (state[0],
            sort_floor(tuple(-ELEMENTS[el[:-1]]
                             if el[-1] == "M"
                             else ELEMENTS[el[:-1]]
                             for el in state[1])),
            sort_floor(tuple(-ELEMENTS[el[:-1]]
                             if el[-1] == "M"
                             else ELEMENTS[el[:-1]]
                             for el in state[2])),
            sort_floor(tuple(-ELEMENTS[el[:-1]]
                             if el[-1] == "M"
                             else ELEMENTS[el[:-1]]
                             for el in state[3])),
            sort_floor(tuple(-ELEMENTS[el[:-1]]
                             if el[-1] == "M"
                             else ELEMENTS[el[:-1]]
                             for el in state[4])))


START = encode_state(
    (1,
     ("ThG", "ThM", "PuG", "SrG"),
     ("PuM", "SrM"),
     ("PrG", "PrM", "RtG", "RtM"),
     ()))

visited = {}
queue = [(0, (START, 0))]

t_0 = time.time()
while queue:
    cur_element = heapq.heappop(queue)
    st = cur_element[1][0]
    steps = cur_element[1][1]
    if check_end(st):
        t_1 = time.time() - t_0
        print(f"Part 1: {steps}")
        print(f"  elapsed in {int(t_1) // 60} min {t_1 % 60:.2f} sec")
        break
    if st in visited and (visited[st] <= steps):
        continue
    visited[st] = steps
    next_moves = possible_moves(st)
    for nxt in next_moves:
        heapq.heappush(queue, (steps + 1 - 10 * len(nxt[4]), (nxt, steps + 1)))

START = encode_state(
    (1,
     ("ThG", "ThM", "PuG", "SrG", "ElG", "ElM", "DiG", "DiM"),
     ("PuM", "SrM"),
     ("PrG", "PrM", "RtG", "RtM"),
     ()))

visited = {}
queue = [(0, (START, 0))]

t_0 = time.time()
while queue:
    cur_element = heapq.heappop(queue)
    st = cur_element[1][0]
    steps = cur_element[1][1]
    if check_end(st):
        t_1 = time.time() - t_0
        print(f"Part 2: {steps}")
        print(f"  elapsed in {int(t_1) // 60} min {t_1 % 60:.2f} sec")
        break
    if st in visited and (visited[st] <= steps):
        continue
    visited[st] = steps
    next_moves = possible_moves(st)
    for nxt in next_moves:
        heapq.heappush(queue, (steps + 1 - 10 * len(nxt[4]), (nxt, steps + 1)))
