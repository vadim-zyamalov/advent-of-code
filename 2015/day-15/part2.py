# from itertools import product
import time

ingredients = []


def self_product(data, repeat=2):
    n = len(data)
    counter = [0 for _ in range(repeat)]
    while not all(i == (n - 1) for i in counter):
        pos = repeat - 1
        while True:
            counter[pos] = (counter[pos] + 1) % n
            if counter[pos] == 0:
                pos -= 1
            else:
                break
        yield [data[i] for i in counter]


def spoons_correct(n, msp=100):
    for i in self_product([i for i in range(0, msp + 1)], repeat=n):
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


t0 = time.time()
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

print('{}, elapsed: {}'.format(ans,
                               time.time() - t0))
