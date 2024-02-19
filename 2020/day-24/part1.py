DXY = {
    "e": (1, 0),
    "w": (-1, 0),
    "ne": (0.5, 1),
    "nw": (-0.5, 1),
    "se": (0.5, -1),
    "sw": (-0.5, -1),
}


def parse(line: str) -> list[str]:
    result = []
    tmp = ""

    for ch in line:
        match ch:
            case "e" | "w":
                result.append(tmp + ch)
                tmp = ""
            case "n" | "s":
                tmp = ch
            case _:
                raise ValueError()

    return result


def get_tile(steps: list[str]) -> tuple[int, int]:
    cur = (0, 0)
    for step in steps:
        dx, dy = DXY[step]
        cur = (cur[0] + dx, cur[1] + dy)
    return cur


def near_tiles(tile: tuple[int, int]) -> list[tuple[int, int]]:
    return [(tile[0] + dx, tile[1] + dy) for dx, dy in DXY.values()]


def life_step(tiles: set[tuple[int, int]]) -> set[tuple[int, int]]:
    new_tiles = set()
    neighbours = {}

    for tile in tiles:
        for nbr in near_tiles(tile):
            if nbr not in neighbours:
                neighbours[nbr] = 0
            neighbours[nbr] += 1

    for tile, count in neighbours.items():
        if (tile in tiles and count == 1) or (count == 2):
            new_tiles.add(tile)

    return new_tiles


def part1(lines):
    black = set()
    for line in lines:
        steps = parse(line)
        tile = get_tile(steps)
        if tile not in black:
            black.add(tile)
        else:
            black.remove(tile)
    return black


def part2(black, steps=100):
    for _ in range(steps):
        black = life_step(black)
    return black


if __name__ == "__main__":
    with open("_inputs/2020/day-24/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n")

    black = part1(lines)
    print(f"Part 1: {len(black)}")

    black = part2(black)
    print(f"Part 2: {len(black)}")
