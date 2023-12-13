def transpose(matrix: list[list[str]]) -> list[list[str]]:
    return list(map(list, list(zip(*matrix))))


def check(row: list[str], idx: int, N: int) -> bool:
    if idx < (N // 2):
        lb, ub = 0, idx * 2 + 1
    else:
        lb, ub = (idx + 1) - (N - (idx + 1)), N - 1
    return row[lb : idx + 1] == row[ub:idx:-1]


def reflection(matrix: list[list[str]]) -> list[int]:
    N = len(matrix[0])

    result = []

    for i in range(0, N - 1):
        if all(check(row, i, N) for row in matrix):
            result.append(i + 1)

    return result


def reflections(matrix: list[list[str]]) -> tuple[list[int], list[int]]:
    return reflection(matrix), reflection(transpose(matrix))


def smudges(matrix: list[list[str]], vr: list[int], hr: list[int]) -> tuple[int, int]:
    def rev(x):
        return "#" if x == "." else "."

    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            matrix[i][j] = rev(matrix[i][j])

            new_vr, new_hr = reflections(matrix)

            if new_vr:
                for el in new_vr:
                    if el not in vr:
                        return el, 0
            if new_hr:
                for el in new_hr:
                    if el not in hr:
                        return 0, el

            matrix[i][j] = rev(matrix[i][j])

    return 0, 0


if __name__ == "__main__":
    res1 = 0
    res2 = 0
    with open("_inputs/2023/day-13/input.txt", "r", encoding="utf8") as f:
        current = []

        for line in f:
            line = line.strip()

            if line == "":
                vr, hr = reflections(current)

                if vr:
                    res1 += vr[0]
                if hr:
                    res1 += 100 * hr[0]

                vr, hr = smudges(current, vr, hr)
                res2 += vr + 100 * hr

                current = []
            else:
                current.append(list(line))

        if current != []:
            for r in current:
                print(r)
            print()
            vr, hr = reflections(current)
            if vr:
                res1 += vr[0]
            if hr:
                res1 += 100 * hr[0]

            print(vr, hr, end=" ")
            vr, hr = smudges(current, vr, hr)
            res2 += vr + 100 * hr
            print(vr, hr)

    print(f"Part 1: {res1}")
    print(f"Part 2: {res2}")
