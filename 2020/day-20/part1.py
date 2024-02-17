OPP = {"L": "R", "R": "L", "U": "D", "D": "U"}
DXY = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
MONSTER = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


def border(tile, side):
    match side:
        case "L":
            return int(
                ("".join(v[0] for v in tile)).replace("#", "1").replace(".", "0"),
                2,
            )
        case "R":
            return int(
                ("".join(v[-1] for v in tile)).replace("#", "1").replace(".", "0"),
                2,
            )
        case "U":
            return int(
                tile[0].replace("#", "1").replace(".", "0"),
                2,
            )
        case "D":
            return int(
                tile[-1].replace("#", "1").replace(".", "0"),
                2,
            )
        case _:
            raise ValueError()


def rot(tile):
    return ["".join(z) for z in zip(*reversed(tile))]


def flipv(tile):
    return [r[::-1] for r in tile]


def fliph(tile):
    return tile[::-1]


class Image:
    def __init__(self, image):
        coords = sorted(image.keys())
        minx, miny = coords[0]
        maxx, maxy = coords[-1]

        self.image = []

        for y in range(miny, maxy + 1):
            new_row = [r[1:-1] for r in image[minx, y].tile[1:-1]]
            for x in range(minx + 1, maxx + 1):
                new_row = [
                    r0 + r1[1:-1] for r0, r1 in zip(new_row, image[x, y].tile[1:-1])
                ]
            self.image += new_row

    def rot(self):
        self.image = ["".join(z) for z in zip(*reversed(self.image))]

    def flipv(self):
        self.image = [r[::-1] for r in self.image]

    def fliph(self):
        self.image = self.image[::-1]


def search_tile(
    cur: tuple[int, list], side: str, tiles: dict[int, list], used: list[int]
):
    result = []
    cur_id, cur_tile = cur

    for tile_id, tile in tiles.items():
        stop = False
        if (cur_id == tile_id) or (tile_id in used):
            continue
        for _ in range(4):
            for flip_func in [fliph, flipv]:
                if border(cur_tile, side) == border(tile, OPP[side]):
                    stop = True
                    result.append((tile_id, tile))
                    break
                tile = flip_func(tile)
                if border(cur_tile, side) == border(tile, OPP[side]):
                    stop = True
                    result.append((tile_id, tile))
                    break
                tile = flip_func(tile)
            if stop:
                break
            tile = rot(tile)
    return result


def arrange_tiles(tiles: dict[int, list]):
    image = {}
    indices = {}

    init_id = list(tiles.keys())[0]

    image[0, 0] = tiles[init_id]
    indices[0, 0] = init_id

    used = [init_id]
    seen = []

    queue = [(0, 0)]

    while queue:
        x, y = queue.pop()

        if (x, y) in seen:
            continue

        seen.append((x, y))

        for side in "LRDU":
            dx, dy = DXY[side]
            nx, ny = x + dx, y + dy
            if (nx, ny) in seen:
                continue
            new_tile = search_tile((indices[x, y], image[x, y]), side, tiles, used)
            if new_tile:
                new_id, new_tile = new_tile[0]
                indices[nx, ny] = new_id
                image[nx, ny] = new_tile
                used.append(new_id)
                queue.append((nx, ny))

    return indices, image


def retrieve_image(image):
    coords = sorted(image.keys())
    minx, miny = coords[0]
    maxx, maxy = coords[-1]

    result = []

    for y in range(miny, maxy + 1):
        new_row = [r[1:-1] for r in image[minx, y][1:-1]]
        for x in range(minx + 1, maxx + 1):
            new_row = [r0 + r1[1:-1] for r0, r1 in zip(new_row, image[x, y][1:-1])]
        result += new_row

    return result


def count_monster(image, monster, size):
    Mx, My = size
    Nx, Ny = len(image[0]), len(image)

    m_num = 0

    for x in range(0, Nx - Mx):
        for y in range(0, Ny - My):
            if all(image[y + dy][x + dx] == "#" for dx, dy in monster):
                m_num += 1

    return m_num


def search_monster(image):
    monster = [
        (x, y) for y, row in enumerate(MONSTER) for x, el in enumerate(row) if el == "#"
    ]

    Mx, My = len(MONSTER[0]), len(MONSTER)

    stop = False
    m_num = 0
    for _ in range(4):
        for flip_func in [fliph, flipv]:
            m_num = count_monster(image, monster, (Mx, My))
            if m_num:
                stop = True
                break
            image = flip_func(image)
            m_num = count_monster(image, monster, (Mx, My))
            if m_num:
                stop = True
                break
            image = flip_func(image)
        if stop:
            break
        image = rot(image)

    return sum(el == "#" for row in image for el in row) - m_num * len(monster)


def checksum(tiles):
    indices, image = arrange_tiles(tiles)
    coords = sorted(indices.keys())

    minx, miny = coords[0]
    maxx, maxy = coords[-1]

    return (
        indices[minx, miny]
        * indices[minx, maxy]
        * indices[maxx, miny]
        * indices[maxx, maxy],
        image,
    )


if __name__ == "__main__":
    with open("_inputs/2020/day-20/input.txt", "r", encoding="utf8") as f:
        chunks = f.read().strip().split("\n\n")

    tiles = {}

    for chunk in chunks:
        chunk = chunk.split("\n")
        tile_id = int(chunk[0][5:-1])
        tiles[tile_id] = chunk[1:]

    result, image = checksum(tiles)
    print(f"Part 1: {result}")

    image = retrieve_image(image)
    print(f"Part 2: {search_monster(image)}")
