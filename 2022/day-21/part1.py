import time
import math


def solve_p1(yelled, counting):
    t0 = time.time()
    while len([i for i in counting if i not in yelled]):
        for m in counting:
            if m in yelled:
                continue
            if all(mm in yelled for mm in counting[m]["mm"]):
                op = counting[m]["op"]
                m1, m2 = counting[m]["mm"]
                match op:
                    case "+":
                        yelled[m] = yelled[m1] + yelled[m2]
                    case "-":
                        yelled[m] = yelled[m1] - yelled[m2]
                    case "*":
                        yelled[m] = yelled[m1] * yelled[m2]
                    case "/":
                        yelled[m] = yelled[m1] / yelled[m2]
    print(f"Part 1: {int(yelled['root'])}")
    print(f"  elapsed in {time.time() - t0:3.2f} sec")


def ascend_none(yelled, counting, start):
    yelled[start] = math.nan

    while len([i for i in counting if i not in yelled]) > 1:
        for m in counting:
            if m in yelled:
                continue
            if all(mm in yelled for mm in counting[m]["mm"]) and (m != "root"):
                op = counting[m]["op"]
                m1, m2 = counting[m]["mm"]
                match op:
                    case "+":
                        yelled[m] = yelled[m1] + yelled[m2]
                    case "-":
                        yelled[m] = yelled[m1] - yelled[m2]
                    case "*":
                        yelled[m] = yelled[m1] * yelled[m2]
                    case "/":
                        yelled[m] = yelled[m1] / yelled[m2]
    return yelled


def descend_none(yelled, counting, start, finish, result=0):
    if start == finish:
        return result

    left, right = counting[start]["mm"][0], counting[start]["mm"][1]

    if start == "root":
        if math.isnan(yelled[left]):
            return descend_none(yelled, counting, left, finish, yelled[right])
        return descend_none(yelled, counting, right, finish, yelled[left])

    if math.isnan(yelled[left]):
        match counting[start]["op"]:
            case "+":
                return descend_none(
                    yelled, counting, left, finish, result - yelled[right]
                )
            case "-":
                return descend_none(
                    yelled, counting, left, finish, result + yelled[right]
                )
            case "*":
                return descend_none(
                    yelled, counting, left, finish, result / yelled[right]
                )
            case "/":
                return descend_none(
                    yelled, counting, left, finish, result * yelled[right]
                )
    else:
        match counting[start]["op"]:
            case "+":
                return descend_none(
                    yelled, counting, right, finish, result - yelled[left]
                )
            case "-":
                return descend_none(
                    yelled, counting, right, finish, yelled[left] - result
                )
            case "*":
                return descend_none(
                    yelled, counting, right, finish, result / yelled[left]
                )
            case "/":
                return descend_none(
                    yelled, counting, right, finish, yelled[left] / result
                )


def solve_p2(yelled, counting, start):
    t0 = time.time()
    yelled = ascend_none(yelled, counting, start)
    result = descend_none(yelled, counting, "root", start, 0)
    assert type(result) == str
    print(f"Part 2: {int(result)}")
    print(f"  elapsed in {time.time() - t0:3.2f} sec")


myelled = {}
mmath = {}

with open("_inputs/2022/day-21/input.txt", "r", encoding="utf8") as f:
    for line in f:
        fst, snd = line.strip().split(": ")
        snd = snd.split()
        if len(snd) == 1:
            myelled[fst] = int(snd[0])
        else:
            mmath[fst] = {"op": snd[1], "mm": [snd[0], snd[2]]}

solve_p1(myelled.copy(), mmath)
solve_p2(myelled.copy(), mmath, "humn")
