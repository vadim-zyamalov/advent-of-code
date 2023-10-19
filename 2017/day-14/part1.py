from functools import reduce


def process_list(length, list_seq, pos, skip):
    LEN = len(list_seq)
    end_pos = (pos + length - 1) % LEN
    for i in range(length // 2):
        list_seq[(pos + i) % LEN], list_seq[(end_pos - i) % LEN] = (
            list_seq[(end_pos - i) % LEN],
            list_seq[(pos + i) % LEN],
        )
    return list_seq, pos + length + skip, skip + 1


def knot_hash(prog, extra=[17, 31, 73, 47, 23]):
    prog = [ord(c) for c in prog]
    prog.extend(extra)

    LIST = [i for i in range(256)]
    POS = 0
    SKIP = 0

    for i in range(64):
        for l in prog:
            LIST, POS, SKIP = process_list(l, LIST, POS, SKIP)

    res = []

    for i in range(16):
        res.append(reduce(lambda x, y: x ^ y, LIST[(16 * i) : (16 * (i + 1))]))

    return "".join(f"{i:02x}" for i in res)


def hash_to_bin(hex_hash):
    return f"{int(hex_hash, 16):0128b}"


def purge_region(i, j, tbl):
    n = len(tbl)
    if (-1 < i - 1) and (tbl[i - 1][j] > 0):
        tbl[i - 1][j] *= -1
        purge_region(i - 1, j, tbl)
    if (i + 1 < n) and (tbl[i + 1][j] > 0):
        tbl[i + 1][j] *= -1
        purge_region(i + 1, j, tbl)
    if (-1 < j - 1) and (tbl[i][j - 1] > 0):
        tbl[i][j - 1] *= -1
        purge_region(i, j - 1, tbl)
    if (j + 1 < n) and (tbl[i][j + 1] > 0):
        tbl[i][j + 1] *= -1
        purge_region(i, j + 1, tbl)


def count_regions(table):
    n = len(table)
    result = 0
    for i in range(n):
        for j in range(n):
            if table[i][j] <= 0:
                continue
            else:
                result += 1
                table[i][j] *= -1
                purge_region(i, j, table)
    return result


if __name__ == "__main__":
    # KEY = "flqrgnkx"
    KEY = "hfdlxzhv"
    TBL = []

    result = 0

    for i in range(128):
        tmp_hash = hash_to_bin(knot_hash(KEY + "-" + str(i)))
        result += sum(int(el) for el in tmp_hash)
        TBL.append(list(int(el) for el in tmp_hash))

    print(f"Part 1: {result}")
    print(f"Part 2: {count_regions(TBL)}")
