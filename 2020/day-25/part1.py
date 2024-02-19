def get_loop(result, subject=7, q=20201227):
    value = 1
    i = 0
    while value != result:
        i += 1
        value = (value * subject) % q
    return i


def apply(subject, loop, q=20201227):
    value = 1
    for _ in range(loop):
        value = (value * subject) % q
    return value


if __name__ == "__main__":
    with open("_inputs/2020/day-25/input.txt", "r", encoding="utf8") as f:
        numbers = [int(line) for line in f.read().strip().split("\n")]

    loops = [get_loop(num) for num in numbers]

    print(f"Part 1: {apply(numbers[0], loops[1])}")
