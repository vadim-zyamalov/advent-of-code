import time

COST = {"A": 1,
        "B": 10,
        "C": 100,
        "D": 1000}
ROOMS = {"A": 2,
         "B": 4,
         "C": 6,
         "D": 8}
ROOMS_IDX = {"A": 1,
             "B": 2,
             "C": 3,
             "D": 4}


def dump(state, length=2):
    print()
    print('#' * (len(state[0]) + 2), sep="")
    print("#", "".join(state[0]), "#", sep="")
    for i in range(length - 1, -1, -1):
        px = "  "
        if i == length - 1:
            px = "##"
        print(px, "#", state[1][i] if len(state[1]) > i else ".",
              "#",   state[2][i] if len(state[2]) > i else ".",
              "#",   state[3][i] if len(state[3]) > i else ".",
              "#",   state[4][i] if len(state[4]) > i else ".",
              "#", px, sep="")
    print("  ", "#" * 9, "  ", sep="")


def tuple_pop(data):
    if data == ():
        return None, ()
    return data[-1], data[:-1]


def tuple_push(new_val, data, right=True):
    if right:
        return data + (new_val,)
    return (new_val,) + data


def tuple_replace(new_val, pos, data):
    assert -1 < pos < len(data)
    return data[:pos] + (new_val,) + data[pos+1:]


def check_room(room, state):
    tmp_room = state[ROOMS_IDX[room]]
    return (len(tmp_room) == 0) or all(el == room for el in tmp_room)


def check_path(pos_0, pos_2, state):
    fst, snd = min(pos_0, pos_2), max(pos_0, pos_2)
    return all(el == "." for el in state[0][fst+1:snd])


def check_winner(state):
    res_hall = all(el == "." for el in state[0])
    res_rooms = all(check_room(room, state) for room in ROOMS)
    return res_hall and res_rooms


def possible_moves(state, length=2):
    # Go to rooms first
    for hall_pos, hall_el in enumerate(state[0]):
        if hall_el == ".":
            continue
        if check_room(hall_el, state) and \
           check_path(hall_pos, ROOMS[hall_el], state):
            new_state = state
            new_state = tuple_replace(
                tuple_replace(".", hall_pos, state[0]),
                0,
                new_state)
            new_state = tuple_replace(
                tuple_push(hall_el, state[ROOMS_IDX[hall_el]]),
                ROOMS_IDX[hall_el],
                new_state)
            new_cost = (abs(hall_pos - ROOMS[hall_el]) +
                        (length - len(state[ROOMS_IDX[hall_el]]))) * COST[hall_el]
            yield (new_state, new_cost)
    # Go out of rooms
    for room, room_pos in ROOMS.items():
        if check_room(room, state):
            continue
        for hall_pos, hall_el in enumerate(state[0]):
            if hall_el != ".":
                continue
            if hall_pos in ROOMS.values():
                continue
            if not check_path(hall_pos, room_pos, state):
                continue
            tmp_el, tmp_room = tuple_pop(state[ROOMS_IDX[room]])
            new_state = state
            new_state = tuple_replace(
                tuple_replace(tmp_el, hall_pos, state[0]),
                0,
                new_state)
            new_state = tuple_replace(
                tmp_room,
                ROOMS_IDX[room],
                new_state)
            new_cost = (abs(hall_pos - room_pos) +
                        (length - len(new_state[ROOMS_IDX[room]]))) * COST[tmp_el]
            yield (new_state, new_cost)

PARTS = [1, 2]
for part in PARTS:
    with open(f"./input{part}.txt", "r", encoding="utf-8") as f:
        tmp_hall = ()
        tmp_rooms = [(), (), (), ()]
        for line in f:
            tmp = line.strip().replace("#", "")
            if tmp == "":
                continue
            if len(tmp) > 4:
                tmp_hall = tuple(list(tmp))
            else:
                for pos, val in enumerate(tmp):
                    tmp_rooms[pos] = tuple_push(val, tmp_rooms[pos], False)


    START = (tmp_hall,) + tuple(tmp_rooms)
    dump(START, length=2 if part == 1 else 4)

    # for s, sm in possible_moves(START):
    #     dump(s)
    #     print(sm)
    #     print()

    queue = [(START, 0)]
    visited = {}
    score = float("inf")

    t0 = time.time()

    while len(queue) > 0:
        q_state, q_sum = queue.pop()
        if check_winner(q_state):
            score = min(score, q_sum)
            continue
        if q_state in visited and \
        (visited[q_state] <= q_sum):
            continue
        visited[q_state] = q_sum
        for loop_state, loop_sum in possible_moves(
                q_state,
                length=2 if part == 1 else 4):
            queue.append((loop_state, q_sum + loop_sum))

    print(f"Part {part}: {score}")
    print(f"Elapsed {time.time() - t0:.2f} seconds")
