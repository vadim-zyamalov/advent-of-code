def mincoord(tiles, dim, rc):
    return min(d[dim] for d in tiles if d[1 - dim] == rc)


def maxcoord(tiles, dim, rc):
    return max(d[dim] for d in tiles if d[1 - dim] == rc)


def step_p1(pos, face, tiles, walls, faces):
    nx_pos = (pos[0] + faces[face][0], pos[1] + faces[face][1])
    if nx_pos in tiles:
        if nx_pos not in walls:
            return nx_pos
        return pos
    else:
        match face:
            case 0:
                nx_col = mincoord(tiles, 1, pos[0])
                if (pos[0], nx_col) in walls:
                    return pos
                return (pos[0], nx_col)
            case 2:
                nx_col = maxcoord(tiles, 1, pos[0])
                if (pos[0], nx_col) in walls:
                    return pos
                return (pos[0], nx_col)
            case 3:
                nx_row = maxcoord(tiles, 0, pos[1])
                if (nx_row, pos[1]) in walls:
                    return pos
                return (nx_row, pos[1])
            case 1:
                nx_row = mincoord(tiles, 0, pos[1])
                if (nx_row, pos[1]) in walls:
                    return pos
                return (nx_row, pos[1])


#      +cc--+dd--+
#      g    |    b
#      g    |    b
#      |    |    |
#      +----+aa==+
#      f    a
#      f    a
#      |    |
# +ff--+----+
# |    |    |
# g    |    b
# g    |    b
# +----+ee--+
# c    e
# c    e
# |    |
# +dd--+
def wrap_cube(face, pos, m):
    row, col = pos
    # a
    if (2 * m <= col < 3 * m) and (row >= m) and (face == 1):
        nx_pos = (m + col % m, 2 * m - 1)
        nx_face = 2
    if (col >= 2 * m) and (m <= row < 2 * m) and (face == 0):
        nx_pos = (m - 1, 2 * m + row % m)
        nx_face = 3
    # b
    if (col >= 3 * m) and (0 <= row < m) and (face == 0):
        nx_pos = (3 * m - 1 - row % m, 2 * m - 1)
        nx_face = 2
    if (col >= 2 * m) and (2 * m <= row < 3 * m) and (face == 0):
        nx_pos = (m - 1 - row % m, 3 * m - 1)
        nx_face = 2
    # c
    if (m <= col < 2 * m) and (row < 0) and (face == 3):
        nx_pos = (3 * m + col % m, 0)
        nx_face = 0
    if (col < 0) and (3 * m <= row < 4 * m) and (face == 2):
        nx_pos = (0, m + row % m)
        nx_face = 1
    # d
    if (2 * m <= col < 3 * m) and (row < 0) and (face == 3):
        nx_pos = (4 * m - 1, col % m)
        nx_face = 3
    if (0 <= col < m) and (row >= 4 * m) and (face == 1):
        nx_pos = (0, 2 * m + col % m)
        nx_face = 1
    # e
    if (m <= col < 2 * m) and (row >= 3 * m) and (face == 1):
        nx_pos = (3 * m + col % m, m - 1)
        nx_face = 2
    if (col >= m) and (3 * m <= row < 4 * m) and (face == 0):
        nx_pos = (3 * m - 1, m + row % m)
        nx_face = 3
    # f
    if (col < m) and (m <= row < 2 * m) and (face == 2):
        nx_pos = (2 * m, row % m)
        nx_face = 1
    if (0 <= col < m) and (row < 2 * m) and (face == 3):
        nx_pos = (m + col % m, m)
        nx_face = 0
    # g
    if (col < m) and (0 <= row < m) and (face == 2):
        nx_pos = (3 * m - 1 - row % m, 0)
        nx_face = 0
    if (col < 0) and (2 * m <= row < 3 * m) and (face == 2):
        nx_pos = (m - 1 - row % m, m)
        nx_face = 0
    return nx_pos, nx_face


def step_p2(pos, face, tiles, walls, faces, m):
    nx_pos = (pos[0] + faces[face][0], pos[1] + faces[face][1])
    if nx_pos in tiles:
        if nx_pos not in walls:
            return nx_pos, face
        return pos, face
    else:
        wp_pos, wp_face = wrap_cube(face, nx_pos, m)
        if wp_pos not in tiles:
            exit(111)
        if wp_pos in walls:
            return pos, face
        return wp_pos, wp_face


def process_p1(script, tiles, walls, faces):
    pos = (0, min(d[1] for d in tiles if d not in walls and d[0] == 0))
    face = 0
    for c in script:
        match c:
            case "L":
                face = (face - 1) % 4
            case "R":
                face = (face + 1) % 4
            case _:
                for _ in range(c):
                    nx_pos = step_p1(pos, face, tiles, walls, faces)
                    if nx_pos == pos:
                        break
                    pos = nx_pos
    return pos, face


def process_p2(script, tiles, walls, faces, m):
    pos = (0, min(d[1] for d in tiles if d not in walls and d[0] == 0))
    face = 0
    for c in script:
        match c:
            case "L":
                face = (face - 1) % 4
            case "R":
                face = (face + 1) % 4
            case _:
                for _ in range(c):
                    nx_pos, nx_face = step_p2(pos, face, tiles, walls, faces, m)
                    if nx_pos == pos:
                        break
                    pos = nx_pos
                    face = nx_face
    return pos, face


TILES = set()
WALLS = set()
SCRIPT = []

FACES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

with open("../../_inputs/2022/day-22/input.txt", "r", encoding="utf8") as f:
    row = -1
    for line in f:
        row += 1
        line = line.rstrip()
        if line == "":
            break
        # print(line)
        for col in range(len(line)):
            match line[col]:
                case ".":
                    TILES.add((row, col))
                case "#":
                    TILES.add((row, col))
                    WALLS.add((row, col))
                case _:
                    pass
    line = f.readline().strip()
    tmp = ""
    for i in range(len(line)):
        match line[i]:
            case "R" | "L":
                SCRIPT.append(int(tmp))
                SCRIPT.append(line[i])
                tmp = ""
            case _:
                tmp += line[i]
    if tmp:
        SCRIPT.append(int(tmp))

# print(WALLS)
# print(SCRIPT)

pos, face = process_p1(SCRIPT, TILES, WALLS, FACES)
print(f"Part 1: {1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + face}")
pos, face = process_p2(SCRIPT, TILES, WALLS, FACES, 50)
print(f"Part 2: {1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + face}")
