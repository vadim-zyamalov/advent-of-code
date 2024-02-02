SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
BEG = (0, 0)


def count(pattern, beg=BEG, part1=1):
    nx, ny = len(pattern), len(pattern[0])
    result = 1

    for i, (dy, dx) in enumerate(SLOPES):
        x, y = beg
        slope_result = 0

        while x < nx:
            if pattern[x][y] == "#":
                slope_result += 1
            x = x + dx
            y = (y + dy) % ny

        if i == part1:
            yield slope_result

        result *= slope_result

    yield result


if __name__ == "__main__":
    with open("_inputs/2020/day-03/input.txt", "r", encoding="utf8") as f:
        pattern = tuple(f.read().strip("\n").split("\n"))

    result = count(pattern)
    print(f"Part 1: {next(result)}")
    print(f"Part 2: {next(result)}")
