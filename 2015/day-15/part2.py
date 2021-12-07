from itertools import product

ingredients = []


def spoons_correct(n, msp=100):
    for i in product([i for i in range(0, msp + 1)], repeat=n):
        if sum(i) != 100:
            continue
        yield i


def score(recipe, ingredients):
    ans = 1
    for ch in range(len(ingredients[0])):
        res = 0
        for ing in range(len(recipe)):
            res += recipe[ing] * ingredients[ing][ch]
        if res < 0:
            res = 0
        if ch < 4:
            ans *= res
        else:
            if res != 500:
                return 0
    return ans


with open("input.txt", "r") as f:
    index = 0
    for line in f:
        _, _, other = line.strip().partition(':')
        entries = [int(i.strip().split()[1]) for i in other.strip().split(',')]
        ingredients.append(entries)

ans = 0
for s in spoons_correct(len(ingredients), 100):
    tmp = score(s, ingredients)
    ans = tmp if ans < tmp else ans

print(ans)
