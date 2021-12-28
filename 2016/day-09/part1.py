def parse(data):
    result = ""
    i = 0
    while i < len(data):
        if data[i] == "(":
            i += 1
            inner = ""
            while data[i] != ")":
                inner += data[i]
                i += 1
            num, times = (int(el) for el in inner.split("x"))
            i += 1
            inner = data[i:i+num]
            result += inner * times
            i += num
        elif data[i] == " ":
            i += 1
        else:
            result += data[i]
            i += 1
    return result


def decompress(data):
    result = 0
    i = 0
    while i < len(data):
        if data[i] == "(":
            i += 1
            inner = ""
            while data[i] != ")":
                inner += data[i]
                i += 1
            num, times = (int(el) for el in inner.split("x"))
            i += 1
            inner = data[i:i+num]
            result += decompress(inner) * times
            i += num
        elif data[i] == " ":
            i += 1
        else:
            result += 1
            i += 1
    return result


with open("./input.txt", "r", encoding="utf-8") as f:
    INPUT = f.readline().strip()

print(f"Part 1: {len(parse(INPUT))}")
print(f"Part 2: {decompress(INPUT)}")
