import random

'''
Generate a random puzzle and its solution
'''
def generatePuzzle(num, size):
    puzzles = []

    solutions = [[i for i in range(size) if i > 0]]
    solutions[0].append(0)

    solutions.append([i for i in range(size) if i % 2 == 1])
    
    for i in range(size):
        if i % 2 == 0 and i > 0:
            solutions[1].append(i)
    
    solutions[1].append(0)

    for i in range(num):
        p = []
        num = None
        for i in range(size):
            while num in p or num == None:
                num = random.randint(0, size - 1)
            p.append(num)
        puzzles.append(p)
    
    return puzzles, solutions


def analysis(puzzle_num, file_name, search_algo):
    return len(search_algo.closed_list), len(search_algo.solution_path), search_algo.return_dict["execution"] if search_algo.return_dict["success"] else None, search_algo.solution_cost


def writeToFile(puzzle_num, file_name, search_algo):
    writeSearchToFile(puzzle_num, file_name, search_algo)
    writeSolutionToFile(puzzle_num, file_name, search_algo)


def writeSearchToFile(puzzle_num, file_name, search_algo):

    with open("search/{}_{}_search.txt".format(puzzle_num, file_name), "w") as f:

        for i, state in enumerate(search_algo.closed_list):

            # Different values depending on the algorithm
            if "astar" in file_name:
                fx = search_algo.closed_f[i]
                gx = state[3]
                hx = state[4]
            elif "gbfs" in file_name:
                fx = 0
                gx = 0
                hx = state[0]
            else:
                gx = state[3]
                fx = 0
                hx = 0

            # Write the values
            f.write("{} {} {} ".format(fx, gx, hx))
            for s in state[1]:
                f.write("{} ".format(s))
            
            f.write("\n")
        
        if not search_algo.return_dict["success"]:
            f.write("no solution")



def writeSolutionToFile(puzzle_num, file_name, search_algo):
    with open("solution/{}_{}_solution.txt".format(puzzle_num, file_name), "w") as f:
        if not search_algo.return_dict["success"]:
            f.write("no solution")
        else:
            for state in search_algo.solution_path:
                f.write("{} {} ".format(state[2], state[1]))

                for s in state[0]:
                    f.write("{} ".format(s))
                
                f.write("\n")
            
            f.write("{} {}".format(search_algo.solution_cost, search_algo.return_dict["execution"]))




def averageSearchLength(stats):
    return sum(s[0] for s in stats)/len(stats)

def averageSolutionLength(stats):
    sum = 0
    total = 0

    for stat in stats:
        if not stat[1] == 0:
            sum = sum + stat[1]
            total = total + 1
    
    return sum/total

def averageNoSolution(stats):
    total = 0

    for stat in stats:
        if stat[2] == None:
            total += 1

    return total, total/len(stats)

def averageExecTime(stats):
    sum = 0
    total = 0

    for stat in stats:
        if not stat[2] == None:
            sum = sum + stat[2]
            total = total + 1
    
    return sum/total

def averageCost(stats):
    sum = 0
    total = 0

    for stat in stats:
        if not stat[2] == None:
            sum = sum + stat[3]
            total = total + 1
    
    return sum/total

def averageStats(stats):
    return averageSearchLength(stats), averageSolutionLength(stats), averageNoSolution(stats), averageExecTime(stats), averageCost(stats)


