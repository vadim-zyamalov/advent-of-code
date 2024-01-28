import sys

sys.path.append(".\\")

from utils.intcode import Intcode

N = 100


def lr(y, computer, pr=(0, 0)):
    l, r = pr

    while True:
        [o], _ = computer.process(inputs=[l, y])
        if o != 0:
            break
        l += 1
        if l > y**2:
            l = 0
            return 0, 0
            break
    r = max(l, r)
    while True:
        [o], _ = computer.process(inputs=[r, y])
        if o == 0:
            break
        r += 1
    return l, r


def is_fitting(lrx, y, n=100):
    y0 = y - n + 1
    _, x01 = lrx[y0]
    x0, _ = lrx[y]
    return (x0 < x01) and (x01 - x0 >= n)


def covered(lrx, n=50):
    result = 0
    for y in range(n):
        x0, x1 = lrx[y]
        if x0 >= n:
            break
        result += min(n, x1) - x0
    return result


if __name__ == "__main__":
    with open("_inputs/2019/day-19/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    computer = Intcode(numbers)

    lrx = {0: lr(0, computer)}
    for y in range(1, N):
        lrx[y] = lr(y, computer, pr=lrx[y - 1])
        if y == 49:
            print(f"Part 1: {covered(lrx)}")

    y = N - 1
    while not is_fitting(lrx, y, N):
        y += 1
        lrx[y] = lr(y, computer, pr=lrx[y - 1])

    x0, _ = lrx[y]
    y0 = y - N + 1

    print(f"Part 2: {10_000 * x0 + y0}")
