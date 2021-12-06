def generation(fishes):
    res = fishes.copy()
    for i in range(len(res)):
        if res[i] > 0:
            res[i] -= 1
        else:
            res[i] = 6
            res.append(8)
    return res


with open("sample.txt", "r") as f:
    fishes = [int(i) for i in f.readline().strip().split(',')]

for i in range(256):
    fishes = generation(fishes)

print(len(fishes))
