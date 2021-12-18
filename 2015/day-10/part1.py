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


parts = {1: 40, 2: 50}
for part, val in parts.items():
    with open("input.txt", "r", encoding="utf-8") as f:
        line = f.read()
        line = line.strip()

    for i in range(val):
        line = look_and_say_fast(line)

    print(f"Part {part}: {len(line)}")
