def process(positions):
    idx = 0

    while positions[idx] != 99:
        i0, i1, i2 = [positions[idx + i] for i in [1, 2, 3]]
        match positions[idx]:
            case 1:
                positions[i2] = positions[i0] + positions[i1]
            case 2:
                positions[i2] = positions[i0] * positions[i1]
            case _:
                assert False
        idx += 4


if __name__ == "__main__":
    with open("_inputs/2019/day-02/input.txt", "r", encoding="utf8") as f:
        for line in f.readlines():
            numbers = [v for v in map(int, line.strip().split(","))]

            _numbers = numbers.copy()

            numbers[1], numbers[2] = 12, 2
            process(numbers)
            print(f"Part 1: {numbers[0]}")

            for i in range(100):
                for j in range(100):
                    numbers = _numbers.copy()
                    numbers[1], numbers[2] = i, j
                    process(numbers)
                    if numbers[0] == 19690720:
                        print(f"Part 2: {100 * i + j}")
                        exit()
