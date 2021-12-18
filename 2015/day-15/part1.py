# from itertools import product
import time

ingredients = []


def self_product(data, repeat=2):
    n = len(data)
    counter = [0 for _ in range(repeat)]
    while not all(i == (n - 1) for i in counter):
        position = repeat - 1
        while True:
            counter[position] = (counter[position] + 1) % n
            if counter[position] == 0:
                position -= 1
            else:
                break
        yield [data[i] for i in counter]


def spoons_correct(n, msp=100):
    for i in self_product(list(range(0, msp + 1)), repeat=n):
        if sum(i) != 100:
            continue
        yield i


def score(recipe, ingredients):
    answer = 1
    for ch in range(len(ingredients[0])):
        res = 0
        for ing, quantity in enumerate(recipe):
            res += quantity * ingredients[ing][ch]
        res = max(0, res)
        answer *= res
    return answer


t0 = time.time()
with open("input.txt", "r", encoding="utf-8") as f:
    index = 0
    for line in f:
        _, _, other = line.strip().partition(':')
        entries = [int(i.strip().split()[1])
                   for i in other.strip().split(',')][:-1]
        ingredients.append(entries)

answer = 0
for s in spoons_correct(len(ingredients), 100):
    tmp = score(s, ingredients)
    answer = tmp if answer < tmp else answer

print(f"Part 1: {answer}")
print(f'elapsed: {time.time() - t0}')
