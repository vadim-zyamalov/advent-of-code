from collections import Counter

DIMS = (3, 2)


def check(data, dims=DIMS):
    N = len(data)
    L = dims[0] * dims[1]

    assert N % L == 0

    min_zeros = N
    onetwo_prod = 0

    for i in range(0, N, L):
        res = Counter(data[i : i + L])
        if res["0"] < min_zeros:
            min_zeros = res["0"]
            onetwo_prod = res["1"] * res["2"]

    return onetwo_prod


def decode(data, dims=DIMS):
    N = len(data)
    L = dims[0] * dims[1]

    assert N % L == 0

    image = list(data[:L])

    for l in range(L, N, L):
        layer = data[l : l + L]

        for p, pxl in enumerate(layer):
            if image[p] != "2":
                continue
            if pxl == "2":
                continue
            image[p] = pxl

    for r in range(0, L, dims[0]):
        for pxl in image[r : r + dims[0]]:
            match pxl:
                case "2":
                    print(" ", end="")
                case "1":
                    print("#", end="")
                case "0":
                    print(".", end="")
        print()


if __name__ == "__main__":
    with open("_inputs/2019/day-08/input.txt", "r", encoding="utf8") as f:
        data = f.read().strip()

    print(f"Part 1: {check(data, dims=(25, 6))}")
    print(f"Part 2:\n{decode(data, dims=(25, 6))}")
