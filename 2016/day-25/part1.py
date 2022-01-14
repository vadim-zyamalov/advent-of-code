def check(data, pat="01"):
    tmp = pat * (len(data) // 2)
    # print(data, tmp, data == tmp)
    return data == tmp


a = 0
b = 231
c = 11

i = 1
while True:
    res = ""
    a = i + b * c
    while True:
        if a == 0:
            break
        res += str(a % 2)
        a //= 2
    if (len(res) % 2 == 0) and check(res):
        print(f"Part 1: {i}")
        break
    i += 2
    # a = bin(i + b * c)[2:]
    # if check(a, "10"):
    #     print(f"Part 1: {i}")
    #     break
    # i += 1
