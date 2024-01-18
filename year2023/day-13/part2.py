def transpose(matrix: list[str]) -> list[str]:
    return list(map(lambda x: "".join(x), list(zip(*matrix))))


def check(row: str, idx: int, N: int) -> int:
    if idx < (N // 2):
        lb, ub = 0, idx * 2 + 1
    else:
        lb, ub = (idx + 1) - (N - (idx + 1)), N - 1

    return sum(1 for el1, el2 in zip(row[lb : idx + 1], row[ub:idx:-1]) if el1 != el2)


def reflection(matrix: list[str]) -> tuple[list[int], ...]:
    N = len(matrix[0])

    result_eq = []
    result_sm = []

    for i in range(0, N - 1):
        smudges = sum(check(row, i, N) for row in matrix)
        if smudges == 0:
            result_eq.append(i + 1)
        if smudges == 1:
            result_sm.append(i + 1)

    return result_eq, result_sm


def reflections(matrix: list[str]) -> tuple[list[int], ...]:
    return *reflection(matrix), *reflection(transpose(matrix))


if __name__ == "__main__":
    res1 = 0
    res2 = 0
    with open("_inputs/2023/day-13/input.txt", "r", encoding="utf8") as f:
        contents = f.read()

        for chunk in contents.split("\n\n"):
            if chunk == "":
                break

            current = chunk.split("\n")

            vr, svr, hr, shr = reflections(current)

            for v in vr:
                res1 += v
            for v in hr:
                res1 += 100 * v

            for v in svr:
                res2 += v
            for v in shr:
                res2 += 100 * v

    print(f"Part 1: {res1}")
    print(f"Part 2: {res2}")
