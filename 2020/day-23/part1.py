from collections import deque
from typing import Deque


def step(cups: Deque):
    N = len(cups)

    cur = cups[0]
    cups.rotate(-1)
    moving = (cups.popleft(), cups.popleft(), cups.popleft())

    dest = (cur - 1) % N
    dest = N if dest == 0 else dest
    while dest in moving:
        dest = (dest - 1) % N
        dest = N if dest == 0 else dest

    idx = cups.index(dest)

    cups.rotate(-idx - 1)
    cups.extendleft(moving[::-1])

    idx = (cups.index(cur) + 1) % N

    cups.rotate(-idx)


def get_p1(cups):
    idx = cups.index(1)
    cups.rotate(-idx)
    cups.popleft()
    return "".join(map(str, cups))


def get_p2(cups):
    idx = cups.index(1)
    cups.rotate(-idx - 1)
    return cups.popleft() * cups.popleft()


if __name__ == "__main__":
    with open("_inputs/2020/day-23/sample.txt", "r", encoding="utf8") as f:
        _cups = deque(list(int(d) for d in f.read().strip()))

    cups = _cups.copy()
    for _ in range(100):
        step(cups)
    print(f"Part 1: {get_p1(cups)}")

    cups = _cups.copy()
    N = len(cups)
    cups.extend(range(N + 1, 1_000_001))
    for _ in range(10_000_000):
        step(cups)

    print(f"Part 2: {get_p2(cups)}")
