# Summed-area table
# https://en.wikipedia.org/wiki/Summed-area_table


def power(x, y, s):
    rid = x + 10
    power = (rid * y + s) * rid
    power = (power % 1000) // 100 - 5
    return power


def powers(s):
    return [[power(x + 1, y + 1, s) for y in range(300)] for x in range(300)]


def sums(powers):
    result = [[0 for _ in range(301)] for _ in range(301)]
    for x in range(1, 301):
        row_sum = 0
        for y in range(1, 301):
            row_sum += powers[x - 1][y - 1]
            result[x][y] = result[x - 1][y] + row_sum
    return result


def part1(sums, dim=3):
    x, y = 0, 0
    power = -5 * dim * dim

    for _x in range(1, 301 - dim + 1):
        for _y in range(1, 301 - dim + 1):
            _power = (
                sums[_x + dim - 1][_y + dim - 1]
                + sums[_x - 1][_y - 1]
                - sums[_x - 1][_y + dim - 1]
                - sums[_x + dim - 1][_y - 1]
            )
            if _power > power:
                x, y, power = _x, _y, _power
    return x, y, power


def part2(sums):
    x, y = 0, 0
    power = -5 * 300 * 300
    dim = 0

    for _dim in range(1, 301):
        _x, _y, _power = part1(sums, _dim)
        if _power > power:
            x, y, power, dim = _x, _y, _power, _dim

    return x, y, power, dim


if __name__ == "__main__":
    power_matr = powers(7857)
    sums_matr = sums(power_matr)
    x, y, _ = part1(sums_matr)
    print(f"Part 1: {x},{y}")
    x, y, _, dim = part2(sums_matr)
    print(f"Part 2: {x},{y},{dim}")
