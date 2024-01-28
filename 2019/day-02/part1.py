import sys

sys.path.append(".\\")

from utils.intcode import Intcode


if __name__ == "__main__":
    with open("_inputs/2019/day-02/input.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            numbers = [v for v in map(int, line.strip().split(","))]

            computer = Intcode(numbers)
            computer.regs[1], computer.regs[2] = 12, 2
            computer.process()
            print(f"Part 1: {computer._regs[0]}")

            for i in range(100):
                for j in range(100):
                    computer.reset()
                    computer.regs[1], computer.regs[2] = i, j
                    computer.process()
                    if computer._regs[0] == 19690720:
                        print(f"Part 2: {100 * i + j}")
                        exit()
