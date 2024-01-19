if __name__ == "__main__":
    res = 0
    with open("_inputs/2018/day-01/input.txt", "r", encoding="utf8") as f:
        for line in f:
            res += int(line.strip())
    print(f"Part 1: {res}")
