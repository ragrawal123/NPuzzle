def LoadFromFile(filepath):
    with open(filepath, "r") as f:
        n = int(next(f))
        board = []
        for line in f:
            line = line.strip()
            line = line.split()
            board.append(line)

        return board

def DebugPrint(state):
    s = ""
    for element in state:
        for number in element:
            s += number + "    "
        print(s)
        s = ""

def ComputeNeighbors(state):
    (row,col) = findHole(state)
    collection = []
    n = len(state)
    adjacent_indices = [(row+i, col+j) for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    valid = []
    for pair in adjacent_indices:
        if validIndex(pair,n):
            valid.append(pair)
    for pairs in valid:
        (r,c) = pairs
        value = state[r][c]
        newState = []
        for element in state:
            for number in element:
                if number == value:
                    number = "*"
                elif number == "*":
                    number = value
                newState.append(number)
        collection.append((value, newState))
    print(collection)

def findHole(state):
    for (r, row) in enumerate(state):
        for (c, element) in enumerate(row):
            if element == "*":
                return (r,c)

def validIndex(t,n):
    (r,c) = t
    return r <=n-1 and c <= n-1 and r >= 0 and c >= 0
        
def isGoal(state):
    # largest = 0
    # for element in state:
    #     if element !< largest:
    #         return False
    #     elif element == "*":
    #         return False
    #     else:
    #         largest = element
    # return True

def main():
    b = LoadFromFile("test.txt")
    DebugPrint(b)
    ComputeNeighbors(b)

main()