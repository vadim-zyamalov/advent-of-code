def process(group):
    group = group.split("\n")
    answers = set(group[0])
    for el in group[1:]:
        answers |= set(el)
    return len(answers)


def process2(group):
    group = group.split("\n")
    answers = set(group[0])
    for el in group[1:]:
        answers &= set(el)
    return len(answers)


if __name__ == "__main__":
    with open("_inputs/2020/day-06/input.txt", "r", encoding="utf8") as f:
        groups = f.read().strip().split("\n\n")

    print(f"Part 1: {sum(process(gr) for gr in groups)}")
    print(f"Part 2: {sum(process2(gr) for gr in groups)}")
