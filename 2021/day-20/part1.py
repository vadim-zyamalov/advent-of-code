def dump(image):
    print()
    for row in image:
        print(''.join(row))


def deepcopy(image):
    return [list(row) for row in image]


def gen_empty(image):
    return [['.' for _ in row] for row in image]


def increase_image(image, n=1):
    result = []
    dimi = len(image)
    for i in range(n):
        result.append(['.' for _ in range(dimi + 2 * n)])
    for i in range(dimi):
        result.append(['.' for _ in range(n)] +
                      list(image[i]) +
                      ['.' for _ in range(n)])
    for i in range(n):
        result.append(['.' for _ in range(dimi + 2 * n)])
    return result


def shrink_image(image, n=1):
    return [list(row[n:(len(row) - n)])
            for row in image[n:(len(image) - n)]]


def process_cell(i, j, image):
    result = '0b'
    for row in range(i - 1, i + 2):
        result += ''.join(['1' if letter == "#" else '0'
                           for letter in image[row][(j - 1):(j + 2)]])
    return int(result, 2)


def process_image(image):
    result = gen_empty(image)
    dimi, dimj = len(image), len(image[0])
    for i in range(1, dimi - 1):
        for j in range(1, dimj - 1):
            result[i][j] = PATTERN[process_cell(i, j, image)]
    return result


def count_lights(image):
    return sum(1 for row in image for letter in row if letter == "#")


PATTERN = ''

with open("input.txt", "r", encoding="utf-8") as f:
    line = f.readline().strip()
    while line != "":
        PATTERN += line
        line = f.readline().strip()
    image = []
    for line in f:
        if line.strip() == "":
            continue
        image.append(list(line.strip()))

PARTS = {1: 2, 2: 50}
for part, val in PARTS.items():
    loop_image = deepcopy(image)
    loop_image = increase_image(loop_image, val * 2)
    for step in range(val):
        loop_image = process_image(loop_image)
        loop_image = shrink_image(loop_image, 1)
    print(f"Part {part}: {count_lights(loop_image)}")
