chars_old = 0
chars_new = 0

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        string = []

        for letter in line.strip():
            string.append(letter)
        chars_new += 2
        i = 0
        while i < len(string):
            if string[i] == '"':
                chars_old += 1
                chars_new += 2
            elif string[i] == '\\':
                chars_old += 1
                chars_new += 2
                if string[i+1] == '"':
                    chars_old += 1
                    chars_new += 2
                    i += 1
                elif string[i+1] == "\\":
                    chars_old += 1
                    chars_new += 2
                    i += 1
                elif string[i+1] == 'x':
                    chars_old += 3
                    chars_new += 3
                    i += 3
            else:
                chars_old += 1
                chars_new += 1
            i += 1
print(f"Part 2: {chars_new - chars_old}")
