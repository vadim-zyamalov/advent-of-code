from itertools import product

RANGES = []


# Limit cube
def limit(cube, limits):
    return {'x': (max(cube['x'][0], limits['x'][0]),
                  min(cube['x'][1], limits['x'][1])),
            'y': (max(cube['y'][0], limits['y'][0]),
                  min(cube['y'][1], limits['y'][1])),
            'z': (max(cube['z'][0], limits['z'][0]),
                  min(cube['z'][1], limits['z'][1]))}


def cutoff(cube, cutter):
    # Are there any intersection between cube and another one?
    if (cutter['x'][1] < cube['x'][0]) or \
       (cutter['x'][0] > cube['x'][1]) or \
       (cutter['y'][1] < cube['y'][0]) or \
       (cutter['y'][0] > cube['y'][1]) or \
       (cutter['z'][1] < cube['z'][0]) or \
       (cutter['z'][0] > cube['z'][1]):
        return [cube]
    # Divide cube into layers
    result = []
    chunks_x = [(cube['x'][0], cutter['x'][0] - 1),
                (max(cube['x'][0], cutter['x'][0]),
                 min(cube['x'][1], cutter['x'][1])),
                (cutter['x'][1] + 1, cube['x'][1])]
    chunks_y = [(cube['y'][0], cutter['y'][0] - 1),
                (max(cube['y'][0], cutter['y'][0]),
                 min(cube['y'][1], cutter['y'][1])),
                (cutter['y'][1] + 1, cube['y'][1])]
    chunks_z = [(cube['z'][0], cutter['z'][0] - 1),
                (max(cube['z'][0], cutter['z'][0]),
                 min(cube['z'][1], cutter['z'][1])),
                (cutter['z'][1] + 1, cube['z'][1])]
    # If there is a lower layer append it
    if chunks_z[0][0] <= chunks_z[0][1]:
        result.append({'x': cube['x'],
                       'y': cube['y'],
                       'z': chunks_z[0]})
    # If there is a top layer append it
    if chunks_z[2][0] <= chunks_z[2][1]:
        result.append({'x': cube['x'],
                       'y': cube['y'],
                       'z': chunks_z[2]})
    # Loop through the middle layer
    for ix, iy in product([0, 1, 2], repeat=2):
        # this is a cut chunk
        if ix * iy == 1:
            continue
        # Ignore out of bounds chunks
        if (chunks_x[ix][0] > chunks_x[ix][1]) or \
           (chunks_y[iy][0] > chunks_y[iy][1]) or \
           (chunks_z[1][0] > chunks_z[1][1]):
            continue
        # Append resulting sub cubes
        result.append({'x': chunks_x[ix],
                       'y': chunks_y[iy],
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
    if (current_cube['x'][0] > current_cube['x'][1]) or \
       (current_cube['y'][0] > current_cube['y'][1]) or \
       (current_cube['z'][0] > current_cube['z'][1]):
        return on_list
    # Cut the current cube from all the previous ones
    for c in on_list:
        tmp = cutoff(c, current_cube)
        result.extend(tmp)
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
