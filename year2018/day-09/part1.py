from collections import deque


def play(last, players):
    marbles = deque([0])
    pl = 0
    scores = {k: 0 for k in range(players)}

    for mm in range(1, last + 1):
        if mm % 23 == 0:
            marbles.rotate(7)
            mrb = marbles.pop()
            marbles.rotate(-1)
            scores[pl] += mm + mrb
        else:
            marbles.rotate(-1)
            marbles.append(mm)
        pl = (pl + 1) % players

    return max(scores.values())


if __name__ == "__main__":
    with open("_inputs/2018/day-09/input.txt", "r", encoding="utf8") as f:
        for line in f:
            line = line.strip()
            if line == "":
                break

            words = line.split()
            players, last = int(words[0]), int(words[6])
            print(f"Part 1: {play(last, players)}")
            print(f"Part 2: {play(last*100, players)}")
