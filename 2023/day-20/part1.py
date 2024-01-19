from collections import deque
from math import lcm


class Module:
    def __init__(self, name, type, dests) -> None:
        # False == flip-flop
        self.name = name
        self.type = type
        self.dests = dests
        match self.type:
            case 0:
                self.is_on = False
            case 1:
                self.src = []
                self.memory = {}
            case _:
                pass

    def reset(self):
        match self.type:
            case 0:
                self.is_on = False
            case 1:
                for k in self.memory:
                    self.memory[k] = 0
            case _:
                pass

    def process(self, signal, src):
        signals = []
        new_signal = None

        if self.type == 0:
            if signal == 0:
                self.is_on = not self.is_on
                new_signal = int(self.is_on)
        elif self.type == 1:
            self.memory[src] = signal
            new_signal = int(not all(self.memory.values()))
        else:
            return []

        if new_signal is not None:
            for dest in self.dests:
                signals.append((self.name, dest, new_signal))

        return signals


class Network:
    def __init__(self):
        self.names = []
        self.modules = {}
        self.cache = {}
        self.push_no = 0
        self.counter = {}

    def reset(self):
        self.cache = {0: 0}
        self.push_no = 0
        for module in self.modules:
            self.modules[module].reset()
        for name in self.counter:
            self.counter[name] = 0

    def add(self, module):
        self.names.append(module.name)
        self.modules[module.name] = module

    def finalize(self, fin="rx"):
        tmp_src = {}

        for name in self.names:
            cur_module = self.modules[name]
            for dest in cur_module.dests:
                if dest not in tmp_src:
                    tmp_src[dest] = []
                tmp_src[dest].append(cur_module.name)

        if tmp_src != {}:
            for name in tmp_src:
                if name not in self.names:
                    self.names.append(name)
                    self.modules[name] = Module(name, 2, [])
                    continue
                if self.modules[name].type == 1:
                    self.modules[name].src = tmp_src[name]
                    for src_name in tmp_src[name]:
                        self.modules[name].memory[src_name] = 0

        for name in self.names:
            cur_module = self.modules[name]
            if fin in cur_module.dests:
                self.counter = {k: 0 for k in cur_module.src}

        self.cache[0] = 0

    def hash(self):
        result = ""
        for name in self.names:
            cur_module = self.modules[name]
            if cur_module.type == 0:
                result += f"{int(cur_module.is_on)}"
            elif cur_module.type == 1:
                for src in cur_module.src:
                    result += f"{cur_module.memory[src]}"
        return int(result, 2)

    def push(self):
        self.push_no += 1

        queue = deque()
        signal_count = [1, 0]

        for dest in self.modules["broadcaster"].dests:
            queue.append(("broadcaster", dest, 0))

        while queue:
            src, dest, signal = queue.popleft()

            # Part 2
            if (src in self.counter) and (signal == 1) and (self.counter[src] == 0):
                self.counter[src] = self.push_no
            # Part 2

            signal_count[signal] += 1
            if src not in self.modules:
                continue
            queue.extend(self.modules[dest].process(signal, src))

        cur_hash = self.hash()
        if cur_hash in self.cache:
            beg = self.cache[cur_hash]
            return True, beg, *signal_count, self.counter

        self.cache[cur_hash] = self.push_no
        return False, -1, *signal_count, self.counter


def part1(network, N=1000):
    counts = {0: (0, 0)}
    num0, num1 = 0, 0

    for pp in range(1, N + 1):
        is_cycle, beg, s0, s1, _ = network.push()
        num0 += s0
        num1 += s1
        if is_cycle:
            cycle_len = pp - beg
            gain0 = num0 - counts[beg][0]
            gain1 = num1 - counts[beg][1]

            cycle_num = (N - beg) // cycle_len
            pushes_left = N - beg - cycle_num * cycle_len

            total0 = counts[beg][0] + gain0 * cycle_num + (counts[beg + pushes_left][0])
            total1 = counts[beg][1] + gain1 * cycle_num + (counts[beg + pushes_left][1])

            print(counts)
            return total0 * total1
        counts[pp] = (num0, num1)

    return counts[N][0] * counts[N][1]


def part2(network):
    network.reset()
    pp = 0
    while True:
        pp += 1
        _, _, _, _, counter = network.push()
        if all(v != 0 for v in counter.values()):
            return lcm(*counter.values())


if __name__ == "__main__":
    network = Network()
    with open("_inputs/2023/day-20/input.txt") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break
            src, dests = line.split(" -> ")
            dests = [el.strip() for el in dests.split(",")]

            if src[0] == "%":
                network.add(Module(src[1:], 0, dests))
            elif src[0] == "&":
                network.add(Module(src[1:], 1, dests))
            else:
                network.add(Module(src, 2, dests))

        network.finalize()

    # for _ in range(4):
    #     print(network.push())
    #     print(network.cache)
    res1 = part1(network)
    print(f"Part 1: {res1}")

    res2 = part2(network)
    print(f"Part 2: {res2}")
