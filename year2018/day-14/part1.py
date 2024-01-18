import time


def step(i, j, board):
    next_scores = divmod(board[i] + board[j], 10)
    if next_scores[0] != 0:
        board.append(next_scores[0])
    board.append(next_scores[1])
    return (i + 1 + board[i]) % len(board), (j + 1 + board[j]) % len(board)


if __name__ == "__main__":
    # data = "9"
    # data = "51589"
    # data = "01245"
    data = "074501"
    steps = int(data, 10)
    data = [int(c) for c in data]

    t0 = time.time()
    board = [3, 7]
    i, j = 0, 1
    while len(board) < steps + 10:
        i, j = step(i, j, board)
    result = "".join(str(board[i]) for i in range(steps, steps + 10))
    print(f"Part 1: {result}")
    print(f"    took {time.time() - t0:.2f} secs")

    t0 = time.time()
    board = [3, 7]
    i, j = 0, 1
    while (board[-len(data) :] != data) and (board[-len(data) - 1 : -1] != data):
        i, j = step(i, j, board)

    result = len(board) - len(data) - (board[-len(data) :] != data)
    print(f"Part 2: {result}")
    print(f"    took {time.time() - t0:.2f} secs")
