from itertools import islice
from collections import deque
from typing import Deque


def play(d0: Deque, d1: Deque):
    while d0 and d1:
        c0, c1 = d0.popleft(), d1.popleft()

        if c0 > c1:
            d0.extend([c0, c1])
        else:
            d1.extend([c1, c0])

    if d0:
        d0.reverse()
        return sum(d * (m + 1) for m, d in enumerate(d0))
    d1.reverse()
    return sum(d * (m + 1) for m, d in enumerate(d1))


def play_recursive(d0: Deque, d1: Deque):
    dcache = []
    while d0 and d1:
        c_val = (tuple(d0), tuple(d1))
        if c_val in dcache:
            d0.reverse()
            return 0, sum(d * (m + 1) for m, d in enumerate(d0))
        dcache.append(c_val)

        c0, c1 = d0.popleft(), d1.popleft()
        if (c0 <= len(d0)) and (c1 <= len(d1)):
            winner, _ = play_recursive(
                deque(islice(d0, 0, c0)), deque(islice(d1, 0, c1))
            )
        else:
            winner = 0 if (c0 > c1) else 1

        if winner == 0:
            d0.extend([c0, c1])
        else:
            d1.extend([c1, c0])

    if d0:
        d0.reverse()
        return 0, sum(d * (m + 1) for m, d in enumerate(d0))
    d1.reverse()
    return 1, sum(d * (m + 1) for m, d in enumerate(d1))


if __name__ == "__main__":
    with open("_inputs/2020/day-22/input.txt", "r", encoding="utf8") as f:
        chunks = f.read().strip().split("\n\n")

    deck0 = deque([int(i) for i in chunks[0].strip().split("\n")[1:]])
    deck1 = deque([int(i) for i in chunks[1].strip().split("\n")[1:]])

    print(f"Part 1: {play(deck0.copy(), deck1.copy())}")
    print(f"Part 2: {play_recursive(deck0.copy(), deck1.copy())}")
