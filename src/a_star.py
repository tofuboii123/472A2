from graph import *
import queue
from heapq import *
from queue import PriorityQueue

class a_star:

    def __init__(self, graph):
        self.graph = graph
        self.open_list = []                 
        self.closed_list = []
        self.pq = PriorityQueue()
        self.nodes = []
        self.solution_path = []
        self.solution_cost = 0                        


    '''
    Find the solution path using A*
    '''
    def search(self, mode=0):
        print("Searching...")

        # Push initial state into PQ
        self.pq.put((0, self.graph.start_state, None, 0, 0))
        self.open_list.append((0, self.graph.start_state, None, 0, 0))
        self.nodes.append(self.graph.start_state)

        # While there are states in the open list, keep searching
        while not self.pq.empty():

            # TODO
            # if timeout:
            #   return False

            # Remove first element from PQ
            fx, current_node, parent_node, cost, gx = self.pq.get()
            self.nodes.remove(current_node)
            self.open_list.remove((fx, current_node, parent_node, cost, gx))
            self.graph.current_state = current_node


            # Visited nodes
            self.closed_list.append((fx, current_node, parent_node, cost, gx))

            # Check if node is goal
            if self.graph.goal():
                # Show search path
                print("Search path:")

                for state in self.closed_list:
                    print(state)

                self.getSolutionPath()

                print("Least cost: {}".format(self.solution_cost))
                print("Done!\n")
                return True
            
            # Get children of current state
            children = self.graph.getChildren(mode)

            

            # Only keep the children that aren't in the open or closed list
            for child in children:

                old_state = [state for state in self.closed_list if child[1] == state[1]]                # Find if the state is in the closed list.
                
                # Child was not in closed light or child had a greater cost than the one already visited.
                if not old_state:

                    # Child has never been visited so we can add it
                    if not child[1] in self.nodes:
                        self.nodes.append(child[1])
                        self.pq.put((child[0] + fx, child[1], child[2], child[3], child[4]))
                        self.open_list.append((child[0] + fx, child[1], child[2], child[3], child[4]))
                    else:
                        old_state = [state for state in self.open_list if child[1] == state[1]]          # Get the state that has the same one as the child
                        
                        # Compare the costs (Don't forget to do the sum of the cost)
                        if child[0] + fx < old_state[0][0]:                                              # We know there can only be 1 old_state that's the same as the child
                            self.nodes.remove(old_state[0][1])                                           # Remove from the open list
                            self.open_list.remove(old_state[0])
                            
                            old_states = []
                            
                            state = self.pq.get()
                            old_states.append(state)

                            # Get all the states from the PQ until we get the repeated one
                            while state[1] != child[1]:
                                state = self.pq.get()
                                old_states.append(state)

                            # Switch the old state with the new child with a lesser cost (We know for sure it's the last one)
                            old_states[-1] = (child[0] + fx, child[1], child[2], child[3], child[4])                      

                            # Put all the removed states back into the PQ
                            for s in old_states:
                                self.pq.put(s)

                            # Add the new state into the open list
                            self.nodes.append(old_states[-1][1])
                            self.open_list.append((old_states[-1][0], old_states[-1][1], old_states[-1][2], old_states[-1][3], old_states[-1][4]))

                # The child state has a lower cost and must be replaced and revisited to find the shortest path
                elif child[0] < old_state[0][-1]:
                    # self.closed_list.remove(old_state[0])
                    self.nodes.append(child[1])
                    self.pq.put((child[0] + fx, child[1], child[2], child[3], child[4]))
                    self.open_list.append((child[0] + fx, child[1], child[2], child[3], child[4]))

            
        return False



    '''
    Get the solution path from the closed list
    '''
    def getSolutionPath(self):

        # Start with the solution and backtrack to the start state
        self.solution_path.append((self.closed_list[-1][1], self.closed_list[-1][3]))
        parent = self.closed_list[-1][2]


        while not parent == None:
            for state in self.closed_list:
                if parent == state[1]:
                    self.solution_path.append((state[1], state[3]))
                    parent = state[2]
                    break

        self.solution_path.reverse()

        print("\nSolution Path:")

        for state in self.solution_path:
            self.solution_cost = self.solution_cost + state[1]
            print(state)