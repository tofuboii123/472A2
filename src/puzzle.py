class Puzzle:
    def __init__(self, path_to_puzzle, size):
        self.size = size
        self.puzzles = self.getPuzzle(path_to_puzzle)
    
    '''
    Get the puzzle from file
    '''
    def getPuzzle(self, path_to_puzzle):
        puzzles_list = []

        # Read each line of the file
        puzzle_file = open(path_to_puzzle, "r")
        puzzles_list = puzzle_file.read().splitlines()

        # Get the individual numbers
        split_puzzles = []
        for p in puzzles_list:
            split_puzzles.append(p.split(" "))

        # TODO can we change this so it's not shit?
        for i, row in enumerate(split_puzzles):
            for j, col in enumerate(row):
                split_puzzles[i][j] = int(split_puzzles[i][j])
                

        # Separate into the correct sizes
        real_puzzles = []
        for s in split_puzzles:
            real_puzzles.append([s[:self.size[1]], s[self.size[1]:]])

        return real_puzzles