rounds = 20

monkeys = {}
monkeys_indices = []
cur_monkey = -1

with open("./input.txt", "r", encoding="utf8") as f:
    for line in f:
        if line.strip() == "":
            continue
        fst, snd = line.strip().split(":")
        fst = fst.split()
        match fst[0]:
            case "Monkey":
                cur_monkey = int(fst[1])
                monkeys_indices.append(cur_monkey)
                if cur_monkey not in monkeys:
                    monkeys[cur_monkey] = {
                        "items": [],
                        "oper": None,
                        "test": -1,
                        "true": -1,
                        "false": -1,
                        "N": 0
                    }
            case "Starting":
                monkeys[cur_monkey]["items"] = \
                    [int(i) for i in snd.strip().split(",")]
            case "Operation":
                snd = snd.split()
                match snd[3]:
                    case "+":
                        if snd[4] == "old":
                            monkeys[cur_monkey]["oper"] = \
                                lambda x: x + x
                        else:
                            monkeys[cur_monkey]["oper"] = \
                                (lambda p: lambda x: x + p)(int(snd[4]))
                    case "-":
                        if snd[4] == "old":
                            monkeys[cur_monkey]["oper"] = \
                                lambda x: x - x
                        else:
                            monkeys[cur_monkey]["oper"] = \
                                (lambda p: lambda x: x - p)(int(snd[4]))
                    case "*":
                        if snd[4] == "old":
                            monkeys[cur_monkey]["oper"] = \
                                lambda x: x * x
                        else:
                            monkeys[cur_monkey]["oper"] = \
                                (lambda p: lambda x: x * p)(int(snd[4]))
                    case "/":
                        if snd[4] == "old":
                            monkeys[cur_monkey]["oper"] = \
                                lambda x: x / x
                        else:
                            monkeys[cur_monkey]["oper"] = \
                                (lambda p: lambda x: x / p)(int(snd[4]))
            case "Test":
                snd = snd.split()
                monkeys[cur_monkey]["test"] = int(snd[2])
            case "If":
                snd = snd.split()
                if fst[1] == "true":
                    monkeys[cur_monkey]["true"] = int(snd[3])
                else:
                    monkeys[cur_monkey]["false"] = int(snd[3])

monkeys_indices.sort()

for i in range(rounds):
    for m in monkeys_indices:
        while len(monkeys[m]["items"]) > 0:
            monkeys[m]["N"] += 1
            new_item = monkeys[m]["oper"](monkeys[m]["items"][0]) // 3
            if new_item % monkeys[m]["test"] == 0:
                monkeys[monkeys[m]["true"]]["items"].append(new_item)
            else:
                monkeys[monkeys[m]["false"]]["items"].append(new_item)
            monkeys[m]["items"] = monkeys[m]["items"][1:]

res = [monkeys[m]["N"] for m in monkeys]
res.sort()

print(f"Part 1: {res[-1] * res[-2]}")
