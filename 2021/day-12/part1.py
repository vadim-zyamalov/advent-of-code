scheme = {}


def small(cave):
    return all(str.islower(letter) for letter in cave)


def walk(cave, visited, allowed):
    visited_c = visited.copy()
    if cave == 'end':
        return [[cave]]
    if small(cave):
        visited_c[cave] += 1
    variants = []
    for next_cave in scheme[cave]:
        if (small(next_cave) and
            (visited_c[next_cave] == 0)) or \
           (small(next_cave) and
            (next_cave == allowed) and
            (visited_c[next_cave] <= 1)) or \
           not small(next_cave):
            result = walk(next_cave, visited_c, allowed)
            if result:
                variants.extend(result)
    if variants != []:
        return [[cave] + tail for tail in variants]
    return None


with open("input.txt", "r") as f:
    for line in f:
        if line.strip() != '':
            cave1, cave2 = line.strip().split('-')
            if cave1 not in scheme:
                scheme[cave1] = []
            if cave2 not in scheme:
                scheme[cave2] = []
            scheme[cave1].append(cave2)
            scheme[cave2].append(cave1)


# Part 1
visited = {}
for k in scheme:
    if small(k):
        visited[k] = 0

result = walk('start', visited, '')
if result:
    print(f"Part 1: {len(result)}")

# Part 2
result = []
visited = {}
for k in scheme:
    if small(k):
        visited[k] = 0


allowed_list = [k for k in visited if (k != 'start') and (k != 'end')]

for a in allowed_list:
    tmp = walk('start', visited, a)
    if tmp:
        for path in tmp:
            if path not in result:
                result.append(path)
if result:
    print(f"Part 2: {len(result)}")
