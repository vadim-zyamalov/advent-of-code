def _hash(line: str) -> int:
    result = 0
    for ch in line:
        result += ord(ch)
        result *= 17
        result %= 256
    return result


def del_lens(boxes: dict[int, list[tuple[str, int]]], box: int, label: str) -> None:
    for lens in boxes[box]:
        if lens[0] == label:
            boxes[box].remove(lens)
            return


def repl_lens(
    boxes: dict[int, list[tuple[str, int]]], box: int, label: str, focal: int
) -> None:
    for i, lens in enumerate(boxes[box]):
        if lens[0] == label:
            boxes[box][i] = (label, focal)
            return
    boxes[box].append((label, focal))


def power_lens(boxes: dict[int, list[tuple[str, int]]]) -> int:
    result = 0
    for box, lenses in boxes.items():
        for i, (_, focal) in enumerate(lenses):
            result += (1 + box) * (1 + i) * focal
    return result


if __name__ == "__main__":
    res1 = 0
    boxes = {k: [] for k in range(256)}

    with open("./_inputs/2023/day-15/input.txt", "r", encoding="utf8") as f:
        for val in f.readline().strip().split(","):
            res1 += _hash(val)

            if (val[-2] == "=") and val[-1].isdigit():
                label, focal = val[:-2], int(val[-1])
                box = _hash(label)
                repl_lens(boxes, box, label, focal)
            elif val[-1] == "-":
                label = val[:-1]
                box = _hash(label)
                del_lens(boxes, box, label)

    print(f"Part 1: {res1}")
    print(f"Part 2: {power_lens(boxes)}")
