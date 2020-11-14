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
        used_nums = []
        p = []
        num = None
        for i in range(size):
            while num in used_nums or num == None:
                num = random.randint(0, 7)
            p.append(num)
            used_nums.append(num)
        puzzles.append(p)
    
    return puzzles, solutions