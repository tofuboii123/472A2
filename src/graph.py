import copy

class Graph:

    def __init__(self, goal_states, start_state=None):
        self.start_state = start_state                      # Start node
        self.goal_states = goal_states                      # Goal states
        self.current_state = self.start_state               # Current state of puzzle
        self.zero_position = self.getZeroPosition()         # Tuple (row, col)


    '''
    # Get the position of zero
    '''
    def getZeroPosition(self):
        for i, row in enumerate(self.current_state):
                for j, col in enumerate(row):
                    if(col == 0):
                        return (i, j)


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
    def getChildren(self):
        self.zero_position = self.getZeroPosition()

        children = []

        # Old zero position                
        old_zero_pos = (self.zero_position[0], self.zero_position[1])

        # Corner positions
        if self.zero_position == (0, 0):
            new_zero_positions = [(self.zero_position[0], self.zero_position[1] + 1),
                                  (self.zero_position[0] + 1, self.zero_position[1]),
                                  (self.zero_position[0], self.zero_position[1] + 3),
                                  (self.zero_position[0] + 1, self.zero_position[1] + 1),
                                  (self.zero_position[0] + 1, self.zero_position[1] + 3)]
            
            for i, position in enumerate(new_zero_positions):
                if i < 2:
                    cost = 1
                elif i == 2:
                    cost = 2
                else:
                    cost = 3

                state_copy = copy.deepcopy(self.current_state) # Deep copy
                state_copy[position[0]][position[1]], state_copy[old_zero_pos[0]][old_zero_pos[1]] = state_copy[old_zero_pos[0]][old_zero_pos[1]], state_copy[position[0]][position[1]]
                children.append((cost, state_copy))

        elif self.zero_position == (1, 0):
            new_zero_positions = [(self.zero_position[0], self.zero_position[1] + 1),
                                  (self.zero_position[0] - 1, self.zero_position[1]),
                                  (self.zero_position[0], self.zero_position[1] + 3),
                                  (self.zero_position[0] - 1, self.zero_position[1] + 1),
                                  (self.zero_position[0] - 1, self.zero_position[1] + 3)]
            
            for i, position in enumerate(new_zero_positions):
                if i < 2:
                    cost = 1
                elif i == 2:
                    cost = 2
                else:
                    cost = 3

                state_copy = copy.deepcopy(self.current_state) # Deep copy
                state_copy[position[0]][position[1]], state_copy[old_zero_pos[0]][old_zero_pos[1]] = state_copy[old_zero_pos[0]][old_zero_pos[1]], state_copy[position[0]][position[1]]
                children.append((cost, state_copy))

        elif self.zero_position == (0, 3):
            new_zero_positions = [(self.zero_position[0], self.zero_position[1] - 1),
                                  (self.zero_position[0] + 1, self.zero_position[1]),
                                  (self.zero_position[0], self.zero_position[1] - 3),
                                  (self.zero_position[0] + 1, self.zero_position[1] - 1),
                                  (self.zero_position[0] + 1, self.zero_position[1] - 3)]
            
            for i, position in enumerate(new_zero_positions):
                if i < 2:
                    cost = 1
                elif i == 2:
                    cost = 2
                else:
                    cost = 3

                state_copy = copy.deepcopy(self.current_state) # Deep copy
                state_copy[position[0]][position[1]], state_copy[old_zero_pos[0]][old_zero_pos[1]] = state_copy[old_zero_pos[0]][old_zero_pos[1]], state_copy[position[0]][position[1]]
                children.append((cost, state_copy))

        elif self.zero_position == (1, 3):
            new_zero_positions = [(self.zero_position[0], self.zero_position[1] - 1),
                                  (self.zero_position[0] - 1, self.zero_position[1]),
                                  (self.zero_position[0], self.zero_position[1] - 3),
                                  (self.zero_position[0] - 1, self.zero_position[1] - 1),
                                  (self.zero_position[0] - 1, self.zero_position[1] - 3)]
            
            for i, position in enumerate(new_zero_positions):
                if i < 2:
                    cost = 1
                elif i == 2:
                    cost = 2
                else:
                    cost = 3

                state_copy = copy.deepcopy(self.current_state) # Deep copy
                state_copy[position[0]][position[1]], state_copy[old_zero_pos[0]][old_zero_pos[1]] = state_copy[old_zero_pos[0]][old_zero_pos[1]], state_copy[position[0]][position[1]]
                children.append((cost, state_copy))
        else:
            cost = 1

            # The possible new positions for the 0 tile
            new_zero_positions = [(self.zero_position[0], self.zero_position[1] + 1),
                                  (self.zero_position[0], self.zero_position[1] - 1),
                                  (self.zero_position[0] + 1 if self.zero_position[0] == 0 else self.zero_position[0] - 1, self.zero_position[1])]

            # Get all possible children and swap the positions.
            for i, position in enumerate(new_zero_positions):
                state_copy = copy.deepcopy(self.current_state) # Deep copy
                state_copy[position[0]][position[1]], state_copy[old_zero_pos[0]][old_zero_pos[1]] = state_copy[old_zero_pos[0]][old_zero_pos[1]], state_copy[position[0]][position[1]]
                children.append((cost, state_copy))

        return children