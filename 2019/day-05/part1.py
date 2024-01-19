import sys

sys.path.append(".\\2019\\")

from intcode.intcode import Intcode

if __name__ == "__main__":
    with open("_inputs/2019/day-05/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

        computer = Intcode(numbers)

        output, _ = computer.process(in3=[1], verbose=False)
        print(f"Part 1: {output[-1]}")

        computer.reset()

        output, _ = computer.process(in3=[5], verbose=False)
        print(f"Part 2: {output[-1]}")
