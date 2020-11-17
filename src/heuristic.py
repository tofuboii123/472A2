# Compare 2 arrays used for hammingDistance
def compareArr(arr1, arr2):
    numOfIncorrectPos = 0
    for i in range (len(arr1)):
        if(arr1[i] != arr2[i]):
            numOfIncorrectPos = numOfIncorrectPos + 1 
    return numOfIncorrectPos

# Compare distance of position in 1D for OneDimensionDistance
def positionCheck(arr1, arr2):
    numOfIncorrect = 0
    # 
    for i in range (len(arr1)):
        for j in range (len(arr1)):
            if(arr1[i] == arr2[j]):
                numOfIncorrect = abs(i - j) + numOfIncorrect
                break
    return numOfIncorrect

# 0 - Naive heuristic returns 0 if last position is 0
def naive(test_puzzle):
    if test_puzzle[7] == 0:
        return 0
    else:
        return 1

# 1 - Order check heuristic, checks if value is smaller then the next 
def orderCheck(test_puzzle):
    numOfIncorrect = 0

    # First row check
    for i in range(0, len(test_puzzle)//2):
        if test_puzzle[i] >= test_puzzle [i+1]:
            numOfIncorrect += 1

    # Second row check
    for i in range(len(test_puzzle)//2, len(test_puzzle) - 1):
        if test_puzzle[i] >= test_puzzle[i+1]:
            numOfIncorrect += 1 

    return numOfIncorrect

# 2 - Row Column Check heuristic, check if the number is in the rows and column
def rowcolCheck(test_puzzle, goal_states):
    numIncorrect = 0
    numCorrect = 0
    errorPerGoalState = []
    errorPerGoalStateRow = []
    errorPerGoalStateCol = []

    # Checks for each goal state
    for state in goal_states:
        # Row Check 1
        for i in range(0, len(state)//2):
            for j in range(0, len(state)//2):
                if (state[i] == test_puzzle[j]):
                    numCorrect += 1
            numIncorrect += 1
        
        # Row Check 2
        for i in range (len(state)//2, len(state)):
            for j in range (len(state)//2, len(state)):
                if(state[i] == test_puzzle[j]):
                    numCorrect += 1
            numIncorrect += 1

        numIncorrect = abs(numIncorrect - numCorrect)
        errorPerGoalStateRow.append(abs(numIncorrect))

    # Check for each goal state
    for state in goal_states:
        numIncorrect = 0
        # Column check 1
        for i in range(0, len(state)//2):
            if test_puzzle[i] not in (state[i], state[i + len(state)//2]):
                numIncorrect += 1
    
        tempVar = 0 
        # Column check 1
        for i in range(len(state)//2, len(state)): 
            if test_puzzle[i] not in (state[tempVar], state[tempVar + len(state)//2]):
                numIncorrect += 1
            tempVar += 1
        errorPerGoalStateCol.append(numIncorrect)
    
    # Add both values of rows and columns found
    for i in range(len(errorPerGoalStateCol)):
        errorPerGoalState.append(errorPerGoalStateRow[i] + errorPerGoalStateCol[i])

    return min(errorPerGoalState)

# 3 - Hamming Distance calculate tiles out of place
def hammingDistance(test_puzzle, goal_states):
    # Array to get the number of error per goal state
    errorPerGoalState = []

    # Checking the position of each arrays and append the number of error
    for state in goal_states: 
        error = compareArr(test_puzzle, state)
        errorPerGoalState.append(error)   
    
    return min(errorPerGoalState)

# 4 - Alternate version of Manhattan heuristic as 1D states instead of 2D
def oneDimensionDistance(test_puzzle, goal_states):

    #Array to get the number of error per goal state
    errorPerGoalState = []

    #Checking the position of each arrays and append the number of error
    for state in goal_states: 
        error = positionCheck(state, test_puzzle)
        errorPerGoalState.append(error)   

    return min(errorPerGoalState)
