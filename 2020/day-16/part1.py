def gen_fn(bounds):
    return lambda x: any(x0 <= x <= x1 for x0, x1 in zip(bounds[::2], bounds[1::2]))


def parse(chunks):
    rules = {}
    tickets = []
    ticket = ()

    lines = chunks[0].split("\n")

    for line in lines:
        field, rngs = line.split(": ")
        rngs = rngs.split(" or ")
        bnds = ()

        for rng in rngs:
            xs = tuple(sorted(map(int, rng.split("-"))))
            bnds += xs

        rules[field] = gen_fn(bnds)

    lines = chunks[1].split("\n")
    ticket = tuple(map(int, lines[1].split(",")))

    lines = chunks[2].split("\n")
    for line in lines[1:]:
        tickets.append(tuple(map(int, line.split(","))))

    return rules, ticket, tickets


def find_pos(rules, tickets, wrong) -> dict[str, int]:
    _tickets = [el for i, el in enumerate(tickets) if i not in wrong]

    count = {k: set() for k in rules}

    for i, vals in enumerate(zip(*_tickets)):
        for k, f in rules.items():
            if all(f(val) for val in vals):
                count[k].add(i)

    queue = [k for k, v in count.items() if len(v) == 1]
    done = []

    while queue:
        cur = queue.pop(0)
        done.append(cur)

        for k in count:
            if k in done:
                continue
            count[k] -= count[cur]

        queue.extend([k for k, v in count.items() if len(v) == 1 and k not in done])

    return {k: list(v)[0] for k, v in count.items()}


def part1(rules, tickets):
    res = 0
    wrong = set()
    for i, tckt in enumerate(tickets):
        for num in tckt:
            if all(not f(num) for f in rules.values()):
                res += num
                wrong.add(i)
    return res, sorted(wrong)


def part2(rules, ticket, tickets, wrong):
    positions: dict[str, int] = find_pos(rules, tickets, wrong)
    res = 1

    for k, v in positions.items():
        if k.startswith("departure"):
            res *= ticket[v]

    return res


if __name__ == "__main__":
    with open("_inputs/2020/day-16/input.txt", "r", encoding="utf8") as f:
        chunks = f.read().strip().split("\n\n")
    rules, ticket, tickets = parse(chunks)
    res0, wrong = part1(rules, tickets)
    print(f"Part 1: {res0}")
    print(f"Part 2: {part2(rules, ticket, tickets, wrong)}")
