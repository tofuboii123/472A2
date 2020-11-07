from graph import *
import queue
from heapq import *

class UCS:

    def __init__(self, graph):
        self.graph = graph
        self.open_list = []                 
        self.closed_list = []                      


    '''
    Find the solution path using uniform cost search
    '''
    def search(self):
        print("Searching...")

        # Push initial state into PQ
        heappush(self.open_list, (0, self.graph.start_state, 0))       

        # While there are states in the open list, keep searching
        while self.open_list:

            # TODO
            # if timeout:
            #   return False

            # Remove first element from PQ
            cost, current_node, parent_node = heappop(self.open_list)
            self.graph.current_state = current_node

            # Debugging
            # print("Total cost: {}, Current Node: {}".format(cost, current_node))

            # Visited nodes
            self.closed_list.append((cost, current_node, parent_node))

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
            children = self.graph.getChildren()

            # Only keep the children that aren't in the open or closed list
            for child in children:

                add = True

                if not child[1] in self.closed_list:
                    
                    # If child is in open list but has a lower cost, remove the higher cost one and add the new child
                    for i, state in enumerate(self.open_list):
                        if child[1] == state[1]:
                            if child[0] < state[0]:
                                self.open_list.remove(state)
                                add = True
                                break
                            else:
                                add = False

                    if add:
                        heappush(self.open_list, (child[0] + cost, child[1], child[2]))

            print("Open List: ")
            for state in self.open_list:
                print(state)

            # print("Children: {}".format(children))
        
        return False

            

        

        
        

