import sys
import heapq as hq

sys.path.append(".\\")

from utils.intcode import Intcode, State
from utils.pos import Pos


DIRS = {1: Pos(-1, 0), 2: Pos(1, 0), 3: Pos(0, -1), 4: Pos(0, 1)}


def path(computer):
    beg = Pos(0, 0)
    bstate = computer.save()
    queue: list[tuple[int, Pos, State]] = [(0, beg, bstate)]
    seen = set()

    while queue:
        dd, pos, state = hq.heappop(queue)
        if pos in seen:
            continue
        seen.add(pos)
        for i, dpos in DIRS.items():
            computer.load(state)
            [output], _, _, _ = computer.process(inputs=[i])
            if output == 0:
                continue
            if output == 2:
                return dd + 1, pos + dpos, computer.save()
            hq.heappush(queue, (dd + 1, pos + dpos, computer.save()))
    return 0, beg, bstate


def fill(computer, pos, state):
    filled = set()
    filled.add(pos)
    minutes = 0

    stack = [(pos, state)]

    while True:
        new_stack = []

        for _pos, _state in stack:
            for i, dpos in DIRS.items():
                if _pos + dpos in filled:
                    continue
                computer.load(_state)
                [output], _, _, _ = computer.process(inputs=[i])
                if output == 0:
                    continue
                filled.add(_pos + dpos)
                new_stack.append((_pos + dpos, computer.save()))

        if new_stack == []:
            return minutes
        stack = new_stack
        minutes += 1


if __name__ == "__main__":
    with open("_inputs/2019/day-15/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    computer = Intcode(numbers)
    computer.start(inputs=[])
    dd, pos, state = path(computer)
    print(f"Part 1: {dd}")

    fill_time = fill(computer, pos, state)
    print(f"Part 2: {fill_time}")
