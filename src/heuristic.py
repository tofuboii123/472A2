import numpy as np

class heuristic:

    # Compare 2 arrays
    def compareArr(self, arr1, arr2):
        numOfIncorrectPos = 0
        for i in range (len(arr1)):
            if(arr1[i] != arr2[i]):
                numOfIncorrectPos = numOfIncorrectPos + 1 
        return numOfIncorrectPos

    # Compare distance of position
    def positionCheck(self, arr1, arr2):
        numOfIncorrect = 0
        # i=x y=j how far it takes to get there  goalx(end goal) - testx(current)
        for i in range (len(arr1)):
            for j in range (len(arr1)):
                if(arr1[i] == arr2[j]):
                    numOfIncorrect = abs(i - j) + numOfIncorrect
                    break
        return numOfIncorrect

    def hammingDistance(self, test_puzzle, goal_states):

        print("Hamming Distance :")
        #Array to get the number of error per goal state
        errorPerGoalState = []

        #Checking the position of each arrays and append the number of error
        for i in range (len(goal_states)): 
            error = self.compareArr(test_puzzle, goal_states[i])
            errorPerGoalState.append(error)   

        #Print out the Goal state with the total error of it 
        for i in range (len(errorPerGoalState)):
            print("Goal State " + str(i) + " : " + str(errorPerGoalState[i]))

    # Alternate version of Manhattan heuristic as 1D states instead of 2D
    def oneDimensionDistance(self, test_puzzle, goal_states):
        print("One Dimension Distance: ")
        #Array to get the number of error per goal state
        errorPerGoalState = []

        #Checking the position of each arrays and append the number of error
        for i in range (len(goal_states)): 
            error = self.positionCheck(goal_states[i], test_puzzle)
            errorPerGoalState.append(error)   

        #Print out the Goal state with the total error of it 
        for i in range (len(errorPerGoalState)):
            print("Goal State " + str(i) + " : " + str(errorPerGoalState[i]))
        

# Test Section
goal_states = [[1, 2, 3, 4, 5, 6, 7, 0], [1, 3, 5, 7, 2, 4, 6, 0]]
test_puzzle = [1, 2, 3, 4, 5, 6, 0, 7]  

h = heuristic()
h.hammingDistance(test_puzzle, goal_states)
h.oneDimensionDistance(test_puzzle, goal_states)