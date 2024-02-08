from collections import defaultdict


def genMasks(line):
    mask0, mask1, maskX = (), (), ()
    for i, c in enumerate(line[::-1]):
        match c:
            case "0":
                mask0 += (i,)
            case "1":
                mask1 += (i,)
            case _:
                maskX += (i,)

    return mask0, mask1, maskX


def genAddresses(addr, mask1, maskX):
    max_num = 2 ** len(maskX)
    res = []

    for x in range(max_num):
        addr_new = addr

        for i in mask1:
            addr_new |= 1 << i

        for i in maskX:
            x, r = divmod(x, 2)
            if r:
                addr_new |= 1 << i
            else:
                addr_new &= ~(1 << i)
            i += 1

        res.append(addr_new)

    return res


if __name__ == "__main__":
    memory = defaultdict(int)
    memory2 = defaultdict(int)
    mask0, mask1, maskX = (), (), ()
    with open("_inputs/2020/day-14/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            p0, p1 = line.split(" = ")
            if p0 == "mask":
                mask0, mask1, maskX = genMasks(p1)
            else:
                p0 = int(p0.replace("mem[", "").replace("]", ""))
                p1 = int(p1)
                p0s = genAddresses(p0, mask1, maskX)

                for addr in p0s:
                    memory2[addr] = p1

                for i in mask1:
                    p1 |= 1 << i
                for i in mask0:
                    p1 &= ~(1 << i)
                memory[p0] = p1

    print(f"Part 1: {sum(memory.values())}")
    print(f"Part 2: {sum(memory2.values())}")
