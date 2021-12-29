def naive_step(a):
    b = "".join("1" if el == "0" else "0" for el in a[::-1])
    return a + "0" + b


def checksum(data):
    cur = data
    while len(cur) % 2 == 0:
        tmp_cur = ""
        for i in range(0, len(cur), 2):
            tmp_cur += str(int(cur[i] == cur[i + 1]))
        cur = tmp_cur
    return cur


with open("./input.txt", "r", encoding="utf-8") as f:
    START = f.readline().strip()

# Part 1
TARGET = 272
cur = START
while len(cur) < TARGET:
    cur = naive_step(cur)

answer = checksum(cur[:TARGET])
print(f"Part 1: {answer}")

# Part 2
TARGET = 35651584
cur = START
while len(cur) < TARGET:
    cur = naive_step(cur)

answer = checksum(cur[:TARGET])
print(f"Part 2: {answer}")
