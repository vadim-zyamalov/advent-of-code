from functools import cache


def check(password, func):
    password = str(password)
    if len(password) != 6 or any(
        c0 > c1 for c0, c1 in zip(password[:-1], password[1:])
    ):
        return False
    n_digits = [password.count(ch) for ch in set(password)]
    return any(func(n) for n in n_digits)


@cache
def fact(n):
    if n <= 0:
        return 1
    return n * fact(n - 1)


def b(n, k):
    if (k == 0) and (n != 0):
        return 0
    if (n == 0) and (k != 0):
        return 1
    if (n == 0) and (k == 0):
        return 1
    return fact(n + k - 1) // (fact(k - 1) * fact(n))


def part2(digits=6, gr=2, lower=0, upper=9, fst=False):
    result = 0

    for i in range(digits - (gr - 1)):
        for d in range(lower, upper + 1):
            dl, dr = d - lower, upper - d
            ld, rd = i, digits - gr - i
            nl = b(ld, dl)
            nr = b(rd, dr)
            result += nl * nr
    return result


if __name__ == "__main__":
    with open("_inputs/2019/day-04/input.txt", "r", encoding="utf8") as f:
        lower, upper = tuple(map(int, f.read().strip().split("-")))
    print(
        f"Part 1: {sum(check(p, lambda x: x >= 2) for p in range(lower, upper+1))}"
    )
    print(
        f"Part 2: {sum(check(p, lambda x: x == 2) for p in range(lower, upper+1))}"
    )
