from ..intcode.intcode import Intcode

with open("_inputs/2019/day-05/input.txt", "r", encoding="utf8") as f:
    numbers = list(map(int, f.read().strip().split(",")))

    computer = Intcode(numbers)
    computer.process(verbose=False)
