import sys
import heapq as hq

sys.path.append(".\\")

from utils.intcode import Intcode
from utils.pos import Pos


DIRS = {1: Pos(-1, 0), 2: Pos(1, 0), 3: Pos(0, -1), 4: Pos(0, 1)}


def path(computer):
    beg = Pos(0, 0)
    queue = [(0, beg, *computer.save())]
    seen = set()

    while queue:
        dd, pos, regs, ip, rbase = hq.heappop(queue)
        if pos in seen:
            continue
        seen.add(pos)
        for i, dpos in DIRS.items():
            computer.load(regs, ip, rbase)
            [output], _ = computer.process(inputs=[i], resume=True)
            if output == 0:
                continue
            if output == 2:
                return dd + 1, pos + dpos, *computer.save()
            hq.heappush(queue, (dd + 1, pos + dpos, *computer.save()))


def fill(computer, pos, regs, ip, rbase):
    filled = set()
    filled.add(pos)
    minutes = 0

    stack = [(pos, regs, ip, rbase)]

    while True:
        new_stack = []

        for _pos, _regs, _ip, _rbase in stack:
            for i, dpos in DIRS.items():
                if _pos + dpos in filled:
                    continue
                computer.load(_regs, _ip, _rbase)
                [output], _ = computer.process(inputs=[i], resume=True)
                if output == 0:
                    continue
                filled.add(_pos + dpos)
                new_stack.append((_pos + dpos, *computer.save()))

        if new_stack == []:
            return minutes
        stack = new_stack
        minutes += 1


if __name__ == "__main__":
    with open("_inputs/2019/day-15/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    computer = Intcode(numbers)
    computer.process(inputs=[])
    dd, pos, regs, ip, rbase = path(computer)
    print(f"Part 1: {dd}")

    fill_time = fill(computer, pos, *computer.save())
    print(f"Part 2: {fill_time}")
