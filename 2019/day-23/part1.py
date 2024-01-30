import sys

sys.path.append(".\\")

from utils.intcode import Intcode
from collections import defaultdict

if __name__ == "__main__":
    with open("_inputs/2019/day-23/input.txt", "r", encoding="utf8") as f:
        numbers = list(map(int, f.read().strip().split(",")))

    network = [Intcode(numbers) for _ in range(50)]
    packets = defaultdict(list)

    last_nat = None
    part1 = True

    # Initial loop
    for i in range(50):
        packets[i] = []
        output, _ = network[i].process(inputs=[i])
        if output:
            oi = iter(output)
            for addr, x, y in zip(oi, oi, oi):
                packets[addr].append((x, y))

    # Main loop
    while True:
        for i in range(50):
            if packets[i]:
                inp = packets[i].pop(0)
                output, _ = network[i].process(inputs=list(inp), resume=True)
            else:
                output, _ = network[i].process(inputs=[-1], resume=True)

            if output:
                oi = iter(output)
                for addr, x, y in zip(oi, oi, oi):
                    packets[addr].append((x, y))
        # NAT
        if packets[255] and part1:
            print(f"Part 1: {packets[255][0][1]}")
            part1 = False
        if all(not v for k, v in packets.items() if k != 255):
            packets[0].append(packets[255][-1])
            if last_nat == packets[255][-1][1]:
                print(f"Part 2: {last_nat}")
                break
            last_nat = packets[255][-1][1]
