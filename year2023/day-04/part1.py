CARDS = {}

if __name__ == "__main__":
    res1 = 0

    with open("_inputs/2023/day-04/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break

            card_id, card = line.split(":")
            card_id = int(card_id.strip().split()[1])
            if card_id not in CARDS:
                CARDS[card_id] = 1

            win, nums = card.strip().split("|")
            win = [int(el) for el in win.strip().split()]
            nums = [int(el) for el in nums.strip().split()]

            inter = sum(1 for el in nums if el in win)

            for i in range(card_id + 1, card_id + inter + 1):
                if i not in CARDS:
                    CARDS[i] = 1
                CARDS[i] += CARDS[card_id]

            if inter > 0:
                res1 += 2 ** (inter - 1)

    print(f"Part 1: {res1}")
    print(f"Part 2: {sum(v for v in CARDS.values())}")
