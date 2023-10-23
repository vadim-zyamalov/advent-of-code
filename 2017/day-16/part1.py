def dance(prog, line):
    seq = line.copy()
    for el in prog:
        match el[0]:
            case "s":
                i = int(el[1:])
                seq = seq[-i:] + seq[:-i]
            case "x":
                i, j = [int(z) for z in el[1:].split("/")]
                seq[i], seq[j] = seq[j], seq[i]
            case "p":
                i, j = [seq.index(z) for z in el[1:].split("/")]
                seq[i], seq[j] = seq[j], seq[i]
    return seq


if __name__ == "__main__":
    seq = [chr(ord("a") + i) for i in range(16)]
    init = seq.copy()

    with open("../../_inputs/2017/day-16/input.txt", "r", encoding="utf8") as f:
        line = f.read().strip().split(",")

    seq = dance(line, seq)
    print(f"Part 1: {''.join(seq)}")

    i = 2
    while i <= 1_000_000_000:
        seq = dance(line, seq)
        if seq == init:
            i += (1_000_000_000 // i - 1) * i
        i += 1

    print(f"Part 2: {''.join(seq)}")
