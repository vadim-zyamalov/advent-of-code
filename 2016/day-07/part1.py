def check_chunk_tls(chunk):
    for i in range(len(chunk) - 3):
        if (chunk[i] == chunk[i+3]) and \
           (chunk[i+1] == chunk[i+2]) and \
           (chunk[i] != chunk[i+1]):
            return True
    return False


def check_address_tls(allowed, prohibited):
    return any(check_chunk_tls(el) for el in allowed) and \
        all(not check_chunk_tls(el) for el in prohibited)


def check_address_ssl(allowed, prohibited):
    for chunk_a in allowed:
        for i in range(len(chunk_a) - 2):
            if (chunk_a[i] == chunk_a[i+2]) and \
               (chunk_a[i] != chunk_a[i+1]):
                test = str(chunk_a[i+1] +
                           chunk_a[i] +
                           chunk_a[i+1])
                for chunk_b in prohibited:
                    if test in chunk_b:
                        return True
    return False


def split_line(ln):
    allowed = []
    prohibited = []
    tmp = ""
    for letter in ln:
        if letter == "[":
            if tmp != "":
                allowed.append(tmp)
                tmp = ""
        elif letter == "]":
            if tmp != "":
                prohibited.append(tmp)
                tmp = ""
        else:
            tmp += letter
    if tmp != "":
        allowed.append(tmp)
    return allowed, prohibited


answer_1 = 0
answer_2 = 0
with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        fst, snd = split_line(line)
        if check_address_tls(fst, snd):
            answer_1 += 1
        if check_address_ssl(fst, snd):
            answer_2 += 1

print(f"Part 1: {answer_1}")
print(f"Part 2: {answer_2}")
