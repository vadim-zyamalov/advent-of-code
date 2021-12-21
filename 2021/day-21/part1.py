from itertools import cycle
import time

DICE = list(range(1, 101))
SUMS = {3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1}

def practice_play(positions, scores, limit):
    dice_throwing = cycle(DICE)
    player = 0
    throws = 0
    while all(el < limit for el in scores):
        d_0 = next(dice_throwing)
        d_1 = next(dice_throwing)
        d_2 = next(dice_throwing)
        throws += 3
        if player == 0:
            positions = ((positions[0] + d_0 + d_1 + d_2 - 1) % 10 + 1,
                         positions[1])
            scores = (scores[0] + positions[0],
                      scores[1])
        else:
            positions = (positions[0],
                         (positions[1] + d_0 + d_1 + d_2 - 1) % 10 + 1)
            scores = (scores[0],
                      scores[1] + positions[1])
        player = (player + 1) % 2
    return (positions, scores, throws)


def dirac_play_linear(current_player, positions, scores, limit, mult=1):
    result = [0, 0]
    queue = [(current_player,
              positions,
              scores,
              mult)]
    while len(queue) > 0:
        tmp = queue.pop()
        for dsum, num in SUMS.items():
            loop_player, loop_positions, loop_scores, loop_mult = tmp
            if loop_player == 0:
                loop_positions = ((loop_positions[0] + dsum - 1) % 10 + 1,
                                  loop_positions[1])
                loop_scores = (loop_scores[0] + loop_positions[0],
                               loop_scores[1])
            else:
                loop_positions = (loop_positions[0],
                                  (loop_positions[1] + dsum - 1) % 10 + 1)
                loop_scores = (loop_scores[0],
                               loop_scores[1] + loop_positions[1])
            if loop_scores[loop_player] >= limit:
                result[loop_player] += loop_mult * num
            else:
                queue.append(((loop_player + 1) % 2,
                              loop_positions,
                              loop_scores,
                              loop_mult * num))
    return result


def dirac_play_recursive(current_player, positions, scores, limit, mult=1):
    if scores[0] >= limit:
        return [mult, 0]
    if scores[1] >= limit:
        return [0, mult]
    result = [0, 0]
    for dsum, num in SUMS.items():
        loop_positions = positions
        loop_scores = scores
        if current_player == 0:
            loop_positions = ((loop_positions[0] + dsum - 1) % 10 + 1,
                              loop_positions[1])
            loop_scores = (loop_scores[0] + loop_positions[0],
                           loop_scores[1])
        else:
            loop_positions = (loop_positions[0],
                              (loop_positions[1] + dsum - 1) % 10 + 1)
            loop_scores = (loop_scores[0],
                           loop_scores[1] + loop_positions[1])
        tmp = dirac_play_recursive((current_player + 1) % 2,
                         loop_positions,
                         loop_scores,
                         limit,
                         mult * num)
        result[0] += tmp[0]
        result[1] += tmp[1]
    return result


with open("input.txt", "r", encoding="utf-8") as f:
    pos_0 = int(f.readline().strip().split(": ")[1])
    pos_1 = int(f.readline().strip().split(": ")[1])

t_0 = time.time()
answer = practice_play((pos_0, pos_1), (0, 0), 1000)
print(f"Part 1: {min(answer[1]) * answer[2]}")
print(f"  elapsed in {time.time() - t_0:.2f} seconds")

t_0 = time.time()
answer = dirac_play_recursive(0, (pos_0, pos_1), (0, 0), 21)
print(f"Part 2: {max(answer)}")
print(f"  elapsed in {time.time() - t_0:.2f} seconds")

t_0 = time.time()
answer = dirac_play_linear(0, (pos_0, pos_1), (0, 0), 21)
print(f"Part 2: {max(answer)}")
print(f"  elapsed in {time.time() - t_0:.2f} seconds")
