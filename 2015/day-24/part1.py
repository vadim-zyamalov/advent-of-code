from itertools import combinations

presents = []


def permute_presents_4(presents, start=1):
    goal_weight = sum(presents) // 4
    max_group = len(presents) // 4
    assert goal_weight * 4 == sum(presents)
    stop_gr0 = False
    for i in range(start, max_group + 1):
        for gr0 in combinations(presents, i):
            if sum(gr0) != goal_weight:
                continue
            tmp_presents = [p for p in presents if p not in gr0]
            for _ in permute_presents_3(tmp_presents):
                stop_gr0 = True
                yield gr0
                break
        if stop_gr0:
            break


def permute_presents_3(presents, start=1):
    goal_weight = sum(presents) // 3
    max_group = len(presents) // 3
    assert goal_weight * 3 == sum(presents)
    stop_gr0 = False
    for i in range(start, max_group + 1):
        for gr0 in combinations(presents, i):
            if sum(gr0) != goal_weight:
                continue
            tmp_presents = [p for p in presents if p not in gr0]
            for j in range(len(gr0), len(tmp_presents) // 2 + 1):
                stop_gr1 = False
                for gr1 in combinations(tmp_presents, j):
                    if sum(gr1) == goal_weight:
                        stop_gr0 = True
                        stop_gr1 = True
                        yield gr0
                        break
                if stop_gr1:
                    break
        if stop_gr0:
            break


def qe(presents):
    result = 1
    for p in presents:
        result *= p
    return result


with open("input.txt", "r") as f:
    for line in f:
        if line.strip() == '':
            continue
        presents.append(int(line.strip()))
        presents.sort(reverse=True)

variants = []
for i in permute_presents_3(presents):
    variants.append(qe(i))

print("Part 1: {}".format(min(variants)))

variants = []
for i in permute_presents_4(presents):
    variants.append(qe(i))

print("Part 2: {}".format(min(variants)))
