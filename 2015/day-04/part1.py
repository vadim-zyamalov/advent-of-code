import hashlib

with open("input.txt", "r") as f:
    puzzle = f.read()

puzzle = puzzle.strip()

nonce = 0

while True:
    res = hashlib.md5('{}{}'.format(puzzle,str(nonce)).encode())
    if res.hexdigest().startswith('00000'):
        break
    else:
        nonce += 1

print("Part 1: {}".format(nonce))
