from itertools import product

RANGES = []


def is_overlap(cube, cutter):
    for dim in ['x', 'y', 'z']:
        if (cutter[dim][1] < cube[dim][0]) or \
           (cutter[dim][0] > cube[dim][1]):
            return False
    return True


def dim_chunks(cube, cutter, dim):
    chunks_0 = (cube[dim][0],
                min(cutter[dim][0] - 1, cube[dim][1]))
    chunks_1 = (max(cube[dim][0], cutter[dim][0]),
                min(cube[dim][1], cutter[dim][1]))
    chunks_2 = (max(cutter[dim][1] + 1, cube[dim][0]),
                cube[dim][1])
    return [chunks_0 if chunks_0[0] <= chunks_0[1] else None,
            chunks_1 if chunks_1[0] <= chunks_1[1] else None,
            chunks_2 if chunks_2[0] <= chunks_2[1] else None]


# Limit cube
def limit(cube, limits):
    result = {}
    for dim in ['x', 'y', 'z']:
        result[dim] = (max(cube[dim][0], limits[dim][0]),
                       min(cube[dim][1], limits[dim][1]))
        if result[dim][0] > result[dim][1]:
            return None
    return result


def cutoff(cube, cutter):
    # Are there any intersection between cube and another one?
    if not is_overlap(cube, cutter):
        return [cube]
    # Divide cube into layers
    result = []
    chunks_x = dim_chunks(cube, cutter, 'x')
    chunks_y = dim_chunks(cube, cutter, 'y')
    chunks_z = dim_chunks(cube, cutter, 'z')
    # If there is a lower layer append it
    if chunks_z[0]:
        result.append({'x': cube['x'],
                       'y': cube['y'],
                       'z': chunks_z[0]})
    # If there is a top layer append it
    if chunks_z[2]:
        result.append({'x': cube['x'],
                       'y': cube['y'],
                       'z': chunks_z[2]})
    # Loop through the middle layer
    for i, j in product([0, 1, 2], repeat=2):
        # this is a cut chunk
        if i * j == 1:
            continue
        # Ignore out of bounds chunks
        if not chunks_x[i] or not chunks_y[j]:
            continue
        # Append resulting sub cubes
        result.append({'x': chunks_x[i],
                       'y': chunks_y[j],
                       'z': chunks_z[1]})
    return result


def count(on_list):
    result = 0
    for cube in on_list:
        result += abs(cube['x'][1] - cube['x'][0] + 1) * \
            abs(cube['y'][1] - cube['y'][0] + 1) * \
            abs(cube['z'][1] - cube['z'][0] + 1)
    return result


def process(rule, on_list, limits=None):
    result = []
    current_cube = {'x': rule['x'],
                    'y': rule['y'],
                    'z': rule['z']}
    if limits:
        current_cube = limit(current_cube, limits)
    # Check whether the cube is out of limits
    if not current_cube:
        return on_list
    # Cut the current cube from all the previous ones
    for list_cube in on_list:
        tmp_cuts = cutoff(list_cube, current_cube)
        result.extend(tmp_cuts)
    # If we are adding the add
    if rule['cmd'] == "on":
        result.append(current_cube)
    return result


with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        range_current = {}
        status, rest = line.strip().split()
        range_current["cmd"] = status
        tmp = rest.split(",")
        for r in tmp:
            coord, rest = r.split("=")
            r_low, r_high = (int(i) for i in rest.split(".."))
            range_current[coord] = (min(r_low, r_high),
                                    max(r_low, r_high))
        RANGES.append(range_current)

cubes_on = []
for r in RANGES:
    cubes_on = process(r, cubes_on, {'x': (-50, 50),
                                     'y': (-50, 50),
                                     'z': (-50, 50)})

print(f"Part 1: {count(cubes_on)}")

cubes_on = []
for r in RANGES:
    cubes_on = process(r, cubes_on)

print(f"Part 2: {count(cubes_on)}")
