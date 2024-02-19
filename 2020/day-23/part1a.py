def shuffle(cups, steps=100):
    dcups = {k: v for k, v in zip(cups, cups[1:] + cups[:1])}
    N = max(cups)

    current = cups[0]
    for _ in range(steps):
        moving = [dcups[current]]
        moving.append(dcups[moving[-1]])
        moving.append(dcups[moving[-1]])

        destination = current - 1
        destination = destination if destination > 0 else N
        while destination in moving:
            destination = destination - 1
            destination = destination if destination > 0 else N

        dcups[current] = dcups[moving[-1]]
        dcups[moving[-1]] = dcups[destination]
        dcups[destination] = moving[0]
        current = dcups[current]

    return dcups


def get_p1(dcups):
    result = ""
    cur = 1

    while True:
        if dcups[cur] == 1:
            break
        result += str(dcups[cur])
        cur = dcups[cur]

    return result


def get_p2(dcups):
    n1 = dcups[1]
    n2 = dcups[n1]
    return n1 * n2


if __name__ == "__main__":
    with open("_inputs/2020/day-23/input.txt", "r", encoding="utf8") as f:
        _cups = list(int(d) for d in f.read().strip())

    cups = _cups.copy()
    dcups = shuffle(cups, 100)
    print(f"Part 1: {get_p1(dcups)}")

    cups = _cups.copy()
    N = len(cups)
    cups.extend(range(N + 1, 1_000_001))
    dcups = shuffle(cups, 10_000_000)

    print(f"Part 2: {get_p2(dcups)}")
