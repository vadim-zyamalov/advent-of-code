from functools import cache
from itertools import cycle, accumulate
import time


@cache
def ranges(n, pos):
    _pos = pos + 1
    p_idx = tuple(
        i - 1
        for i in range(1, n + 1)
        if i % (4 * _pos) in range(_pos, 2 * _pos)
    )
    n_idx = tuple(
        i - 1
        for i in range(1, n + 1)
        if i % (4 * _pos) in range(3 * _pos, 4 * _pos)
    )
    return p_idx, n_idx


def phase1_ranges(digits):
    new_number = []

    for i in range(len(digits)):
        p_idx, n_idx = ranges(len(digits), i)
        new_number.append(
            abs(sum(digits[i] for i in p_idx) - sum(digits[i] for i in n_idx))
            % 10
        )

    return new_number


def phase2(digits):
    new_number = []
    total = sum(digits)
    for i in range(len(digits)):
        if i == 0:
            new_number.append(abs(total) % 10)
        else:
            total -= digits[i - 1]
            new_number.append(abs(total) % 10)
    return new_number


def phase2_iter(digits, offset):
    cycle_number = cycle(reversed(digits))
    N = 10_000 * len(digits) - offset
    number = [next(cycle_number) for _ in range(N)]
    for _ in range(100):
        number = [el % 10 for el in accumulate(number)]

    return "".join(map(str, number[-1:-9:-1]))


if __name__ == "__main__":
    with open("_inputs/2019/day-16/input.txt", "r", encoding="utf8") as f:
        line = f.read().strip()
        offset = int(line[:7])

    t0 = time.time()
    digits = list(map(int, list(line)))

    for _ in range(100):
        digits = phase1_ranges(digits)
    result = "".join(map(str, digits[:8]))
    print(f"Part 1: {result}")
    print(f"    took {time.time() - t0:.2f} secs")

    t0 = time.time()
    digits = list(map(int, list(line)))
    nreps, nsurp = divmod(10_000 * len(digits) - offset, len(digits))
    digits = digits[-nsurp:] + digits * nreps

    for _ in range(100):
        digits = phase2(digits)
    result = "".join(map(str, digits[:8]))
    print(f"Part 2: {result}")
    print(f"    took {time.time() - t0:.2f} secs")

    t0 = time.time()
    digits = list(map(int, list(line)))
    print(f"Part 2: {phase2_iter(digits, offset)} (iter)")
    print(f"    took {time.time() - t0:.2f} secs")
