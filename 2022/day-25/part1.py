neg = {-2: "=", -1: "-"}

def dec_to_five(number):
    res = ""
    while number:
        number, resid = divmod(number, 5)
        if resid in [0, 1, 2]:
            res = str(resid) + res
        elif resid in [3, 4]:
            number += 1
            resid = resid - 5
            res = neg[resid] + res
    return res


def five_to_dec(number):
    res = 0
    power = 1
    while number:
        cur = number[-1]
        number = number[:-1]
        match cur:
            case "0" | "1" | "2":
                res += int(cur) * power
            case "-":
                res -= power
            case "=":
                res -= 2 * power
        power *= 5
    return res


with open("../../_inputs/2022/day-25/input.txt", "r", encoding="utf8") as f:
    res = 0
    for num in f:
        num = num.strip()
        res += five_to_dec(num)
    print(f"Part 1: {dec_to_five(res)}")
