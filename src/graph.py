import copy
from heuristic import *

class Graph:

    def __init__(self, goal_states, size, start_state=None):
        self.start_state = start_state                      # Start node
        self.goal_states = goal_states                      # Goal states
        self.current_state = self.start_state               # Current state of puzzle
        self.zero_position = self.getZeroPosition()
        self.size = size         


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

        # Heuristic for each children
        h = []
        g = [1, 2, 3]
        cost = 0
        hx = 0
        new_zero_positions = None

        # Corner positions
        if self.zero_position == 0:
            new_zero_positions = [self.zero_position + 1,
                                  self.zero_position + (self.size//2),
                                  self.zero_position + (self.size//2 - 1),
                                  self.zero_position + (self.size//2 + 1),
                                  self.zero_position + (self.size//2 - 1)]
            
            for i, position in enumerate(new_zero_positions):
                state_copy = self.current_state.copy() # Deep copy

                if(mode == 0):
                    hx = 0
                elif(mode == 1):
                    hx = hammingDistance(state_copy, self.goal_states)
                elif(mode == 2):
                    hx = oneDimensionDistance(state_copy, self.goal_states)

                h.append(hx)

                if i < 2:
                    cost = g[0]
                    fx = cost + hx
                elif i == 2:
                    cost = g[1]
                    fx = cost + hx
                else:
                    cost = g[2]
                    fx = cost + hx
                
                moved_tile = state_copy[position]
                state_copy[position], state_copy[self.zero_position] = state_copy[self.zero_position], state_copy[position]
                children.append((fx, state_copy, self.current_state, cost, hx, moved_tile))

        elif self.zero_position == self.size/2:
            new_zero_positions = [self.zero_position + 1,
                                  self.zero_position - (self.size//2),
                                  self.zero_position + (self.size//2 - 1),
                                  self.zero_position - (self.size//2 - 1),
                                  self.zero_position - 1]
            
            for i, position in enumerate(new_zero_positions):
                state_copy = self.current_state.copy() # Deep copy

                if(mode == 0):
                    hx = 0
                elif(mode == 1):
                    hx = hammingDistance(state_copy, self.goal_states)
                elif(mode == 2):
                    hx = oneDimensionDistance(state_copy, self.goal_states)

                if i < 2:
                    cost = g[0]
                    fx = g[0] + hx
                elif i == 2:
                    cost = g[1]
                    fx = g[1] + hx
                else:
                    cost = g[2]
                    fx = g[2] + hx

                moved_tile = state_copy[position]
                state_copy[position], state_copy[self.zero_position] = state_copy[self.zero_position], state_copy[position]
                children.append((fx, state_copy, self.current_state, cost, hx, moved_tile))

        elif self.zero_position == self.size/2 - 1:
            new_zero_positions = [self.zero_position - 1,
                                  self.zero_position + (self.size//2),
                                  self.zero_position - (self.size//2 - 1),
                                  self.zero_position + (self.size//2 - 1),
                                  self.zero_position + 1]
            
            for i, position in enumerate(new_zero_positions):
                state_copy = self.current_state.copy() # Deep copy

                if(mode == 0):
                    hx = 0
                elif(mode == 1):
                    hx = hammingDistance(state_copy, self.goal_states)
                elif(mode == 2):
                    hx = oneDimensionDistance(state_copy, self.goal_states)

                if i < 2:
                    cost = g[0]
                    fx = g[0] + hx
                elif i == 2:
                    cost = g[1]
                    fx = g[1] + hx
                else:
                    cost = g[2]
                    fx = g[2] + hx

                moved_tile = state_copy[position]
                state_copy[position], state_copy[self.zero_position] = state_copy[self.zero_position], state_copy[position]
                children.append((fx, state_copy, self.current_state, cost, hx, moved_tile))

        elif self.zero_position == self.size - 1:
            new_zero_positions = [self.zero_position - 1,
                                  self.zero_position - (self.size//2),
                                  self.zero_position - (self.size//2 - 1),
                                  self.zero_position - (self.size//2 + 1),
                                  self.zero_position - int(self.size - 1)]
            
            for i, position in enumerate(new_zero_positions):
                state_copy = self.current_state.copy() # Deep copy

                if(mode == 0):
                    hx = 0
                elif(mode == 1):
                    hx = hammingDistance(state_copy, self.goal_states)
                elif(mode == 2):
                    hx = oneDimensionDistance(state_copy, self.goal_states)

                if i < 2:
                    cost = g[0]
                    fx = g[0] + hx
                elif i == 2:
                    cost = g[1]
                    fx = g[1] + hx
                else:
                    cost = g[2]
                    fx = g[2] + hx

                moved_tile = state_copy[position]
                state_copy[position], state_copy[self.zero_position] = state_copy[self.zero_position], state_copy[position]
                children.append((fx, state_copy, self.current_state, cost, hx, moved_tile))
        else:
            state_copy = self.current_state.copy()
            if(mode == 0):
                hx = 0
            elif(mode == 1):
                hx = hammingDistance(state_copy, self.goal_states)
            elif(mode == 2):
                hx = oneDimensionDistance(state_copy, self.goal_states)

            cost = g[0]
            fx = g[0] + hx

            # The possible new positions for the 0 tile
            new_zero_positions = [self.zero_position + 1,
                                  self.zero_position - 1,
                                  self.zero_position + 4 if self.zero_position < 3 else self.zero_position - 4]

            # Get all possible children and swap the positions.
            for i, position in enumerate(new_zero_positions):
                state_copy = self.current_state.copy() # Deep copy

                moved_tile = state_copy[position]
                # Swap positions
                state_copy[position], state_copy[self.zero_position] = state_copy[self.zero_position], state_copy[position]
                children.append((fx, state_copy, self.current_state, cost, hx, moved_tile))

        return children