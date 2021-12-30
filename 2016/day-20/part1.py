# MIN_IDX = 0
# MAX_IDX = 9

MIN_IDX = 0
MAX_IDX = 4294967295

RANGES = []
coords = [MIN_IDX, MAX_IDX + 1]
status = []

with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        fst, snd = (int(el) for el in line.strip().split("-"))
        fst, snd = min(fst, snd), max(fst, snd) + 1
        RANGES.append((fst, snd))
        coords.append(fst)
        coords.append(snd)
    coords = list(set(coords))
    coords.sort()

status = [1 for _ in coords]

for fst, snd in RANGES:
    fst_idx = coords.index(fst)
    snd_idx = coords.index(snd)
    for idx in range(fst_idx, snd_idx):
        status[idx] = 0

answer = min(coords[idx]
             for idx in range(len(coords))
             if status[idx] == 1)
print(f"Part 1: {answer}")

answer: int = 0
for idx in range(len(coords) - 1):
    if status[idx] == 1:
        answer += coords[idx + 1] - coords[idx]
print(f"Part 2: {answer}")
