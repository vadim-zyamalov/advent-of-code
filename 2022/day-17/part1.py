import time

def top_unit(grid):
    res = 0
    for x, _ in grid:
        res = max(res, x)
    return res


def init_block(i, blocks, grid):
    # x starts from 1! 0 is floor!
    dx, dy = top_unit(grid) + 4, 2
    return [(x + dx, y + dy) for x, y in blocks[i]]


def move_block(block, dir, grid):
    match dir:
        case "<":
            dx, dy = 0, -1
        case ">":
            dx, dy = 0, 1
        case _:
            dx, dy = -1, 0
    tmp_block = [(x + dx, y + dy) for x, y in block]
    if any((x, y) in grid for x, y in tmp_block) or \
       any((y < 0) or (y >= 7) for _, y in tmp_block) or \
       any(x < 1 for x, _ in tmp_block):
        return False
    for i in range(len(block)):
        block[i] = tmp_block[i]
    return True


def cycle(flow, block, grid):
    move_block(block, flow, grid)
    if move_block(block, "", grid):
        return True
    return False


BLOCKS = [
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,1), (1,0), (1,1), (1,2), (2,1)],
    [(0,0), (0,1), (0,2), (1,2), (2,2)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (0,1), (1,0), (1,1)]
]

with open("./input.txt", "r", encoding="utf8") as f:
    FLOWS = f.readline().strip()
    lenFlows = len(FLOWS)

findex = -1
period_ht = 0

STACK = set()
cache = {}

t0 = time.time()
for bn in range(int(1e12)):
    bi = bn % 5
    if bn == 2022:
        print(f"Part 1: {top_unit(STACK)}")
        print(f"  Finished in {time.time() - t0:3.2f} sec.")
    # Block/Flow in cache already
    if (bi, (findex + 1) % lenFlows) in cache:
        # get Block number and Flow index
        BN, H = cache[bi, (findex + 1) % lenFlows]
        # Maybe cycle lenght
        period = bn - BN
        # Maybe cycle height
        period_ht = top_unit(STACK) - H
        # Maybe periods left and modulo for testing
        # the MUST be whole number of cycles left!
        period_no, checker = divmod(int(1e12) - bn, period)
        if not checker:
            print(f"Part 2: {top_unit(STACK) + period_ht * period_no}")
            print(f"  Finished in {time.time() - t0:3.2f} sec.")
            break
    # Keep block and flow index in cache along with number and height
    cache[bi, (findex + 1) % lenFlows] = bn, top_unit(STACK)
    cur_block = init_block(bi, BLOCKS, STACK)
    while True:
        findex = (findex + 1) % lenFlows
        if not cycle(FLOWS[findex], cur_block, STACK):
            STACK |= {(x, y) for x, y in cur_block}
            break
# If there is no cycles
if period_ht == 0:
    print(f"Part 2: {top_unit(STACK)}")
    print(f"  Finished in {time.time() - t0:3.2f} sec.")
