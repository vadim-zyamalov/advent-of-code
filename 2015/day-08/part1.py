chars = 0
codes = 0

with open("input.txt", "r", encoding="utf-8") as f:
    for line in f:
        string = []
        for letter in line.strip():
            string.append(letter)
        i = 0
        while i < len(string):
            if string[i] == '"':
                codes += 1
            elif string[i] == '\\':
                codes += 1
                if string[i+1] == '"':
                    codes += 1
                    chars += 1
                    i += 1
                elif string[i+1] == "\\":
                    codes += 1
                    chars += 1
                    i += 1
                elif string[i+1] == 'x':
                    codes += 3
                    chars += 1
                    i += 3
            else:
                codes += 1
                chars += 1
            i += 1
print(f"Part 1: {codes - chars}")
