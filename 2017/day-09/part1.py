def process_str(input_str):
    total_score = 0

    group_lvl = 0
    in_garbage = False
    garbage_count = 0

    str_len = len(input_str)
    pos = 0

    while pos < str_len:
        match input_str[pos]:
            case "{":
                if not in_garbage:
                    group_lvl += 1
                    total_score += group_lvl
                else:
                    garbage_count += 1
            case "}":
                if not in_garbage:
                    group_lvl -= 1
                else:
                    garbage_count += 1
            case "<":
                if not in_garbage:
                    in_garbage = True
                else:
                    garbage_count += 1
            case ">":
                in_garbage = False
            case "!":
                pos += 1
            case _:
                if in_garbage:
                    garbage_count += 1
        pos += 1
    return total_score, garbage_count


with open("../../_inputs/2017/day-09/input.txt", "r", encoding="utf-8") as f:
    step = 0
    for line in f:
        r1, r2 = process_str(line.strip())
        print(f"{step:3}. Part 1: {r1}")
        print(f"{step:3}. Part 2: {r2}")
        step += 1
