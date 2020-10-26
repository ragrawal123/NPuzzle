import copy
def main():
    b = LoadFromFile("test.txt")
    DebugPrint(b)
    print(BFS(b))
    #print(DFS(b))
    print(bidirectionalsearch(b))

#arguments: file
#returns: 2d tuple of board
def LoadFromFile(filepath):
    board = []
    n = 0
    with open(filepath, 'r') as file:
        count = 0
        for line in file:
            line1 = []
            if count == 0:
                n = file
            else:
                row = line.strip().split("\t")
                for element in row:
                    if element == "*":
                        line1.append("0")
                    else:
                        line1.append(element)
                board.append(tuple(line1))
            count += 1
    return tuple(board)

#arguments: 2d tuple of board
#returns: nothing, prints out board
def DebugPrint(state):
    s = ""
    for element in state:
        for number in element:
            s += number + "    "
        print(s)
        s = ""
#arguments: 2d tuple of board
#returns: 2d tuple of board
def FindHole(state):
    for i in range(len(state)):
        for j in range(len(state)):
            if state[i][j] == "0":
                return tuple([i, j])

#arguments: 2d tuple of board, tuple pair of hole location, tuple pair being switched
#returns: 2d tuple of board
def switch(state, hole, switched):
    newState = list(list(row) for row in copy.deepcopy(state))
    hole_row, hole_col = hole
    switch_row, switch_col = switched
    newState[hole_row][hole_col], newState[switch_row][switch_col] = newState[switch_row][switch_col], newState[hole_row][hole_col]
    return tuple(tuple(row) for row in newState)


#arguments: 2d tuple of board
#returns: 2d tuple of resulting neighbor moves, ((int, 1d list))
def ComputeNeighbors(state):
    value = []
    hole = []
    hole = FindHole(state)
    row, col = hole
    #check above
    if row - 1 >= 0:
        value.append([state[row - 1][col], switch(state, hole, (row - 1, col))])
    #below
    if row + 1 <= len(state) -1:
        value.append([state[row + 1][col], switch(state, hole, (row + 1, col))])
    #left
    if col - 1 >= 0:
        value.append([state[row][col - 1], switch(state, hole, (row, col - 1))])
    #right
    if col + 1 <= len(state) -1:
        value.append([state[row][col + 1], switch(state, hole, (row, col + 1))])

    return value

#arguments: 2d tuple of board
#returns: return True/False, is the state the goal state
def IsGoal(state):
    position = 0
    n = len(state)
    for i in range(n):
        for j in range(n):
            if not int(state[i][j]) == position + 1:
                return False
            if i == n-1 and j == n-2:
                return True
            position += 1


#arguments: 2d tuple of board
#returns: 1d array of tile path to reach goal
def BFS(state):
    frontier = [(0, state)]
    discovered = set(state)
    parents = {(0, state): None}
    path = []
    while len(frontier) != 0:
        current_state = frontier.pop(0)
        discovered.add(current_state[1])
        if IsGoal(current_state[1]):
            while parents.get((current_state[0], current_state[1])) != None:
                path.insert(0, current_state[0])
                current_state = parents.get((current_state[0], current_state[1]))
            return path
        for neighbor in ComputeNeighbors(current_state[1]):
            if neighbor[1] not in discovered:
                frontier.append(neighbor)
                discovered.add(neighbor[1])
                parents.update({(neighbor[0], neighbor[1]): current_state})
    print("FAIL")
    return None

#arguments: 2d tuple of board
#returns: 1d array of tile path to reach goal
def DFS(state):
    frontier = [(0, state)]
    discovered = set(state)
    parents = {(0, state): None}
    path = []
    while len(frontier) != 0:
        current_state = frontier.pop(0)
        discovered.add(current_state[1])
        if IsGoal(current_state[1]):
            while parents.get((current_state[0], current_state[1])) != None:
                path.insert(0, current_state[0])
                current_state = parents.get((current_state[0], current_state[1]))
            return path
        for neighbor in ComputeNeighbors(current_state[1]):
            if neighbor[1] not in discovered:
                frontier.insert(0, neighbor)
                discovered.add(neighbor[1])
                parents.update({(neighbor[0], neighbor[1]): current_state})
    print("FAIL")
    return None

#arguments: len of state, int
#returns: 2d tuple of goal board
def findGoal(n):
    Total = n**2
    count = 1
    End_state = []
    for i in range(n):
        row = []
        for j in range(n):
            if count == Total:
                row.append("0")
            else:
                row.append(str(count))
            count+=1
        End_state.append(tuple(row))
    
    return tuple(End_state)

#arguments: 2d tuple of board
#returns: 1d array of tile path to reach goal
def bidirectionalsearch(state):
    Goal = findGoal(len(state))
    frontier1 = [(0, state)]
    frontier2 = [(0, Goal)]
    discovered1 = set(state)
    discovered2 = set(Goal)
    parents1 = {(0, state): None}
    parents2 = {(0, Goal): None}
    path = []

    while frontier1 and frontier2:
    #while len(frontier1) != 0 or len(frontier2) != 0:
        current_state1 = frontier1.pop(0)
        current_state2 = frontier2.pop(0)
        discovered1.add(current_state1[1])
        discovered2.add(current_state2[1])
        intersection = discovered1.intersection(discovered2)

        if(len(intersection) > 0):
#            intersectionPoint = intersection[0]
#            forwardPath = parents1[intersectionPoint]
#            backwardsPath = list(reversed(parents2[intersectionPoint]))
#            return forwardPath + backwardsPath
            if IsGoal(current_state1[1]):
                while parents1.get((current_state1[0], current_state1[1])) != None:
                    path.insert(0, current_state1[0])
                    current_state1 = parents1.get((current_state1[0], current_state1[1]))
            else:
                while parents2.get((current_state2[0], current_state2[1])) != None:
                    path.insert(0, current_state2[0])
                    current_state2 = parents2.get((current_state2[0], current_state2[1]))
            return path
        for neighbor in ComputeNeighbors(current_state1[1]):
            if neighbor[1] not in discovered1:
                frontier1.append(neighbor)
                discovered1.add(neighbor[1])
                parents1.update({(neighbor[0], neighbor[1]): current_state2})
                #parents1[neighbor[1]] = (neighbor[0], current_state1[1])

        for neighbor in ComputeNeighbors(current_state2[1]):
            if neighbor[1] not in discovered2:
                frontier2.append(neighbor)
                discovered2.add(neighbor[1])
                parents2.update({(neighbor[0], neighbor[1]): current_state2})
                #print("Hello")
                #print("cool")
                #parents2[neighbor[1]] = (neighbor[0], current_state2[1])
    print("FAIL")
    return None


main()