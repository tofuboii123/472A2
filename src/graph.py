import copy
from heuristic import *

class Graph:

    def __init__(self, goal_states, start_state=None):
        self.start_state = start_state                      # Start node
        self.goal_states = goal_states                      # Goal states
        self.current_state = self.start_state               # Current state of puzzle
        self.zero_position = self.getZeroPosition()         # Tuple (row, col)


    '''
    Get the position of zero
    '''
    def getZeroPosition(self):
        for i, num in enumerate(self.current_state):
            if(num == 0):
                return i


    '''
    Check if the current state is the goal state
    '''
    def goal(self):
        for goal in self.goal_states:
            if(self.current_state == goal):
                return True
        
        return False

    
    '''
    Get all possible children depending on the position
    '''
    def getChildren(self, mode=0):
        self.zero_position = self.getZeroPosition()

        # List of tuples (cost, child_state, parent_state)
        children = []

        # Old zero position                
        # old_zero_pos = (self.zero_position[0], self.zero_position[1])

        # Corner positions
        if self.zero_position == 0:
            new_zero_positions = [self.zero_position + 1,
                                  self.zero_position + 4,
                                  self.zero_position + 3,
                                  self.zero_position + 5,
                                  self.zero_position + 7]
            

            for i, position in enumerate(new_zero_positions):
                
                h = 0
                state_copy = self.current_state.copy() # Deep copy

                if(mode == 0):
                    h = 0
                elif(mode == 1):
                    h = heuristic.hammingDistance(state_copy, self.goal_states)
                elif(mode == 2):
                    h = heuristic.oneDimensionDistance(state_copy, self.goal_states)

                if i < 2:
                    cost = 1 + h
                elif i == 2:
                    cost = 2 + h
                else:
                    cost = 3 + h


                state_copy[position], state_copy[self.zero_position] = state_copy[self.zero_position], state_copy[position]
                children.append((cost, state_copy, self.current_state))

        elif self.zero_position == 4:
            new_zero_positions = [self.zero_position + 1,
                                  self.zero_position - 4,
                                  self.zero_position + 3,
                                  self.zero_position - 3,
                                  self.zero_position - 1]
            
            for i, position in enumerate(new_zero_positions):
                
                h = 0
                state_copy = self.current_state.copy() # Deep copy

                if(mode == 0):
                    h = 0
                elif(mode == 1):
                    h = heuristic.hammingDistance(state_copy, self.goal_states)
                elif(mode == 2):
                    h = heuristic.oneDimensionDistance(state_copy, self.goal_states)

                if i < 2:
                    cost = 1 + h
                elif i == 2:
                    cost = 2 + h
                else:
                    cost = 3 + h

                state_copy[position], state_copy[self.zero_position] = state_copy[self.zero_position], state_copy[position]
                children.append((cost, state_copy, self.current_state))

        elif self.zero_position == 3:
            new_zero_positions = [self.zero_position - 1,
                                  self.zero_position + 4,
                                  self.zero_position - 3,
                                  self.zero_position + 3,
                                  self.zero_position + 1]
            
            for i, position in enumerate(new_zero_positions):
                
                h = 0
                state_copy = self.current_state.copy() # Deep copy

                if(mode == 0):
                    h = 0
                elif(mode == 1):
                    h = heuristic.hammingDistance(state_copy, self.goal_states)
                elif(mode == 2):
                    h = heuristic.oneDimensionDistance(state_copy, self.goal_states)

                if i < 2:
                    cost = 1 + h
                elif i == 2:
                    cost = 2 + h
                else:
                    cost = 3 + h

                state_copy[position], state_copy[self.zero_position] = state_copy[self.zero_position], state_copy[position]
                children.append((cost, state_copy, self.current_state))

        elif self.zero_position == 7:
            new_zero_positions = [self.zero_position - 1,
                                  self.zero_position - 4,
                                  self.zero_position - 3,
                                  self.zero_position - 5,
                                  self.zero_position - 7]
            
            for i, position in enumerate(new_zero_positions):
                
                h = 0
                state_copy = self.current_state.copy() # Deep copy

                if(mode == 0):
                    h = 0
                elif(mode == 1):
                    h = heuristic.hammingDistance(state_copy, self.goal_states)
                elif(mode == 2):
                    h = heuristic.oneDimensionDistance(state_copy, self.goal_states)

                if i < 2:
                    cost = 1 + h
                elif i == 2:
                    cost = 2 + h
                else:
                    cost = 3 + h

                state_copy[position], state_copy[self.zero_position] = state_copy[self.zero_position], state_copy[position]
                children.append((cost, state_copy, self.current_state))
        else:
            h = 0
            state_copy = self.current_state.copy()
            if(mode == 0):
                h = 0
            elif(mode == 1):
                h = heuristic.hammingDistance(state_copy, self.goal_states)
            elif(mode == 2):
                h = heuristic.oneDimensionDistance(state_copy, self.goal_states)

            cost = 1 + h

            # The possible new positions for the 0 tile
            new_zero_positions = [self.zero_position + 1,
                                  self.zero_position - 1,
                                  self.zero_position + 4 if self.zero_position < 3 else self.zero_position - 4]

            # Get all possible children and swap the positions.
            for i, position in enumerate(new_zero_positions):
                state_copy = self.current_state.copy() # Deep copy

                # Swap positions
                state_copy[position], state_copy[self.zero_position] = state_copy[self.zero_position], state_copy[position]
                
                children.append((cost, state_copy, self.current_state))

        return children