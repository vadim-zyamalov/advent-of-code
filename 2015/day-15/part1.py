from itertools import combinations
import time

ingredients = []


def spoons(n, msp=100):
    for i in combinations(range(msp + n - 1), n - 1):
        i0 = i[0]
        i1 = i[1] - i0 - 1
        i2 = i[2] - i1 - i0 - 2
        i3 = 103 - i2 - i1 - i0 - 3
        yield (i0, i1, i2, i3)


def score1(recipe, ingredients):
    answer = 1
    for ch in range(len(ingredients[0]) - 1):
        res = 0
        for ing, quantity in enumerate(recipe):
            res += quantity * ingredients[ing][ch]
        res = max(0, res)
        answer *= res
    return answer


def score2(recipe, ingredients):
    answer = 1
    for ch in range(len(ingredients[0])):
        res = 0
        for ing, quantity in enumerate(recipe):
            res += quantity * ingredients[ing][ch]
        res = max(0, res)
        if ch < 4:
            answer *= res
        else:
            if res != 500:
                return 0
    return answer


with open("_inputs/2015/day-15/input.txt", "r", encoding="utf-8") as f:
    index = 0
    for line in f:
        _, other = line.strip().split(":")
        entries = [int(i.strip().split()[1]) for i in other.strip().split(",")]
        ingredients.append(entries)

t0 = time.time()
answer = 0
for s in spoons(len(ingredients), 100):
    answer = max(score1(s, ingredients), answer)

print(f"Part 1: {answer}")
print(f"elapsed: {time.time() - t0}")

t0 = time.time()
answer = 0
for s in spoons(len(ingredients), 100):
    answer = max(score2(s, ingredients), answer)

print(f"Part 2: {answer}")
print(f"elapsed: {time.time() - t0}")
