fishes = [0 for _ in range(0, 9)]


def step(fishes):
    res = fishes.copy()
    tmp = res[0]
    res[:-1] = res[1:]
    res[8] =  tmp
    res[6] += tmp
    return res

with open("input.txt", "r") as f:
    tmp = [int(i) for i in f.readline().strip().split(',')]

for i in tmp:
    fishes[i] += 1

for i in range(256):
    fishes = step(fishes)

print(sum(fishes))
