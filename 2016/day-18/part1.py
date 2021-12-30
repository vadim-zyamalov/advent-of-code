TRAPS = ["^^.", ".^^", "^..", "..^"]


def next_row(data):
    result = ""
    safe_tiles = 0
    for idx, _ in enumerate(data):
        if (idx == 0) or (idx == len(data) - 1):
            result += "."
        else:
            if data[idx-1:idx+2] in TRAPS:
                result += "^"
            else:
                result += "."
                safe_tiles += 1
    return (result, safe_tiles)

with open("./input.txt", "r", encoding="utf-8") as f:
    START = f.readline().strip()

answer = sum(1 for el in START if el == ".")
cur = "." + START + "."
for i in range(400000 - 1):
    cur, safe = next_row(cur)
    answer += safe
    if i == 38:
        print(f"Part 1: {answer}")
print(f"Part 2: {answer}")
