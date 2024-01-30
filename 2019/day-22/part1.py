from collections import deque


N = (10007, 119315717514047)
REPS = 101741582076661


def reverse_rules(seq, N):
    a, b = 1, 0

    for op, n in seq[::-1]:
        match op:
            case "new":
                a, b = -a % N, (N - b - 1) % N
            case "cut":
                b = (b + n) % N
            case "inc":
                z = pow(n, -1, N)
                a = (a * z) % N
                b = (b * z) % N
    return a, b


def pow_polinome(a, b, P, N):
    if P == 1:
        return a, b
    if P % 2 == 0:
        return pow_polinome((a * a) % N, (a * b + b) % N, P // 2, N)
    else:
        c, d = pow_polinome(a, b, P - 1, N)
        return (a * c) % N, (a * d + b) % N


def pow_polinome2(a, b, P, N):
    return pow(a, P, N), ((a**P - 1) / (a - 1)) % N


def shuffle(rules, N):
    deck = deque(range(N))

    for op, n in rules:
        match op:
            case "new":
                deck.reverse()
            case "cut":
                deck.rotate(-n)
            case "inc":
                i = 0
                _deck = [0] * N
                for d in deck:
                    _deck[i] = d
                    i += n
                    i %= N
                deck = deque(_deck)

    print(f"Part 1: {deck.index(2019)}")


if __name__ == "__main__":
    seq = []
    with open("_inputs/2019/day-22/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            if line.startswith("deal into"):
                seq.append(("new", None))
            elif line.startswith("deal with"):
                seq.append(("inc", int(line.split()[-1])))
            else:
                seq.append(("cut", int(line.split()[-1])))

    shuffle(seq, N[0])

    a, b = reverse_rules(seq, N[1])
    a, b = pow_polinome(a, b, REPS, N[1])

    print(f"Part 2: {(a * 2020 + b) % N[1]}")
