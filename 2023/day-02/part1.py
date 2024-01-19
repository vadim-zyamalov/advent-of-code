RGB = (12, 13, 14)
RGBnames = ["red", "green", "blue"]


def check_game(game: tuple[list[int]]) -> bool:
    for i, v in enumerate(RGB):
        if any(el > v for el in game[i]):
            return False
    return True


def power_game(game: tuple[list[int]]) -> int:
    res = 1
    for v in game:
        res *= max(v)
    return res


if __name__ == "__main__":
    GAMES = {}
    with open("_inputs/2023/day-02/input.txt", "r", encoding="utf8") as f:
        for line in f:
            balls = ([], [], [])
            game_id, game = line.strip().split(":")
            game_id = int(game_id.split()[1])
            for turn in game.strip().split(";"):
                turn_RGB = [0, 0, 0]
                for bb in turn.strip().split(","):
                    n, col = bb.strip().split()
                    turn_RGB[RGBnames.index(col)] = int(n)
                for i, v in enumerate(turn_RGB):
                    balls[i].append(v)
                GAMES[game_id] = balls

    total = 0
    power = 0
    for game_id, balls in GAMES.items():
        if check_game(balls):
            total += game_id
        power += power_game(balls)

    print(f"Part 1: {total}")
    print(f"Part 2: {power}")
