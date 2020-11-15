from graph import *
from puzzle import *
from UCS import *
from heuristic import *
from a_star import *
from GBFS import *
from utility import *
from threading import Timer
import multiprocessing

def stop_search():
    if p.is_alive():
        print('Search is now terminated')
        p.terminate()
        p.join()


p = Puzzle("puzzles/test.txt", (2, 4))

# goal_states = [[1, 2, 3, 4, 5, 6, 7, 0], [1, 3, 5, 7, 2, 4, 6, 0]]

# Easy puzzle for testing
test_puzzle = [1, 2, 3, 4, 5, 6, 0, 7]  
test_puzzle2 = [1, 3, 5, 7, 2, 4, 0, 6] 
test_puzzle3 = [1, 2, 3, 4, 5, 0, 6, 7]
test_puzzle4 = [1, 2, 0, 4, 5, 6, 7, 3]
test_puzzle5 = [1, 3, 5, 7, 0, 2, 4, 6]
test_puzzle6 = [0, 4, 3, 7, 2, 1, 5, 6]
test_puzzle7 = [6, 5, 3, 4, 0, 1, 2, 7]


puzzles, goal_states = generatePuzzle(1, 8)

for puzzle in puzzles:
    g = Graph(goal_states, len(puzzle), puzzle)
    
    aStar = a_star(g)
    gbfs = GBFS(g)
    ucs = UCS(g)

    aStar.check_timeout(1)
    aStar.check_timeout(2)

    ucs.check_timeout()
    
    gbfs.check_timeout(1)
    gbfs.check_timeout(2)

# g1 = Graph(goal_states, test_puzzle7)
# ucs = UCS(g1)
# ucs.search()

# aStar = a_star(g1)
# # aStar.search(1)
# aStar.search(1)

# g2 = Graph(goal_states, test_puzzle2)
# ucs2 = UCS(g2)
# ucs2.search()

# g3 = Graph(goal_states, p.puzzles[1])
# gbfs = GBFS(g3)