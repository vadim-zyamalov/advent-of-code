from collections import defaultdict
from typing import DefaultDict

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
EMPTY = ((0,) * 5,) * 5


def step(state):
    new_state = ()
    for r in range(5):
        new_row = ()
        for c in range(5):
            checksum = sum(
                state[r + dr][c + dc]
                for dr, dc in DIRS
                if (0 <= r + dr < 5) and (0 <= c + dc < 5)
            )
            if state[r][c] == 1:
                if checksum != 1:
                    new_row += (0,)
                else:
                    new_row += (1,)
            else:
                if checksum in [1, 2]:
                    new_row += (1,)
                else:
                    new_row += (0,)
        new_state += (new_row,)
    return new_state


def step_recursive(states):
    levels = sorted(states.keys())
    if diversity(states[min(levels)]) != 0:
        levels = [min(levels) - 1] + levels
    if diversity(states[max(levels)]) != 0:
        levels = levels + [max(levels) + 1]

    new_states: DefaultDict[int, tuple[tuple[int, ...], ...]] = defaultdict(
        lambda: EMPTY
    )

    for level in levels:
        upper = states[level + 1]
        state = states[level]
        lower = states[level - 1]

        new_state = ()
        for r in range(5):
            new_row = ()
            for c in range(5):
                if (r == 2) and (c == 2):
                    new_row += (0,)
                    continue
                checksum = 0
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    # Граничные случаи
                    # Выходим за внешнюю границу -> переходим на уровень выше
                    if nr == -1:
                        checksum += upper[1][2]
                    elif nr == 5:
                        checksum += upper[3][2]
                    elif nc == -1:
                        checksum += upper[2][1]
                    elif nc == 5:
                        checksum += upper[2][3]

                    # Приходим в центр -Ю переходим на уровнеь ниже
                    elif ((nr, nc) == (2, 2)) and (dr == 1):
                        checksum += sum(lower[0])
                    elif ((nr, nc) == (2, 2)) and (dr == -1):
                        checksum += sum(lower[-1])
                    elif ((nr, nc) == (2, 2)) and (dc == 1):
                        checksum += sum(lower[j][0] for j in range(5))
                    elif ((nr, nc) == (2, 2)) and (dc == -1):
                        checksum += sum(lower[j][-1] for j in range(5))

                    else:
                        checksum += state[nr][nc]

                if state[r][c] == 1:
                    if checksum != 1:
                        new_row += (0,)
                    else:
                        new_row += (1,)
                else:
                    if checksum in [1, 2]:
                        new_row += (1,)
                    else:
                        new_row += (0,)

            new_state += (new_row,)
        new_states[level] = new_state

    levels = sorted(new_states.keys())
    for level in levels:
        if diversity(new_states[level]) != 0:
            break
        del new_states[level]
    for level in levels[::-1]:
        if diversity(new_states[level]) != 0:
            break
        del new_states[level]
    return new_states


def count(states):
    result = 0
    for v in states.values():
        result += sum(sum(row) for row in v)
    return result


def diversity(state):
    res = 0

    for row in state[::-1]:
        for el in row[::-1]:
            res = res * 2 + el

    return res


def dump(state):
    for row in state:
        for el in row:
            print("#" if el == 1 else ".", end="")
        print()


if __name__ == "__main__":
    with open("_inputs/2019/day-24/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n")

    state = tuple(tuple(1 if el == "#" else 0 for el in row) for row in lines)
    cache: dict[int, tuple[tuple[int, ...], ...]] = {diversity(state): state}

    while True:
        state = step(state)
        biodiv = diversity(state)
        if biodiv in cache:
            break
        cache[biodiv] = state

    print(f"Part 1: {biodiv}")

    state = tuple(tuple(1 if el == "#" else 0 for el in row) for row in lines)

    states: DefaultDict[int, tuple[tuple[int, ...], ...]] = defaultdict(
        lambda: EMPTY
    )
    states[0] = state

    for _ in range(200):
        states = step_recursive(states)

    print(f"Part 2: {count(states)}")
