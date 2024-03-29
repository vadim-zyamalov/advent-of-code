import sys

sys.path.append(".\\")

from utils.intcode import Intcode


def to_string(output):
    return str("".join(map(chr, output)))


if __name__ == "__main__":
    with open("_inputs/2019/day-21/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    inputs = [
        "NOT C T\n",
        "OR T J\n",
        "NOT B T\n",
        "OR T J\n",
        "NOT A T\n",
        "OR T J\n",
        "AND D J\n",
        "WALK\n",
    ]

    inputs2 = [
        "NOT H T\n",
        "OR T J\n",
        "AND I J\n",
        "AND E J\n",
        "OR H J\n",
        "NOT C T\n",
        "AND T J\n",
        "NOT B T\n",
        "OR T J\n",
        "NOT A T\n",
        "OR T J\n",
        "AND D J\n",
        "RUN\n",
    ]

    # inputs = [list(map(ord, list(inp))) for inp in inputs]
    # inputs2 = [list(map(ord, list(inp))) for inp in inputs2]

    computer = Intcode(numbers, ascii=True)
    computer.start(inputs=[])

    for inp in inputs:
        output = computer.resume(inputs=inp)

    print(output.ascii)
    print(f"Part 1: {output.rest[-1]}")

    computer.start(inputs=[])

    for inp in inputs2:
        output = computer.resume(inputs=inp)

    print(output.ascii)
    print(f"Part 2: {output.rest[-1]}")
