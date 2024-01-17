def fuel(mass):
    return (mass // 3) - 2


def uberfuel(mass):
    result = 0
    while (mass := (mass // 3) - 2) > 0:
        result += mass
    return result


if __name__ == "__main__":
    with open("_inputs/2019/day-01/input.txt", "r", encoding="utf8") as f:
        masses = list(map(int, f.read().strip().split("\n")))

    print(f"Part 1: {sum(map(fuel, masses))}")
    print(f"Part 2: {sum(map(uberfuel, masses))}")
