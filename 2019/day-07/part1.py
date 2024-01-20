import sys

sys.path.append(".\\")

from utils.intcode import Intcode
from itertools import permutations


if __name__ == "__main__":
    with open("_inputs/2019/day-07/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    amplifiers = [Intcode(numbers) for _ in range(5)]

    max_signal = 0

    for phases in permutations([0, 1, 2, 3, 4]):
        _input = 0
        for i, phase in enumerate(phases):
            _output, _ = amplifiers[i].process(
                inputs=[phase, _input], verbose=False
            )
            if _output is []:
                assert False
            [_input] = _output
        max_signal = max(max_signal, _input)

        for i in range(5):
            amplifiers[i].reset()

    print(f"Part 1: {max_signal}")

    max_signal = 0

    for phases in permutations([5, 6, 7, 8, 9]):
        _input = 0
        for i, phase in enumerate(phases):
            _output, _ = amplifiers[i].process(inputs=[phase], verbose=False)

        finished = [False] * 5
        while not all(finished):
            for i in range(5):
                _output, _finished = amplifiers[i].process(
                    inputs=[_input], resume=True
                )
                if _output is []:
                    assert False
                [_input] = _output
                finished[i] = _finished

        max_signal = max(max_signal, _input)

        for i in range(5):
            amplifiers[i].reset()

    print(f"Part 2: {max_signal}")
