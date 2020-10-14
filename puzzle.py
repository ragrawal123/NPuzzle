with open("test.txt", "r") as f:
    n = int(next(f))
    board = [[],[],[],[]]
    row = 0
    for line in f:
        print(line)
        line.strip()
        print(line)
        for col in range(0,n):
            board[row][col] = line[col]
        row += 1
    print(board)