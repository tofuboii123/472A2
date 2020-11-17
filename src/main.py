from graph import *
from puzzle import *
from UCS import *
from heuristic import *
from a_star import *
from GBFS import *
from utility import *


puzzles, goal_states = generatePuzzle(2, 8)
writePuzzlesToFile(puzzles)

ucs_values = []
gbfs_h1_values = []
gbfs_h2_values = []
astar_h1_values = []
astar_h2_values = []

ucs_stats = {"avg" : [], "total" : []}
gbfs_h1_stats = {"avg" : [], "total" : []}
gbfs_h2_stats = {"avg" : [], "total" : []}
astar_h1_stats = {"avg" : [], "total" : []}
astar_h2_stats = {"avg" : [], "total": []}

ucs_name = "ucs"
astar_h1_name = "astar-h1"
astar_h2_name = "astar-h2"
gbfs_h1_name = "gbfs-h1"
gbfs_h2_name = "gbfs-h2"

for i, puzzle in enumerate(puzzles):
    g = Graph(goal_states, len(puzzle), puzzle)

    aStar = a_star(g)
    # aStar2 = a_star(g)
    gbfs = GBFS(g)
    # gbfs2 = GBFS(g)
    ucs = UCS(g)

    gbfs.check_timeout(3)
    # gbfs2.check_timeout(2)
    aStar.check_timeout(3)
    # aStar2.check_timeout(2)
    ucs.check_timeout()

    writeToFile(i, gbfs_h1_name, gbfs)
    writeToFile(i, astar_h1_name, aStar)
    writeToFile(i, ucs_name, ucs)
    # writeToFile(i, gbfs_h2_name, gbfs2)
    # writeToFile(i, astar_h2_name, aStar2)

    ucs_values.append((stats(i, ucs_name, ucs)))
    gbfs_h1_values.append((stats(i, gbfs_h1_name, gbfs)))
    # gbfs_h2_values.append((stats(i, gbfs_h2_name, gbfs2)))
    astar_h1_values.append((stats(i, astar_h1_name, aStar)))
    # astar_h2_values.append((stats(i, astar_h2_name, aStar2)))

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


# print("gbfs2 values: ", gbfs_h2_values)
# print("average gbfs2: ", averageStats(gbfs_h2_values))


print("astar1 values: ", astar_h1_values)
astar_h1_stats["avg"] = averageStats(astar_h1_values)
astar_h1_stats["total"] = totalStats(astar_h1_values)
writeStatsToCSV(astar_h1_name, astar_h1_stats["avg"], astar_h1_stats["total"])


print("average astar1: ", astar_h1_stats["avg"])
print("total astar1: ", astar_h1_stats["total"])


# print("astar2 values: ", astar_h2_values)
# print("average astar2: ", averageStats(astar_h2_values))