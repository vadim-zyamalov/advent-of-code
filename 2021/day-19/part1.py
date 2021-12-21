ROTATIONS = [("+x", "+y", "+z"),
             ("-y", "+x", "+z"),
             ("-x", "-y", "+z"),
             ("+y", "-x", "+z"),
             ("+z", "+x", "+y"),
             ("-x", "+z", "+y"),
             ("-z", "-x", "+y"),
             ("+x", "-z", "+y"),
             ("+y", "+z", "+x"),
             ("-z", "+y", "+x"),
             ("-y", "-z", "+x"),
             ("+z", "-y", "+x"),
             ("+y", "+x", "-z"),
             ("-x", "+y", "-z"),
             ("-y", "-x", "-z"),
             ("+x", "-y", "-z"),
             ("+x", "+z", "-y"),
             ("-z", "+x", "-y"),
             ("-x", "-z", "-y"),
             ("+z", "-x", "-y"),
             ("+z", "+y", "-x"),
             ("-y", "+z", "-x"),
             ("-z", "-y", "-x"),
             ("+y", "-z", "-x")]


def dump(pairs_matrix):
    print()
    for row in pairs_matrix:
        for pair in row:
            if not pair:
                print(" ", end="")
            elif pair[0] is True:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def reverse_rotate(rotation):
    tmp = [["x", rotation[0]],
           ["y", rotation[1]],
           ["z", rotation[2]]]
    result = {}
    for pair in tmp:
        if pair[1][0] == "+":
            pair[0] = "+" + pair[0]
        else:
            pair[0] = "-" + pair[0]
        pair[1] = pair[1][1]
        result[pair[1]] = pair[0]
    return (result['x'], result['y'], result['z'])


def rotate_point(point, rotation):
    if rotation == ROTATIONS[0]:
        return point
    tmp = {}
    tmp[rotation[0][1]] = point[0] * (1 if rotation[0][0] == "+" else -1)
    tmp[rotation[1][1]] = point[1] * (1 if rotation[1][0] == "+" else -1)
    tmp[rotation[2][1]] = point[2] * (1 if rotation[2][0] == "+" else -1)
    return (tmp['x'], tmp['y'], tmp['z'])


def rotate_scanner(sensor, rotation):
    return [rotate_point(point, rotation)
            for point in sensor]


def normalize_point(point, ref_point, d=1):
    return (point[0] - d * ref_point[0],
            point[1] - d * ref_point[1],
            point[2] - d * ref_point[2])


def normalize_scanner(sensor, ref_point, d=1):
    return [normalize_point(point, ref_point, d) for point in sensor]


def shift_scanner(sensor, rotation, ref_point0, ref_point1):
    return normalize_scanner(
        normalize_scanner(
            rotate_scanner(sensor, rotation),
            ref_point1),
        ref_point0, -1)


def check_pair(sensor0, sensor1):
    for rot in ROTATIONS:
        rsensor1 = rotate_scanner(sensor1, rot)
        for el_0 in sensor0:
            for el_1 in rsensor1:
                tmp0 = normalize_scanner(sensor0, el_0)
                tmp1 = normalize_scanner(rsensor1, el_1)
                if len(set(tmp0) & set(tmp1)) >= 12:
                    return (True, rot, el_0, el_1)
    return (False, None, None, None)


def merge_data(current, pairs_matrix, data, is_merged):
    result = set(data[current])
    for scanner in data.keys():
        if scanner in is_merged:
            continue
        if pairs_matrix[current][scanner][0] is True:
            is_merged.append(scanner)
            tmp = merge_data(scanner, pairs_matrix, data, is_merged)
            tmp = shift_scanner(tmp,
                                pairs_matrix[current][scanner][1],
                                pairs_matrix[current][scanner][2],
                                pairs_matrix[current][scanner][3])
            for point in tmp:
                result.add(point)
    return list(result)


def detect_scanners(current, rotations, pairs_matrix,
                    scanners_list, coordinates):
    for scanner in scanners_list:
        if scanner in coordinates:
            continue
        if pairs_matrix[current][scanner][0] is True:
            tmp = coordinates[current]
            if rotations != []:
                for _, rot in enumerate(rotations):
                    tmp = rotate_point(tmp, reverse_rotate(rot))
            tmp = normalize_point(tmp, pairs_matrix[current][scanner][2], -1)
            tmp = normalize_point(tmp, pairs_matrix[current][scanner][3])
            if rotations != []:
                for _, rot in enumerate(rotations[::-1]):
                    tmp = rotate_point(tmp, rot)
            coordinates[scanner] = tmp
            detect_scanners(scanner,
                            rotations + [pairs_matrix[current][scanner][1]],
                            pairs_matrix,
                            scanners_list,
                            coordinates)


input_data = {}
with open("input.txt", "r", encoding="utf-8") as f:
    i = -1
    for line in f:
        if line.strip() == "":
            continue
        if line.startswith("---"):
            _, _, num, _ = line.strip().split()
            i = int(num)
            if num not in input_data:
                input_data[i] = []
                continue
        x, y, z = line.strip().split(",")
        input_data[i].append((int(x),
                              int(y),
                              int(z)))


scanner_pairs = [[(False, None, None, None) for _ in input_data]
                 for _ in input_data]
for i, scanner0 in input_data.items():
    print(f"{i}, ", end="")
    for j, scanner1 in input_data.items():
        if i >= j:
            continue
        check_result = check_pair(scanner0, scanner1)
        if check_result[0] is True:
            scanner_pairs[i][j] = check_result
            scanner_pairs[j][i] = (
                True,
                reverse_rotate(check_result[1]),
                rotate_point(check_result[3],
                             reverse_rotate(check_result[1])),
                rotate_point(check_result[2],
                             reverse_rotate(check_result[1])))
print()


merged_scanners = [0]
answer = merge_data(0, scanner_pairs, input_data, merged_scanners)
print(f"Part 1: {len(answer)}")

scanners_coords = {}
scanners_coords[0] = (0, 0, 0)
detect_scanners(0, [], scanner_pairs, input_data.keys(), scanners_coords)

distances = [[0 for _ in scanners_coords]
             for _ in scanners_coords]
for i, scanner_i in scanners_coords.items():
    for j, scanner_j in scanners_coords.items():
        if i >= j:
            continue
        distances[i][j] = abs(scanner_i[0] - scanner_j[0]) + \
            abs(scanner_i[1] - scanner_j[1]) + \
            abs(scanner_i[2] - scanner_j[2])
        distances[j][i] = distances[i][j]

distances = [el for row in distances for el in row]
print(f"Part 2: {max(distances)}")
