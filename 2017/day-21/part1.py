def rot90(chunk):
    # https://stackoverflow.com/questions/42519/how-do-you-rotate-a-two-dimensional-array/24356420#24356420
    # kind of magic!
    # *chunk splits list of lists into separate lists
    # zip forms tuples of 1st, 2nd, etc. elements of *chunk
    # list makes list of tuples (effectively transpose)
    # reversed reverse row order
    return list(reversed(list(zip(*chunk))))


def rotate(chunk, n=0):
    if n == 0:
        return chunk
    tmp = chunk
    for _ in range(n):
        tmp = rot90(tmp)
    return tmp


def flip(chunk):
    return [list(el) for el in map(reversed, chunk)]


def hstack(chunk1, chunk2):
    if chunk1 == []:
        return chunk2
    return [r1 + r2 for r1, r2 in zip(chunk1, chunk2)]


def vstack(chunk1, chunk2):
    if chunk1 == []:
        return chunk2
    return chunk1 + chunk2


def binval(chunk):
    num = "0b"
    for r in chunk:
        for el in r:
            num += "1" if el == "#" else "0"
    return int(num, 2)


def getchunk(image, i, j, s):
    return [r[j : j + s] for r in image[i : i + s]]


def dump(image):
    for r in image:
        print("".join(r))
    print()


def step(image, rules2, rules3):
    N = len(image)
    result = []
    if N % 2 == 0:
        nc = N // 2
        s = 2
        for i in range(nc):
            row = []
            for j in range(nc):
                tmp = binval(getchunk(image, i * s, j * s, s))
                row = hstack(row, rules2[tmp])
            result = vstack(result, row)
    elif N % 3 == 0:
        nc = N // 3
        s = 3
        for i in range(nc):
            row = []
            for j in range(nc):
                tmp = binval(getchunk(image, i * s, j * s, s))
                row = hstack(row, rules3[tmp])
            result = vstack(result, row)
    return result


def part1(image, rules2, rules3, n=5):
    result = [r.copy() for r in image]
    for _ in range(n):
        result = step(result, rules2, rules3)
        # dump(result)
    total = sum(1 if el == "#" else 0 for row in result for el in row)
    print(f"Part 1/2: {total}")


if __name__ == "__main__":
    image = []
    with open("../../_inputs/2017/day-21/start.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            image.append(list(line))

    rules2 = {}
    rules3 = {}
    with open("../../_inputs/2017/day-21/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            tmp = line.split(" => ")
            tmp_from = [list(el) for el in tmp[0].split("/")]
            tmp_to = [list(el) for el in tmp[1].split("/")]
            rule = set()
            for i in range(4):
                rule.add(binval(rotate(tmp_from, i)))
                rule.add(binval(rotate(flip(tmp_from), i)))
            for k in rule:
                if len(tmp_from) == 2:
                    rules2[k] = tmp_to
                else:
                    rules3[k] = tmp_to

    part1(image, rules2, rules3, n=5)
    part1(image, rules2, rules3, n=18)
