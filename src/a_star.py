from graph import *
import queue
from heapq import *
from queue import PriorityQueue
import time
from threading import Timer, Thread
import multiprocessing
from multiprocessing import *

class a_star:

    def __init__(self, graph):
        self.graph = graph
        self.open_list = []                 
        self.closed_list = []
        self.pq = PriorityQueue()
        self.nodes = []
        self.solution_path = []
        self.solution_cost = 0
        self.original_f = []                                
        self.closed_f = [] 
        self.p = Thread(target=self.search, name="UCS", args=(0, {}))
        self.timeout = False 
        self.return_dict = {"success":False, "execution":0}


    '''
    Find the solution path using A*
    '''
    def search(self, mode):
        start_time = time.time()
        print("Searching...")

        # Push initial state into PQ
        self.pq.put((0, self.graph.start_state, None, 0, 0, 0, 0))
        self.open_list.append((0, self.graph.start_state, None, 0, 0, 0, 0))
        self.nodes.append(self.graph.start_state)
        self.original_f.append(0)

        # While there are states in the open list, keep searching
        while not self.pq.empty():

            if self.timeout:
                self.return_dict["success"] = False
                return 

            # Remove first element from PQ
            fx, current_node, parent_node, cost, hx, moved_tile, prev_cost = self.pq.get()

            # print(fx, current_node, parent_node, cost, hx, moved_tile, prev_cost, prev_cost)

            self.nodes.remove(current_node)
            idx = self.open_list.index((fx, current_node, parent_node, cost, hx, moved_tile, prev_cost))
            self.open_list.remove((fx, current_node, parent_node, cost, hx, moved_tile, prev_cost))
            self.graph.current_state = current_node

            # Visited nodes
            self.closed_list.append((fx, current_node, parent_node, cost, hx, moved_tile, prev_cost))
            self.closed_f.append(self.original_f[idx])
            self.original_f.pop(idx)

            # Check if node is goal
            if self.graph.goal():
                execution_time = time.time() - start_time
                # Show search path
                # print("Search path:")

                # for state in self.closed_list:
                #     print(state)

                self.getSolutionPath()

                print("Cost: {}".format(self.solution_cost))
                print("The A* search took ", execution_time, " seconds.")
                print("Done!\n")
                self.return_dict["success"] = True
                self.return_dict["execution"] = execution_time
                return 
            
            # Get children of current state
            children = self.graph.getChildren(prev_cost, mode)

            # Only keep the children that aren't in the open or closed list
            for child in children:

                visited_states = [state for state in self.closed_list if child[1] == state[1]]                # Find if the state is in the closed list.
                
                # Child was not in closed light or child had a greater cost than the one already visited.
                if not visited_states:

                    # Child has never been visited so we can add it
                    if not child[1] in self.nodes:
                        self.nodes.append(child[1])
                        self.pq.put((child[0], child[1], child[2], child[3], child[4], child[5], child[6]))
                        self.open_list.append((child[0], child[1], child[2], child[3], child[4], child[5], child[6]))
                        self.original_f.append(child[0])
                    else:
                        visited_states = [state for state in self.open_list if child[1] == state[1]]          # Get the state that has the same one as the child
                        
                        # Compare the costs (Don't forget to do the sum of the cost)
                        if child[0] < visited_states[0][0]:                                              # We know there can only be 1 old_state that's the same as the child
                            self.nodes.remove(visited_states[0][1])                                           # Remove from the open list
                            idx = self.open_list.index(visited_states[0])
                            self.open_list.remove(visited_states[0])
                            self.original_f.pop(idx)

                            old_states = []
                            
                            state = self.pq.get()
                            old_states.append(state)

                            # Get all the states from the PQ until we get the repeated one
                            while state[1] != child[1]:
                                state = self.pq.get()
                                old_states.append(state)


                            # Switch the old state with the new child with a lesser cost (We know for sure it's the last one)
                            old_states[-1] = (child[0], child[1], child[2], child[3], child[4], child[5], child[6]) 
                            self.original_f.append(child[0])

                            # Put all the removed states back into the PQ
                            for s in old_states:
                                self.pq.put(s)

                            # Add the new state into the open list
                            self.nodes.append(old_states[-1][1])
                            self.open_list.append(old_states[-1])

                # The child state has a lower cost and must be replaced and revisited to find the shortest path
                elif child[0] < visited_states[0][-1]:
                    # self.closed_list.remove(old_state[0])
                    self.nodes.append(child[1])
                    self.pq.put((child[0], child[1], child[2], child[3], child[4], child[5], child[6]))
                    self.open_list.append((child[0], child[1], child[2], child[3], child[4], child[5], child[6]))
                    self.original_f.append(child[0])

        self.return_dict["success"] = False

    '''
    Get the solution path from the closed list
    '''
    def getSolutionPath(self):

        # Start with the solution and backtrack to the start state
        self.solution_path.append((self.closed_list[-1][1], self.closed_list[-1][3], self.closed_list[-1][5]))
        parent = self.closed_list[-1][2]


        while not parent == None:
            for state in self.closed_list:
                if parent == state[1]:
                    self.solution_path.append((state[1], state[3], state[5]))
                    parent = state[2]
                    break

        self.solution_path.reverse()

        print("\nSolution Path:")

        for state in self.solution_path:
            self.solution_cost = self.solution_cost + state[1]
            print(state)

    '''
    End the seaching process if it's longer than 60 seconds
    '''
    def stop_search(self):
        if(self.p.is_alive()):
            print('Search A* is now terminated')
            self.timeout = True
            self.p.join()
        else:
            print('Search A* is already terminated')

    '''
    Check if the search goes over 60 seconds
    '''
    def check_timeout(self, mode):
        self.p = Thread(target=self.search, name="A*", args=(mode,))   #Creating thread for this search function
        t = Timer(60, self.stop_search)                                            #Stop function after 60 seconds
        t.start()                                                                  #Start timer
        self.p.start()                                                             #Start search algorithm  
        self.p.join()                                                              #Joining all the returned values      

        if(self.return_dict["success"]):
            t.cancel()                                                             #Stopping timer if the search was done before timeout