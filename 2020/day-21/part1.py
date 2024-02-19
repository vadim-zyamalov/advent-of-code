if __name__ == "__main__":
    with open("_inputs/2020/day-21/input.txt", "r", encoding="utf8") as f:
        lines = f.read().strip().split("\n")

    data = []
    for i, line in enumerate(lines):
        line = line.strip(")")
        lst0, lst1 = line.split("(contains ")
        lst0 = set(lst0.strip().split())
        lst1 = set(lst1.replace(" ", "").strip().split(","))
        data.append((lst0, lst1))

    all_ingredients, all_allergens = (set.union(*s) for s in zip(*data))

    filtered = {
        k: set.intersection(*(ings for ings, alls in data if k in alls))
        for k in all_allergens
    }

    allergens = {}
    while filtered:
        allergen, ingredient = next(
            (k, v) for k, v in filtered.items() if len(v) == 1
        )
        allergens[allergen] = list(ingredient)[0]
        filtered.pop(allergen)
        for k in filtered:
            filtered[k] -= ingredient

    res0 = sum(len(v - set(allergens.values())) for v, _ in data)
    print(f"Part 1: {res0}")

    res1 = ",".join(allergens[k] for k in sorted(all_allergens))
    print(f"Part 2: {res1}")
