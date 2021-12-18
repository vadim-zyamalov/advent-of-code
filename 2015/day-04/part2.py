import hashlib

with open("input.txt", "r", encoding="utf-8") as f:
    puzzle = f.read()

puzzle = puzzle.strip()

nonce = 0

while True:
    res = hashlib.md5(f'{puzzle}{str(nonce)}'.encode())
    if res.hexdigest().startswith('000000'):
        break
    else:
        nonce += 1

print(f"Part 2: {nonce}")
