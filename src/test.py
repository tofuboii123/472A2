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



# goal_states = [[1, 2, 3, 4, 5, 6, 7, 0], [1, 3, 5, 7, 2, 4, 6, 0]]

# Easy puzzle for testing
test_puzzle = [1, 2, 3, 4, 5, 6, 0, 7]
test_puzzle2 = [1, 3, 5, 7, 2, 4, 0, 6]
test_puzzle3 = [1, 2, 3, 4, 5, 0, 6, 7]
test_puzzle4 = [1, 2, 0, 4, 5, 6, 7, 3]
test_puzzle5 = [1, 3, 5, 7, 0, 2, 4, 6]
test_puzzle6 = [0, 4, 3, 7, 2, 1, 5, 6]
test_puzzle7 = [6, 5, 3, 4, 0, 1, 2, 7]
test_puzzle8 = [7, 3, 4, 2, 6, 0, 1, 5]

puzzles, goal_states = generatePuzzle(2, 8)

writePuzzlesToFile(puzzles)

ucs_stats = []
gbfs_h1_stats = []
gbfs_h2_stats = []
astar_h1_stats = []
astar_h2_stats = []

ucs_name = "ucs"
astar_h1_name = "astar-h1"
astar_h2_name = "astar-h2"
gbfs_h1_name = "gbfs-h1"
gbfs_h2_name = "gbfs-h2"

p = Puzzle("puzzles/test.txt", (2, 4))


g = Graph(goal_states, len(test_puzzle4), p.puzzles[0])

aStar = a_star(g)
aStar.check_timeout(3)

gbfs = GBFS(g)
gbfs.check_timeout(3)

ucs = UCS(g)
ucs.check_timeout()


# for i, puzzle in enumerate(puzzles):
#     g = Graph(goal_states, len(puzzle), puzzle)

#     aStar = a_star(g)
#     aStar2 = a_star(g)
#     gbfs = GBFS(g)
#     gbfs2 = GBFS(g)
#     ucs = UCS(g)

#     gbfs.check_timeout(1)
#     gbfs2.check_timeout(2)
#     aStar.check_timeout(1)
#     aStar2.check_timeout(2)
#     ucs.check_timeout()

#     writeToFile(i, gbfs_h1_name, gbfs)
#     writeToFile(i, astar_h1_name, aStar)
#     writeToFile(i, ucs_name, ucs)
#     writeToFile(i, gbfs_h2_name, gbfs2)
#     writeToFile(i, astar_h2_name, aStar2)

#     ucs_stats.append((analysis(i, ucs_name, ucs)))
#     gbfs_h1_stats.append((analysis(i, gbfs_h1_name, gbfs)))
#     gbfs_h2_stats.append((analysis(i, gbfs_h2_name, gbfs2)))
#     astar_h1_stats.append((analysis(i, astar_h1_name, aStar)))
#     astar_h2_stats.append((analysis(i, astar_h2_name, aStar2)))

# print("ucs stats:" , ucs_stats)
# print("average ucs: ", averageStats(ucs_stats))
# print("gbfs1 stats: ", gbfs_h1_stats)
# print("average gbfs1: ", averageStats(gbfs_h1_stats))
# print("gbfs2 stats: ", gbfs_h2_stats)
# print("average gbfs2: ", averageStats(gbfs_h2_stats))
# print("astar1 stats: ", astar_h1_stats)
# print("average astar1: ", averageStats(astar_h1_stats))
# print("astar2 stats: ", astar_h2_stats)
# print("average astar2: ", averageStats(astar_h2_stats))

