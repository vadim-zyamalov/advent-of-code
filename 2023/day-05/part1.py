def process(seed: int, maps: list[list[tuple]]) -> int:
    res = seed
    for cur_map in maps:
        for dest, src, rng in cur_map:
            if 0 <= (res - src) < rng:
                res = dest + (res - src)
                break
    return res


def overlaps(seeds: list[int], maps: list[list[tuple]]) -> list[list[int]]:
    ranges = [[beg, beg + rng] for beg, rng in zip(seeds[::2], seeds[1::2])]

    for cur_map in maps:
        new_ranges = []
        while ranges:
            beg, fin = ranges.pop(0)
            for dest, src, rng in cur_map:
                new_beg = max(beg, src)
                new_fin = min(fin, src + rng)

                if new_beg < new_fin:
                    new_ranges.append([dest + (new_beg - src), dest + (new_fin - src)])
                    if beg < new_beg:
                        ranges.append([beg, new_beg])
                    if fin > new_fin:
                        ranges.append([new_fin, fin])
                    break
            else:
                new_ranges.append([beg, fin])

        ranges = new_ranges

    return ranges


if __name__ == "__main__":
    with open("_inputs/2023/day-05/input.txt", "r", encoding="utf8") as f:
        maps = []
        seeds = [int(el) for el in f.readline().strip().split(":")[1].strip().split()]
        f.readline()

        cur_maps = []
        for line in f:
            line = line.strip()
            if line == "":
                maps.append(cur_maps)
                cur_maps = []
            elif line.endswith(":"):
                continue
            else:
                cur_maps.append(tuple(int(el) for el in line.split()))
        if cur_maps != []:
            maps.append(cur_maps)

    res = float("inf")
    for seed in seeds:
        res = min(res, process(seed, maps))

    print(f"Part 1: {res}")

    res = overlaps(seeds, maps)

    print(f"Part 2: {min(el for el, _ in res)}")
