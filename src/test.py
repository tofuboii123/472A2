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

ucs_values = []
gbfs_h1_values = []
gbfs_h2_values = []
astar_h1_values = []
astar_h2_values = []

ucs_name = "ucs"
astar_h1_name = "astar-h1"
astar_h2_name = "astar-h2"
gbfs_h1_name = "gbfs-h1"
gbfs_h2_name = "gbfs-h2"

p = Puzzle("puzzles/test.txt", (2, 4))


# g = Graph(goal_states, len(test_puzzle4), test_puzzle7)

# aStar = a_star(g)
# aStar.check_timeout(1)

# writeToFile(0, astar_h1_name, aStar)

# gbfs = GBFS(g)
# gbfs.check_timeout(1)
# writeToFile(0, gbfs_h1_name, gbfs)


# ucs = UCS(g)
# ucs.check_timeout()
# writeToFile(0, ucs_name, ucs)


ucs_stats = {"avg" : [], "total" : []}
gbfs_h1_stats = {"avg" : [], "total" : []}
gbfs_h2_stats = {"avg" : [], "total" : []}
astar_h1_stats = {"avg" : [], "total" : []}
astar_h2_stats = {"avg" : [], "total": []}

for i, puzzle in enumerate(p.puzzles):
    g = Graph(goal_states, len(puzzle), puzzle)

    aStar = a_star(g)
    aStar2 = a_star(g)
    gbfs = GBFS(g)
    gbfs2 = GBFS(g)
    ucs = UCS(g)

    gbfs.check_timeout(1)
    gbfs2.check_timeout(2)
    aStar.check_timeout(1)
    aStar2.check_timeout(2)
    ucs.check_timeout()

    writeToFile(i, gbfs_h1_name, gbfs)
    writeToFile(i, astar_h1_name, aStar)
    writeToFile(i, ucs_name, ucs)
    writeToFile(i, gbfs_h2_name, gbfs2)
    writeToFile(i, astar_h2_name, aStar2)

    ucs_values.append((stats(i, ucs_name, ucs)))
    gbfs_h1_values.append((stats(i, gbfs_h1_name, gbfs)))
    gbfs_h2_values.append((stats(i, gbfs_h2_name, gbfs2)))
    astar_h1_values.append((stats(i, astar_h1_name, aStar)))
    astar_h2_values.append((stats(i, astar_h2_name, aStar2)))

print("ucs values:" , ucs_values)
ucs_stats["avg"] = averageStats(ucs_values)
ucs_stats["total"] = totalStats(ucs_values)
writeStatsToCSV(ucs_name, ucs_stats["avg"], ucs_stats["total"])

print("average ucs: ", ucs_stats["avg"])
print("total ucs: ", ucs_stats["total"])

print("gbfs1 values: ", gbfs_h1_values)
gbfs_h1_stats["avg"] = averageStats(gbfs_h1_values)
gbfs_h1_stats["total"] = totalStats(gbfs_h1_values)
writeStatsToCSV(gbfs_h1_name, gbfs_h1_stats["avg"], gbfs_h1_stats["total"])


print("average gbfs1: ", gbfs_h1_stats["avg"])
print("total gbfs1: ", gbfs_h1_stats["total"])


print("astar1 values: ", astar_h1_values)
astar_h1_stats["avg"] = averageStats(astar_h1_values)
astar_h1_stats["total"] = totalStats(astar_h1_values)
writeStatsToCSV(astar_h1_name, astar_h1_stats["avg"], astar_h1_stats["total"])


print("average astar1: ", astar_h1_stats["avg"])
print("total astar1: ", astar_h1_stats["total"])
