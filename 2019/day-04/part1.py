def check(password, func):
    password = str(password)
    if len(password) != 6 or any(
        c0 > c1 for c0, c1 in zip(password[:-1], password[1:])
    ):
        return False
    n_digits = [password.count(ch) for ch in set(password)]
    return any(func(n) for n in n_digits)


if __name__ == "__main__":
    with open("_inputs/2019/day-04/input.txt", "r", encoding="utf8") as f:
        lower, upper = tuple(map(int, f.read().strip().split("-")))
    print(
        f"Part 1: {sum(check(p, lambda x: x >= 2) for p in range(lower, upper+1))}"
    )
    print(
        f"Part 2: {sum(check(p, lambda x: x == 2) for p in range(lower, upper+1))}"
    )
