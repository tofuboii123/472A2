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

def boardCheck(x):
    p1 = x[:4]
    p2 = x[4:]
    print(p1, end='\n')
    print(p2)


def newCheck(arr1, arr2):
    """
    checks distance between arrays
    :param arr1: int list - to be checked
    :param arr2: int list - correct copy
    :return: int
    """
    # print('NEW CHECK')
    numIncorrect = 0
    arr1 = [8 if x == 0 else x for x in arr1]
    arr1Top, arr1Bot = arr1[:4], arr1[4:]
    # print(arr1Top)
    # print(arr1Bot)

    # print('--')
    numIncorrect += checkHelper(arr1Top)
    # print('--')
    numIncorrect += checkHelper(arr1Bot, False)
    arr1 = [0 if x == 8 else x for x in arr1]
    # print('num incorrect:', numIncorrect)
    return numIncorrect


def checkHelper(arr, isTop=True):
    numIncorrect = 0
    for i in range(len(arr)):
        incCounter = 0
        # print('val:', arr[i])
        if isTop:
            if arr[i] - 4 > 0:
                incCounter += 1
                arr[i] -= 4
                # print('\tshift row: +1')
        else:
            if arr[i] - 4 > 0:
                arr[i] -= 4

            else:
                incCounter += 1
                # print('\tshift row: +1')
        dist = abs(arr[i] - (i+1))
        dist = 1 if dist == 3 else dist
        incCounter += dist
        # print('\tnew val:', arr[i], ' - index:', i+1, ' - distance: +', dist)
        # print('\tincorrect:+', incCounter)
        numIncorrect += incCounter
    return numIncorrect

# Naive heuristic returns 0 if last position is 0
def naive(test_puzzle):
    if test_puzzle[7] == 0:
        return 0
    else:
        return 1

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

# Order check 
def orderCheck(test_puzzle):
    numOfIncorrect = 0
    for i in range(1,4):
        if test_puzzle[i] >= test_puzzle [i+1]:
            numOfIncorrect += 1
            #print("wrong")
    for i in range(4,7):
        if test_puzzle[i] >= test_puzzle[i+1]:
            numOfIncorrect += 1 
            #print("wrong")
    return numOfIncorrect

# # Compare 2 arrays
# def compareArr(arr1, arr2):
#     numOfIncorrectPos = 0
#     for i in range (len(arr1)):
#         if(arr1[i] != arr2[i]):
#             numOfIncorrectPos = numOfIncorrectPos + 1 
#     return numOfIncorrectPos
        

# Test Section
# goal_states = [[1, 2, 3, 4, 5, 6, 7, 0], [1, 3, 5, 7, 2, 4, 6, 0]]
# test_puzzle = [1, 3, 2, 4, 5, 7, 0, 6]  

# heuristic.hammingDistance(test_puzzle, goal_states)
# heuristic.oneDimensionDistance(test_puzzle, goal_states)
# print(orderCheck(test_puzzle))