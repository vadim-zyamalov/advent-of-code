def search(line):
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(line[7:].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + col


if __name__ == "__main__":
    with open("_inputs/2020/day-05/input.txt", "r", encoding="utf8") as f:
        lines = [search(el) for el in f.read().strip().split("\n")]

    lines.sort()

    print(f"Part 1: {lines[-1]}")

    for i0, i1 in zip(lines[:-1], lines[1:]):
        if abs(i0 - i1) == 2:
            print(f"Part 2: {(i0 + i1) // 2}")
            break
