PROG = []

if __name__ == "__main__":
    with open("_inputs/2018/day-01/input.txt", "r", encoding="utf8") as f:
        for line in f:
            if line.strip() == "":
                break
            PROG.append(int(line.strip()))

    i, N = 0, len(PROG)
    freq = 0
    freqs = set()
    freqs.add(0)

    while True:
        freq += PROG[i]
        if freq in freqs:
            print(f"Part 2: {freq}")
            exit()
        freqs.add(freq)
        i = (i + 1) % N
