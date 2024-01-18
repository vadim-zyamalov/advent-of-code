from functools import cache


@cache
def count(entry: str, sizes: tuple[int, ...], current: int = 0) -> int:
    if entry == "":
        # We finished and no opened groups left
        if (len(sizes) == 1) and (current == sizes[0]):
            return 1
        if (len(sizes) == 0) and (current == 0):
            return 1
        return 0

    result = 0

    # If current letter is not `?` we use it else we split branches
    next_step = [".", "#"] if entry[0] == "?" else entry[0]
    for nxt in next_step:
        if nxt == "#":
            # Go ahead, we in the group
            result += count(entry[1:], sizes, current + 1)
        else:
            # We exited the group
            # Let's check whether the group is of good size
            if (len(sizes) > 0) and (current > 0) and (current == sizes[0]):
                result += count(entry[1:], sizes[1:], 0)
            # or go ahead if we were not in the group
            elif current == 0:
                result += count(entry[1:], sizes, 0)
    return result


if __name__ == "__main__":
    entries = []
    with open("_inputs/2023/day-12/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break

            springs, seq = line.split()
            seq = tuple(int(el) for el in seq.split(","))

            entries.append((springs, seq))

    res1 = 0
    res2 = 0
    for springs, seq in entries:
        res1 += count(springs, seq)
        res2 += count("?".join([springs] * 5), seq * 5)

    print(f"Part 1: {res1}")
    print(f"Part 2: {res2}")
