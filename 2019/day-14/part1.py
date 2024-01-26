from collections import defaultdict


def parse(lines):
    result = {}

    for line in lines:
        ins, out = line.split(" => ")

        quantity, name = out.strip().split()
        quantity = int(quantity)
        result[name] = {"n": quantity}

        for ingredient in ins.split(","):
            quantity, ingredient = ingredient.strip().split()
            quantity = int(quantity)
            result[name][ingredient] = quantity

    return result


def ore_quantity(recipes, fuel=1):
    production = defaultdict(int)
    surplus = defaultdict(int)
    ores = set()

    queue = [("FUEL", fuel)]

    while queue:
        cur, cur_prod = queue.pop(0)
        if cur == "ORE":
            production[cur] += cur_prod
            continue

        recipe_prod = recipes[cur]["n"]

        nrec, nsurp = divmod(cur_prod - surplus[cur], recipe_prod)
        if nsurp > 0:
            nrec += 1
            surplus[cur] += nrec * recipe_prod - cur_prod
        else:
            surplus[cur] = 0

        production[cur] += nrec * recipe_prod

        for ingredient, quant_needed in recipes[cur].items():
            if ingredient in ["n"]:
                continue
            queue.append((ingredient, nrec * quant_needed))

    # result = 0
    # for cur in ores:
    #     result += production[cur] // recipes[cur]["n"] * recipes[cur]["ORE"]

    return production["ORE"]


def fuel(recipes, max_ores=1_000_000_000_000):
    single_ore = ore_quantity(recipes)
    max_fuel = max_ores // single_ore

    while (needed_ore := ore_quantity(recipes, max_fuel)) <= max_ores:
        ore_surplus = max_ores - needed_ore
        ore_step = ore_surplus // single_ore
        max_fuel += ore_step if ore_step > 0 else 1

    return max_fuel - 1


if __name__ == "__main__":
    with open("_inputs/2019/day-14/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n")

    recipes = parse(lines)
    print(f"Part 1: {ore_quantity(recipes)}")
    fuels = fuel(recipes)
    print(f"Part 2: {fuels}")
