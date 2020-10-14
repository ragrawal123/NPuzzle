with open("test.txt", "r") as f:
    n = int(next(f))
    board = []
    for line in f:
        line = line.strip()
        line = line.split()
        board.append(line)

    print(board)