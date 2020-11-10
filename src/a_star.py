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


    '''
    Find the solution path using uniform cost search
    '''
    def search(self, mode=0):
        print("Searching...")

        # Push initial state into PQ
        self.pq.put((0, self.graph.start_state, None))
        self.open_list.append((0, self.graph.start_state, None))
        self.nodes.append(self.graph.start_state)
        # heappush(self.open_list, (0, self.graph.start_state, 0))       

        # While there are states in the open list, keep searching
        while not self.pq.empty():

            # TODO
            # if timeout:
            #   return False

            # Remove first element from PQ
            cost, current_node, parent_node = self.pq.get()
            self.nodes.remove(current_node)
            self.open_list.remove((cost, current_node, parent_node))
            self.graph.current_state = current_node

            # Debugging
            # print("Total cost: {}, Current Node: {}".format(cost, current_node))

            # Visited nodes
            self.closed_list.append(current_node)

            # Check if node is goal
            if self.graph.goal():
                # Show search path
                print("Search path:")
                for state in self.closed_list:
                    print(state)

                print("Least cost: {}".format(cost))
                print("Done!\n")
                return True
            
            # Get children of current state
            children = self.graph.getChildren(mode)

            # Only keep the children that aren't in the open or closed list
            for child in children:
                if not child[1] in self.closed_list:

                    # Child has never been visited so we can add it
                    if not child[1] in self.nodes:
                        self.nodes.append(child[1])
                        self.pq.put((child[0] + cost, child[1], child[2]))
                        self.open_list.append((child[0] + cost, child[1], child[2]))
                    else:
                        old_state = [state for state in self.open_list if child[1] == state[1]]          # Get the state that has the same one as the child
                        
                        # Compare the costs (Don't forget to do the sum of the cost)
                        if child[0] + cost < old_state[0][0]:                                            # We know there can only be 1 old_state that's the same as the child
                            self.nodes.remove(old_state[0][1])                                           # Remove from the open list
                            self.open_list.remove(old_state[0])
                            
                            old_states = []
                            
                            state = self.pq.get()
                            old_states.append(state)

                            # Get all the states from the PQ until we get the repeated one
                            while state[1] != child[1]:
                                state = self.pq.get()
                                old_states.append(state)

                            old_states[-1] = (child[0] + cost, child[1], child[2])                      # Switch the old state with the new child with a lesser cost (We know for sure it's the last one)

                            # Put all the removed states back into the PQ
                            for s in old_states:
                                self.pq.put(s)

                            # Add the new state into the open list
                            self.nodes.append(old_states[-1][1])
                            self.open_list.append((old_states[-1][0], old_states[-1][1], old_states[-1][2]))
                        
            # print("Children: {}".format(children))
        
        return False