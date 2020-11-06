from graph import *
from puzzle import *
from UCS import *

p = Puzzle("puzzles/test.txt", (2, 4))

goal_states = [[[1, 2, 3, 4], [5, 6, 7, 0]], [[1, 3, 5, 7], [2, 4, 6, 0]]]

test_puzzle = [[1, 2, 3, 4], [5, 6, 0, 7]]  # Easy puzzle for testing
test_puzzle2 = [[1, 3, 5, 7], [2, 4, 0, 6]] # Easy puzzle for testing


g1 = Graph(goal_states, test_puzzle)
g2 = Graph(goal_states, test_puzzle2)

ucs = UCS(g1)
ucs2 = UCS(g2)

ucs.search()
ucs2.search()