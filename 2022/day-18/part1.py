import sys
sys.setrecursionlimit(3000)

MOVES = [(-1, 0, 0),
         (1, 0, 0),
         (0, -1, 0),
         (0, 1, 0),
         (0, 0, -1),
         (0, 0, 1)]


def count_external(pos: tuple, blocks: list[tuple], bounds: tuple):
    res = 0
    minx, maxx, miny, maxy, minz, maxz = bounds

    nx_pos = []

    for dx, dy, dz in MOVES:
        mb_pos = (pos[0] + dx, pos[1] + dy, pos[2] + dz)
        if not ((minx <= mb_pos[0] <= maxx) and \
                (miny <= mb_pos[1] <= maxy) and \
                (minz <= mb_pos[2] <= maxz)):
            continue
        if mb_pos in visited:
            continue
        elif mb_pos in blocks:
            res += 1
        else:
            nx_pos.append(mb_pos)
            visited.add(mb_pos)

    if nx_pos:
        for mb_pos in nx_pos:
            res += count_external(mb_pos, blocks, bounds)
    return res



blocks = []
visited = set()
minx, maxx = float("inf"), float("-inf")
miny, maxy = float("inf"), float("-inf")
minz, maxz = float("inf"), float("-inf")

with open("../../_inputs/2022/day-18/input.txt", "r", encoding="utf8") as f:
    for line in f:
        cur_block = tuple(int(x) for x in line.strip().split(","))
        blocks.append(cur_block)
        minx, maxx = min(minx, cur_block[0]), max(maxx, cur_block[0])
        miny, maxy = min(miny, cur_block[1]), max(maxy, cur_block[1])
        minz, maxz = min(minz, cur_block[2]), max(maxz, cur_block[2])

minx, miny, minz = minx - 1, miny - 1, minz - 1
maxx, maxy, maxz = maxx + 1, maxy + 1, maxz + 1

res = len(blocks) * 6
for i in range(len(blocks) - 1):
    for j in range(i+1, len(blocks)):
        if abs(blocks[i][0] - blocks[j][0]) + \
           abs(blocks[i][1] - blocks[j][1]) + \
           abs(blocks[i][2] - blocks[j][2]) == 1:
            res -= 2

print(f"Part 1: {res}")

res = count_external((minx, miny, minz),
                     blocks,
                     (minx, maxx, miny, maxy, minz, maxz))

print(f"Part 2: {res}")
