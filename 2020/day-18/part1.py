from collections import defaultdict


def solve(line, advanced=False):
    tokens = line.replace("(", "( ").replace(")", " )").split()

    op = None
    ops = []
    level = 0

    stack = defaultdict(list)

    for token in tokens:
        match token:
            case d if d.isdecimal():
                match op:
                    case "+":
                        stack[level].append(stack[level].pop() + int(d))
                    case "*":
                        if not advanced:
                            stack[level].append(stack[level].pop() * int(d))
                        else:
                            stack[level].append(int(d))
                    case _:
                        stack[level].append(int(d))

            case o if o in "+*":
                op = o

            case "(":
                level += 1
                ops.append(op)
                op = None

            case ")":
                res = 1
                while stack[level]:
                    res *= stack[level].pop()

                level -= 1
                op = ops.pop()

                match op:
                    case "+":
                        stack[level].append(res + stack[level].pop())
                    case "*":
                        if not advanced:
                            stack[level].append(res * stack[level].pop())
                        else:
                            stack[level].append(res)
                    case _:
                        stack[level].append(res)

    res = 1
    for d in stack[0]:
        res *= d
    return res


if __name__ == "__main__":
    with open("_inputs/2020/day-18/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n")

    res = sum(solve(line) for line in lines)
    print(f"Part 1: {res}")
    res = sum(solve(line, True) for line in lines)
    print(f"Part 1: {res}")
