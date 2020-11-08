from graph import *
import queue
from heapq import *
from queue import PriorityQueue

class UCS:

    def __init__(self, graph):
        self.graph = graph
        self.open_list = []                 
        self.closed_list = []
        self.pq = PriorityQueue()
        self.nodes = []                      


    '''
    Find the solution path using uniform cost search
    '''
    def search(self):
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
            children = self.graph.getChildren()

            # Only keep the children that aren't in the open or closed list
            for child in children:

                add = True

                if not child[1] in self.closed_list:
                    if not child[1] in self.nodes:
                        self.nodes.append(child[1])
                        self.pq.put((child[0] + cost, child[1], child[2]))
                        self.open_list.append((child[0] + cost, child[1], child[2]))
                    else:
                        old_state = [state for state in self.open_list if self.nodes[-1] in state]
                        if child[0] < old_state[0][0]:
                            self.nodes.remove(old_state[0][1])
                            self.open_list.remove(old_state[0])
                            
                            old_states = []
                            
                            state = self.pq.get()

                            while state[1] != child[1]:
                                state = self.pq.get()
                                old_states.append(state)

                            if old_states[-1][0] > child[0]:
                                old_states[-1] = child

                            for s in old_states:
                                self.pq.put(s)

                            self.nodes.append(child[1])
                            self.pq.put((child[0] + cost, child[1], child[2]))
                            self.open_list.append((child[0] + cost, child[1], child[2]))
                        
                        
                    # repeated_children = [state for state in self.open_list if child[1] in state]

                    # if repeated_children:
                    #     if repeated_children[0][2] != parent_node:
                    #          if repeated_children[0][0] < cost:

                    
                    # # If child is in open list but has a lower cost, remove the higher cost one and add the new child
                    # for i, state in enumerate(self.open_list):
                    #     if child[1] == state[1]:
                    #         if child[0] < state[0]:
                    #             self.open_list.remove(state)
                    #             add = True
                    #             break
                    #         else:
                    #             add = False

                    # if add:
                    #     self.pq.put((child[0] + cost, child[1], child[2]))
                    #     self.open_list.append((child[0] + cost, child[1], child[2]))
                    #     # heappush(self.open_list, (child[0] + cost, child[1], child[2]))

            print("Open List: ")
            for state in self.open_list:
                print(state)

            # print("Children: {}".format(children))
        
        return False

            

        

        
        

