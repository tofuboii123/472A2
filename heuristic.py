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
            for j in range (len(arr1[i])):
                goalX = np.asarray(np.where(arr1 == arr1[i][j]))[0][0]
                goalY = np.asarray(np.where(arr1 == arr1[i][j]))[1][0]
                testX = np.asarray(np.where(arr2 == arr1[i][j]))[0][0]
                testY = np.asarray(np.where(arr2 == arr1[i][j]))[1][0]

                numOfIncorrect = abs(goalX - testX) + abs(goalY - testY) + numOfIncorrect
        return numOfIncorrect

    def hammingDistance(self, test_puzzle, goal_states):

        print("Hamming Distance :")
        #Array to get the number of error per goal state
        errorPerGoalState = []

        #Checking the position of each arrays and append the number of error
        for i in range (len(goal_states)): 
            error = 0
            for j in range (len(goal_states[i])):
                error = error + self.compareArr(test_puzzle[j], goal_states[i][j])
            errorPerGoalState.append(error)   

        #Print out the Goal state with the total error of it 
        for i in range (len(errorPerGoalState)):
            print("Goal State " + str(i) + " : " + str(errorPerGoalState[i]))

    # Calculate the total to arrive to goal state
    def manhattanDistance(self, test_puzzle, goal_states):
        print("Manhattan Distance: ")
        #Array to get the number of error per goal state
        errorPerGoalState = []

        #Checking the position of each arrays and append the number of error
        for i in range (len(goal_states)): 
            error = self.positionCheck(goal_states[i], test_puzzle)
            errorPerGoalState.append(error)   

        #Print out the Goal state with the total error of it 
        for i in range (len(errorPerGoalState)):
            print("Goal State " + str(i) + " : " + str(errorPerGoalState[i]))
        
test_puzzle = np.array([[1, 2, 3, 4], [5, 6, 0, 7]])  
goal_states = np.array([[[1, 2, 3, 4], [5, 6, 7, 0]], [[1, 3, 5, 7], [2, 4, 6, 0]]])
h = heuristic()
h.hammingDistance(test_puzzle, goal_states)
h.manhattanDistance(test_puzzle, goal_states)