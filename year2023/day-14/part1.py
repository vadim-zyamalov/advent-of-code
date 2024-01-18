def transpose(matrix: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(map(lambda x: "".join(x), [*zip(*matrix)]))


def tilt(matrix: tuple[str, ...], direction="E"):
    trans = direction in "NS"
    rev = direction in "NW"

    if trans:
        matrix = transpose(matrix)

    result = ()

    for row in matrix:
        result += (
            "#".join("".join(sorted(chunk, reverse=rev)) for chunk in row.split("#")),
        )

    if trans:
        result = transpose(result)

    return result


def tilt4(matrix: tuple[str, ...]) -> tuple[str, ...]:
    result = matrix
    for d in "NWSE":
        result = tilt(result, d)
    return result


def loads(matrix: tuple[str, ...]) -> int:
    N = len(matrix)
    result = 0

    for i, row in enumerate(matrix):
        result += row.count("O") * (N - i)
    return result


def spin(matrix: tuple[str, ...], N: int) -> tuple[str, ...]:
    result = matrix
    cache = {result: 0}
    i = 1

    while i <= N:
        result = tilt4(result)
        if result not in cache:
            cache[result] = i
        else:
            cycle = i - cache[result]
            idx = cache[result] + (N - cache[result]) % cycle
            for k, v in cache.items():
                if v == idx:
                    return k

        i += 1

    return result


def dump(matrix: list[str]) -> None:
    for row in matrix:
        print(row)
    print()


if __name__ in "__main__":
    with open("_inputs/2023/day-14/input.txt", "r", encoding="utf8") as f:
        matrix: tuple[str, ...] = tuple(f.read().strip().split("\n"))

    result = tilt(matrix, "N")

    res1 = loads(result)

    print(f"Part 1: {res1}")

    result = spin(matrix, 1_000_000_000)

    res2 = loads(result)

    print(f"Part 2: {res2}")
