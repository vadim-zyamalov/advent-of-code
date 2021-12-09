import hashlib

with open("input.txt", "r") as f:
    puzzle = f.read()

puzzle = puzzle.strip()

nonce = 0

while True:
    res = hashlib.md5('{}{}'.format(puzzle,str(nonce)).encode())
    if res.hexdigest().startswith('000000'):
        break
    else:
        nonce += 1

print("Part 2: {}".format(nonce))
