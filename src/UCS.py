from graph import *
import queue
from heapq import *

class UCS:

    def __init__(self, graph):
        self.graph = graph
        self.open_list = []                 
        self.closed_list = []                      


    '''
    Find the solution path
    '''
    def search(self):

        # Push initial state into PQ
        heappush(self.open_list, (0, self.graph.start_state))       

        # While there are states in the open list, keep searching
        while self.open_list:

            # Remove first element from PQ
            cost, current_node = self.open_list[0]
            self.graph.current_state = current_node
            del self.open_list[0]

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

                print("Done!\n")
                return
            
            # Get children of current state
            children = self.graph.getChildren()

            # Only keep the children that aren't in the open or closed list
            for child in children:
                if not child[1] in self.closed_list and child not in self.open_list:
                    heappush(self.open_list, (child[0] + cost, child[1]))

            

        

        
        

