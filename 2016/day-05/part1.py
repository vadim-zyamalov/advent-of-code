import hashlib

with open("./input.txt", "r", encoding="utf-8") as f:
    puzzle = f.readline().strip()

nonce = 0
answer = ''
digit = 0

while digit < 8:
    res = hashlib.md5(f"{puzzle}{nonce}".encode()).hexdigest()
    if res.startswith("00000"):
        print(f"  {digit + 1} symbol retrieved")
        answer += res[5]
        digit += 1
    nonce += 1

print(f"Part 1: {answer}")

nonce = 0
answer = '        '
digit = 0

while digit < 8:
    res = hashlib.md5(f"{puzzle}{nonce}".encode()).hexdigest()
    if res.startswith("00000"):
        if ('0' <= res[5] <= '7'):
            pos = int(res[5])
            sym = res[6]
            if (answer[pos] == ' '):
                print(f"  {digit + 1} symbol retrieved")
                answer = answer[:pos] + sym + answer[pos+1:]
                digit += 1
    nonce += 1

print(f"Part 2: {answer}")
