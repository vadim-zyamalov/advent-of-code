numbers = []
boards = {}


def fill(number, boards=boards):
    for k in boards:
        for i in range(5):
            for j in range(5):
                if boards[k][i][j] is not None and \
                   boards[k][i][j] == number:
                    boards[k][i][j] = None
    return boards


def check(boards=boards):
    winners = []
    for k in boards:
        # Check row
        next = False
        if not next:
            for i in range(5):
                if all(boards[k][i][j] is None for j in range(5)):
                    winners.append(k)
                    next = True
                    break
        # Check col
        if not next:
            for j in range(5):
                if all(boards[k][i][j] is None for i in range(5)):
                    winners.append(k)
                    break
    return winners


def score(board):
    ans = 0
    for i in range(5):
        for j in range(5):
            if board[i][j] is not None:
                ans += board[i][j]
    return ans


with open("input.txt", "r") as f:
    line = f.readline()
    numbers = [int(i) for i in line.strip().split(',')]

    _ = f.readline()

    count = 0
    board = []
    for line in f:
        if line.strip() == '':
            boards[count] = board
            board = []
            count += 1
        else:
            board.append([
                int(i) for i in line.strip().split()
            ])
    boards[count] = board

winners = []
for i in numbers:
    boards = fill(i, boards)
    winners = check(boards)
    if winners and len(boards) > 1:
        for i in winners:
            del boards[i]
    elif winners:
        res = i * max([score(boards[i]) for i in boards.keys()])
        break

print("Part 2: {}".format(res))
