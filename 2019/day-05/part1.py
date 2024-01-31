import sys

sys.path.append(".\\")

from utils.intcode import Intcode

if __name__ == "__main__":
    with open("_inputs/2019/day-05/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

        computer = Intcode(numbers)

        output = computer.start(inputs=[1])
        print(f"Part 1: {output.list[-1]}")

        # computer.reset()

        output = computer.start(inputs=[5])
        print(f"Part 2: {output.list[-1]}")
