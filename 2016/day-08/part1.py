COMMANDS = []
SCREEN = [[0 for _ in range(50)] for _ in range(6)]

def dump():
    for row in SCREEN:
        print("".join(("#" if el == 1 else " ") for el in row))
    print()


def rotate_row(y, by):
    final_by = by % 50
    SCREEN[y] = SCREEN[y][-final_by:] + SCREEN[y][:-final_by]


def rotate_column(x, by):
    final_by = by % 6
    tmp = []
    for i in range(6):
        tmp.append(SCREEN[i][x])
    tmp = tmp[-final_by:] + tmp[:-final_by]
    for i in range(6):
        SCREEN[i][x] = tmp[i]


def process():
    for com, fst, snd in COMMANDS:
        if com == "rect":
            for i in range(snd):
                for j in range(fst):
                    SCREEN[i][j] = 1
        elif com == "column":
            rotate_column(fst, snd)
        elif com == "row":
            rotate_row(fst, snd)


with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        tmp = line.strip().split()
        if tmp[0] == "rect":
            c_num, r_num = (int(el) for el in tmp[1].split("x"))
            COMMANDS.append(("rect", c_num, r_num))
        elif tmp[1] == "column":
            c_num = int(tmp[2].split("=")[1])
            r_num = int(tmp[4])
            COMMANDS.append(("column", c_num, r_num))
        elif tmp[1] == "row":
            c_num = int(tmp[2].split("=")[1])
            r_num = int(tmp[4])
            COMMANDS.append(("row", c_num, r_num))

process()
answer = sum(sum(row) for row in SCREEN)

print(f"Part 1: {answer}")
print("Part 2")
dump()
