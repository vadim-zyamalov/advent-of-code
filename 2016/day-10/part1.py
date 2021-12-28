COMMANDS = []

bots = {}
outputs = {}

def parse(commands):
    for line in commands:
        tmp = line.strip().split()
        if tmp[0] == "value":
            if tmp[4] == "bot":
                idx = int(tmp[5])
                if idx not in bots:
                    bots[idx] = {"val": [],
                                "low": (),
                                "high": ()}
                bots[idx]["val"].append(int(tmp[1]))
        elif tmp[0] == "bot":
            idx_0 = int(tmp[1])
            tgt_1 = tmp[5]
            idx_1 = int(tmp[6])
            tgt_2 = tmp[10]
            idx_2 = int(tmp[11])
            if idx_0 not in bots:
                bots[idx_0] = {"val": [],
                            "low": (),
                            "high": ()}
            if tgt_1 == "bot":
                bots[idx_0]["low"] = ("bot", idx_1)
                if idx_1 not in bots:
                    bots[idx_1] = {"val": [],
                                "low": (),
                                "high": ()}
            else:
                bots[idx_0]["low"] = ("out", idx_1)
                if idx_1 not in outputs:
                    outputs[idx_1] = 0
            if tgt_2 == "bot":
                bots[idx_0]["high"] = ("bot", idx_2)
                if idx_2 not in bots:
                    bots[idx_2] = {"val": [],
                                "low": (),
                                "high": ()}
            else:
                bots[idx_0]["high"] = ("out", idx_2)
                if idx_2 not in outputs:
                    outputs[idx_2] = 0


def process(x, y):
    stop = False
    while not stop:
        stop = True
        for idx, bot in bots.items():
            if len(bot["val"]) == 2:
                if x in bot["val"] and y in bot["val"]:
                    print(f"Part 1: {idx}")
                if bot["low"][0] == "bot":
                    if len(bots[bot["low"][1]]["val"]) < 2:
                        stop = False
                        bots[bot["low"][1]]["val"].append(min(bot["val"]))
                else:
                    outputs[bot["low"][1]] = min(bot["val"])
                if bot["high"][0] == "bot":
                    if len(bots[bot["high"][1]]["val"]) < 2:
                        stop = False
                        bots[bot["high"][1]]["val"].append(max(bot["val"]))
                else:
                    outputs[bot["high"][1]] = max(bot["val"])
                bot["val"] = []


with open("./input.txt", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "":
            continue
        COMMANDS.append(line)

parse(COMMANDS)

bots = {k:v for k, v in sorted(bots.items(), key=lambda x: x[0])}
outputs = {k:v for k, v in sorted(outputs.items(), key=lambda x: x[0])}

process(17, 61)

print(f"Part 2: {outputs[0] * outputs[1] * outputs[2]}")
