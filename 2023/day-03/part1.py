def check_symb(
    i: int, j: int, scheme: list[list]
) -> tuple[bool, tuple[int, int] | None]:
    N, M = len(scheme), len(scheme[0])

    for di in range(-1, 2):
        for dj in range(-1, 2):
            if (di, dj) == (0, 0):
                continue
            elif not (0 <= i + di < N) or not (0 <= j + dj < M):
                continue
            elif scheme[i + di][j + dj] not in ".0123456789":
                if scheme[i + di][j + dj] == "*":
                    return True, (i + di, j + dj)
                return True, None
    return False, None


def parse_numbers(scheme: list[list]) -> tuple[list[int], dict]:
    N, M = len(scheme), len(scheme[0])
    acc = ""
    ispart = False
    gear = None

    parts = []
    gears = {}

    for i in range(N):
        for j in range(M):
            if scheme[i][j] in "0123456789":
                acc += scheme[i][j]
                if not ispart:
                    ispart, gear = check_symb(i, j, scheme)
            elif acc != "":
                if ispart:
                    parts.append(int(acc))
                    ispart = False
                if gear is not None:
                    if gear in gears:
                        gears[gear].append(int(acc))
                    else:
                        gears[gear] = [int(acc)]
                    gear = None
                acc = ""

    if (acc != "") and ispart:
        parts.append(int(acc))
        if gear in gears:
            gears[gear].append(int(acc))
        else:
            gears[gear] = [int(acc)]

    return parts, {k: v for k, v in gears.items() if len(v) == 2}


if __name__ == "__main__":
    scheme = []
    with open("_inputs/2023/day-03/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break

            scheme.append(list(line))

    parts, gears = parse_numbers(scheme)

    print(f"Part 1: {sum(parts)}")

    ratio = sum(gear[0] * gear[1] for gear in gears.values())

    print(f"Part 2: {ratio}")
