def look_and_say_fast(string):
    result = ''
    count = 0
    prev = None
    for letter in string:
        if not prev:
            count += 1
            prev = letter
        elif prev != letter:
            result += str(count) + prev
            count = 1
            prev = letter
        else:
            count += 1
    if count > 0:
        result += str(count) + str(prev)
    return result


part = {1: 40, 2: 50}
for k in part:
    with open("input.txt", "r") as f:
        line = f.read()
        line = line.strip()

    for i in range(part[k]):
        line = look_and_say_fast(line)

    print("Part {}: {}".format(k, len(line)))
