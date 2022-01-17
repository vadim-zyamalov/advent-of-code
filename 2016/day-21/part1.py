# INPUT = "abcde"
INPUT = "abcdefgh"

# INPUT2 = "decab"
INPUT2 = "fbgdceah"

COMMANDS = []

BREVERSE = {0: 1,
            1: 1,
            2: 6,
            3: 2,
            4: 7,
            5: 3,
            6: 0,
            7: 4}


def pswap_str(pos_0, pos_1, data):
    return data[:pos_0] + \
        data[pos_1] + \
        data[pos_0+1:pos_1] + \
        data[pos_0] + \
        data[pos_1+1:]


def lswap_str(letter_0, letter_1, data):
    pos_0, pos_1 = data.index(letter_0), data.index(letter_1)
    pos_0, pos_1 = min(pos_0, pos_1), max(pos_0, pos_1)
    return pswap_str(pos_0, pos_1, data)


def rrotate_str(steps, data):
    steps %= len(data)
    return data[-steps:] + data[:-steps]


def lrotate_str(steps, data):
    steps %= len(data)
    return data[steps:] + data[:steps]


def brotate_str(letter, data):
    steps = data.index(letter)
    if steps >= 4:
        steps += 1
    steps += 1
    steps %= len(data)
    return rrotate_str(steps, data)


def rev_brotate_str(letter, data):
    idx = data.index(letter)
    steps = BREVERSE[idx]
    return lrotate_str(steps, data)


def reverse_str(pos_0, pos_1, data):
    if pos_0 != 0:
        return data[:pos_0] + \
            data[pos_1:pos_0-1:-1] + \
            data[pos_1+1:]
    return data[:pos_0] + \
        data[pos_1::-1] + \
        data[pos_1+1:]


def move_str(pos_0, pos_1, data):
    letter = data[pos_0]
    tmp_data = data[:pos_0] + data[pos_0+1:]
    return tmp_data[:pos_1] + \
        letter + \
        tmp_data[pos_1:]


with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        tmp = line.strip().split()
        match tmp[0]:
            case "swap":
                if tmp[1] == "position":
                    fst, snd = int(tmp[2]), int(tmp[5])
                    fst, snd = min(fst, snd), max(fst, snd)
                    COMMANDS.append(("pswap", fst, snd))
                else:
                    COMMANDS.append(("lswap", tmp[2], tmp[5]))
            case "rotate":
                if tmp[1] == "right":
                    COMMANDS.append(("rrotate", int(tmp[2])))
                elif tmp[1] == "left":
                    COMMANDS.append(("lrotate", int(tmp[2])))
                else:
                    COMMANDS.append(("brotate", tmp[6]))
            case "reverse":
                fst, snd = int(tmp[2]), int(tmp[4])
                fst, snd = min(fst, snd), max(fst, snd)
                COMMANDS.append(("reverse", fst, snd))
            case "move":
                COMMANDS.append(("move", int(tmp[2]), int(tmp[5])))

answer = INPUT
for cmd in COMMANDS:
    match cmd[0]:
        case "pswap":
            answer = pswap_str(cmd[1], cmd[2], answer)
        case "lswap":
            answer = lswap_str(cmd[1], cmd[2], answer)
        case "rrotate":
            answer = rrotate_str(cmd[1], answer)
        case "lrotate":
            answer = lrotate_str(cmd[1], answer)
        case "brotate":
            answer = brotate_str(cmd[1], answer)
        case "reverse":
            answer = reverse_str(cmd[1], cmd[2], answer)
        case "move":
            answer = move_str(cmd[1], cmd[2], answer)
    # print(cmd, "=>", answer)

print(f"Part 1: {answer}")

answer = INPUT2
for cmd in reversed(COMMANDS):
    match cmd[0]:
        case "pswap":
            answer = pswap_str(cmd[1], cmd[2], answer)
        case "lswap":
            answer = lswap_str(cmd[1], cmd[2], answer)
        case "rrotate":
            answer = lrotate_str(cmd[1], answer)
        case "lrotate":
            answer = rrotate_str(cmd[1], answer)
        case "brotate":
            answer = rev_brotate_str(cmd[1], answer)
        case "reverse":
            answer = reverse_str(cmd[1], cmd[2], answer)
        case "move":
            answer = move_str(cmd[2], cmd[1], answer)
    # print(cmd, "=>", answer)

print(f"Part 1: {answer}")
