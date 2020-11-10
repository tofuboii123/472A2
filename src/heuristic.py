import numpy as np


# Compare 2 arrays
def compareArr(arr1, arr2):
    numOfIncorrectPos = 0
    for i in range (len(arr1)):
        if(arr1[i] != arr2[i]):
            numOfIncorrectPos = numOfIncorrectPos + 1 
    return numOfIncorrectPos

# Compare distance of position
def positionCheck(arr1, arr2):
    numOfIncorrect = 0
    # 
    for i in range (len(arr1)):
        for j in range (len(arr1)):
            if(arr1[i] == arr2[j]):
                numOfIncorrect = abs(i - j) + numOfIncorrect
                break
    return numOfIncorrect

def hammingDistance(test_puzzle, goal_states):

    # print("Hamming Distance :")
    #Array to get the number of error per goal state
    errorPerGoalState = []

    #Checking the position of each arrays and append the number of error
    for state in goal_states: 
        error = compareArr(test_puzzle, state)
        errorPerGoalState.append(error)   

    # #Print out the Goal state with the total error of it 
    # for i in range (len(errorPerGoalState)):
    #     print("Goal State " + str(i) + " : " + str(errorPerGoalState[i]))
    
    return min(errorPerGoalState)

# Alternate version of Manhattan heuristic as 1D states instead of 2D
def oneDimensionDistance(test_puzzle, goal_states):
    # print("One Dimension Distance: ")
    #Array to get the number of error per goal state
    errorPerGoalState = []

    #Checking the position of each arrays and append the number of error
    for state in goal_states: 
        error = positionCheck(state, test_puzzle)
        errorPerGoalState.append(error)   

    # #Print out the Goal state with the total error of it 
    # for i in range (len(errorPerGoalState)):
    #     print("Goal State " + str(i) + " : " + str(errorPerGoalState[i]))
    
    return min(errorPerGoalState)
        

# Test Section
# goal_states = [[1, 2, 3, 4, 5, 6, 7, 0], [1, 3, 5, 7, 2, 4, 6, 0]]
# test_puzzle = [1, 2, 3, 4, 5, 6, 0, 7]  

# heuristic.hammingDistance(test_puzzle, goal_states)
# heuristic.oneDimensionDistance(test_puzzle, goal_states)